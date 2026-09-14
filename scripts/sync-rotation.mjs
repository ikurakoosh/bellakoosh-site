#!/usr/bin/env node
/**
 * Pulls the current contents of one Spotify playlist and writes it to
 * assets/data/rotation.json. Runs in GitHub Actions on a schedule — never
 * in the browser, so the client secret and refresh token never ship to
 * a visitor's machine.
 *
 * Requires four environment variables, all provided as GitHub repo secrets:
 *   SPOTIFY_CLIENT_ID
 *   SPOTIFY_CLIENT_SECRET
 *   SPOTIFY_REFRESH_TOKEN
 *   SPOTIFY_PLAYLIST_ID
 *
 * Needs Node 18+ (built-in fetch). No npm dependencies.
 */

const {
  SPOTIFY_CLIENT_ID,
  SPOTIFY_CLIENT_SECRET,
  SPOTIFY_REFRESH_TOKEN,
  SPOTIFY_PLAYLIST_ID,
} = process.env;

const OUT_PATH = new URL("../assets/data/rotation.json", import.meta.url);

function need(name, val) {
  if (!val) {
    console.error(`Missing required env var: ${name}`);
    process.exit(1);
  }
  return val;
}

need("SPOTIFY_CLIENT_ID", SPOTIFY_CLIENT_ID);
need("SPOTIFY_CLIENT_SECRET", SPOTIFY_CLIENT_SECRET);
need("SPOTIFY_REFRESH_TOKEN", SPOTIFY_REFRESH_TOKEN);
need("SPOTIFY_PLAYLIST_ID", SPOTIFY_PLAYLIST_ID);

async function getAccessToken() {
  const basic = Buffer.from(`${SPOTIFY_CLIENT_ID}:${SPOTIFY_CLIENT_SECRET}`).toString("base64");
  const res = await fetch("https://accounts.spotify.com/api/token", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
      "Authorization": `Basic ${basic}`,
    },
    body: new URLSearchParams({
      grant_type: "refresh_token",
      refresh_token: SPOTIFY_REFRESH_TOKEN,
    }),
  });
  if (!res.ok) {
    const body = await res.text();
    throw new Error(
      `Token refresh failed (${res.status}): ${body}\n` +
      `If this is a 400 with "invalid_grant", the refresh token has expired — ` +
      `Spotify refresh tokens expire six months after the original authorization. ` +
      `Repeat the one-time login step (README: "Refreshing the Spotify token") and ` +
      `update the SPOTIFY_REFRESH_TOKEN secret.`
    );
  }
  const data = await res.json();
  return data.access_token;
}

async function getPlaylist(token) {
  const meta = await spotifyGet(`/playlists/${SPOTIFY_PLAYLIST_ID}?fields=name,external_urls,images`, token);

  const tracks = [];
  // Spotify renamed /playlists/{id}/tracks -> /playlists/{id}/items in the
  // February 2026 migration. Using /items is required as of that migration.
  let url = `/playlists/${SPOTIFY_PLAYLIST_ID}/items?limit=50&fields=next,items(item(id,name,duration_ms,external_urls,preview_url,artists(name),album(name,images)))`;
  while (url) {
    const page = await spotifyGet(url, token);
    for (const entry of page.items || []) {
      const item = entry.item;
      if (!item) continue;
      tracks.push({
        id: item.id,
        name: item.name,
        artists: (item.artists || []).map((a) => a.name).join(", "),
        album: item.album ? item.album.name : "",
        image: item.album && item.album.images && item.album.images[0]
          ? item.album.images[0].url
          : null,
        url: item.external_urls ? item.external_urls.spotify : null,
        durationMs: item.duration_ms || null,
        previewUrl: item.preview_url || null, // often null — Spotify has scaled preview_url back site-wide
      });
    }
    // `next` on this endpoint is a full URL; spotifyGet accepts either a
    // path or a full URL, see below.
    url = page.next || null;
  }

  return {
    name: meta.name,
    url: meta.external_urls ? meta.external_urls.spotify : null,
    image: meta.images && meta.images[0] ? meta.images[0].url : null,
    tracks,
  };
}

async function spotifyGet(pathOrUrl, token) {
  const url = pathOrUrl.startsWith("http") ? pathOrUrl : `https://api.spotify.com/v1${pathOrUrl}`;
  const res = await fetch(url, { headers: { Authorization: `Bearer ${token}` } });
  if (!res.ok) {
    const body = await res.text();
    throw new Error(`Spotify GET ${url} failed (${res.status}): ${body}`);
  }
  return res.json();
}

async function main() {
  const token = await getAccessToken();
  const playlist = await getPlaylist(token);

  const payload = {
    updatedAt: new Date().toISOString(),
    playlist: {
      name: playlist.name,
      url: playlist.url,
      image: playlist.image,
    },
    tracks: playlist.tracks,
  };

  const fs = await import("node:fs/promises");
  await fs.mkdir(new URL("../assets/data/", import.meta.url), { recursive: true });
  await fs.writeFile(OUT_PATH, JSON.stringify(payload, null, 2) + "\n");

  console.log(`Wrote ${payload.tracks.length} tracks from "${payload.playlist.name}" to assets/data/rotation.json`);
}

main().catch((err) => {
  console.error(err.message || err);
  process.exit(1);
});
