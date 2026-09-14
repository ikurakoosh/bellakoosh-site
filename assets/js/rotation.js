/* In Rotation — reads assets/data/rotation.json (written by a scheduled
   GitHub Action, see .github/workflows/sync-rotation.yml) and renders a
   real, filterable track list. Clicking a row loads that track onto
   Deck A and hands whatever was on A to Deck B — nothing autoplays;
   audio (where a 30s preview exists) only starts from a real click. */
(function () {
  "use strict";

  var list = document.querySelector("[data-rotation-list]");
  if (!list) return;

  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  var el = {
    sync: document.querySelector("[data-sync-status]"),
    filters: document.querySelector("[data-filters]"),
    tracks: document.querySelector("[data-tracks]"),
    empty: document.querySelector("[data-empty]"),
    deckA: document.querySelector('[data-deck="A"]'),
    deckB: document.querySelector('[data-deck="B"]'),
  };

  var state = { tracks: [], filter: "All", current: null };
  var audio = null;

  function fmtDuration(ms) {
    if (!ms) return "";
    var s = Math.round(ms / 1000);
    return Math.floor(s / 60) + ":" + String(s % 60).padStart(2, "0");
  }

  function fmtSyncDate(iso) {
    try {
      var d = new Date(iso);
      return d.toLocaleDateString(undefined, { month: "short", day: "numeric" });
    } catch (e) {
      return "";
    }
  }

  function deckFields(deckEl) {
    return {
      root: deckEl,
      art: deckEl.querySelector("[data-deck-art]"),
      title: deckEl.querySelector("[data-deck-title]"),
      meta: deckEl.querySelector("[data-deck-meta]"),
    };
  }

  var deckA = el.deckA ? deckFields(el.deckA) : null;
  var deckB = el.deckB ? deckFields(el.deckB) : null;

  function loadDeck(deck, track) {
    if (!deck) return;
    if (track.image) deck.art.src = track.image;
    deck.title.textContent = track.name;
    deck.meta.textContent = track.artists;
    deck.root.classList.add("is-active");
  }

  function selectTrack(track, rowEl) {
    // Handoff: whatever is on A moves to B, the new pick loads onto A —
    // same pattern as clicking a record on the Work page's shelf.
    if (state.current && deckA && deckB) loadDeck(deckB, state.current);
    if (deckA) loadDeck(deckA, track);
    state.current = track;

    Array.prototype.forEach.call(el.tracks.querySelectorAll(".ir-track"), function (r) {
      r.classList.toggle("is-active", r === rowEl);
    });

    if (audio) { audio.pause(); audio = null; }
    if (track.previewUrl) {
      audio = new Audio(track.previewUrl);
      audio.play().catch(function () { /* blocked or unavailable — fine, visual state still updated */ });
    }
  }

  function renderFilters(tracks) {
    var artists = [];
    tracks.forEach(function (t) {
      var name = (t.artists || "").split(",")[0].trim();
      if (name && artists.indexOf(name) === -1) artists.push(name);
    });
    artists = artists.slice(0, 14); // keep the row readable
    if (!artists.length) return;

    el.filters.hidden = false;
    el.filters.innerHTML = "";
    var makeChip = function (label) {
      var b = document.createElement("button");
      b.type = "button";
      b.className = "ir-filter" + (label === "All" ? " is-active" : "");
      b.textContent = label;
      b.addEventListener("click", function () {
        state.filter = label;
        Array.prototype.forEach.call(el.filters.children, function (c) {
          c.classList.toggle("is-active", c === b);
        });
        renderTracks();
      });
      return b;
    };
    el.filters.appendChild(makeChip("All"));
    artists.forEach(function (a) { el.filters.appendChild(makeChip(a)); });
  }

  function renderTracks() {
    el.tracks.innerHTML = "";
    var visible = state.tracks.filter(function (t) {
      return state.filter === "All" || (t.artists || "").indexOf(state.filter) === 0
        || (t.artists || "").split(",")[0].trim() === state.filter;
    });

    visible.forEach(function (t, i) {
      var row = document.createElement("button");
      row.type = "button";
      row.className = "ir-track";

      var img = t.image
        ? '<img class="ir-track__art" src="' + t.image + '" alt="">'
        : '<span class="ir-track__art" aria-hidden="true"></span>';

      row.innerHTML =
        '<span class="ir-track__i">' + String(i + 1).padStart(2, "0") + '</span>' +
        img +
        '<span class="ir-track__name">' +
          '<span class="ir-track__title"></span>' +
          '<span class="ir-track__artist"></span>' +
        '</span>' +
        '<span class="ir-track__dur">' + fmtDuration(t.durationMs) + '</span>' +
        (t.url ? '<a class="ir-track__open" href="' + t.url + '" target="_blank" rel="noopener">Open &#8599;</a>' : '<span></span>');

      row.querySelector(".ir-track__title").textContent = t.name;
      row.querySelector(".ir-track__artist").textContent = t.artists;

      row.addEventListener("click", function (e) {
        if (e.target.closest(".ir-track__open")) return; // let that link behave normally
        selectTrack(t, row);
      });

      el.tracks.appendChild(row);
    });
  }

  function renderEmpty() {
    el.empty.hidden = false;
    if (el.sync) el.sync.textContent = "Not yet synced";
  }

  fetch("assets/data/rotation.json", { cache: "no-store" })
    .then(function (data) {
  state.tracks = Array.isArray(data.tracks) ? data.tracks : [];
  if (!state.tracks.length) { renderEmpty(); return; }

  if (el.sync) {
    var bits = ["Synced " + fmtSyncDate(data.updatedAt)];
    if (data.playlist && data.playlist.url) {
      el.sync.innerHTML = bits[0] + ' &middot; <a href="' + data.playlist.url +
        '" target="_blank" rel="noopener">' + (data.playlist.name || "Open playlist") + " &#8599;</a>";
    } else {
      el.sync.textContent = bits[0];
    }
  }

  renderFilters(state.tracks);
  renderTracks();

  /* Load first two tracks automatically. */
  if (state.tracks[0] && deckA) {
    loadDeck(deckA, state.tracks[0]);
    state.current = state.tracks[0];
  }

  if (state.tracks[1] && deckB) {
    loadDeck(deckB, state.tracks[1]);
  }
})