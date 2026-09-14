# bellakoosh.com

Static site. No build step, no dependencies, no framework. Every page is plain HTML
that works with JavaScript disabled; JS only adds the mobile nav, scroll reveals, the
reading-progress needle, section highlighting, and the In Rotation rig.

All nine pages carry the real content brief (positioning, roles, dates, metrics, teaching
thesis, leadership, footer). Only two things are still marked: a LinkedIn URL and Chillzu's
year — both genuinely absent from the brief, not guessed at. Start with `EDITING.md`, then
`CONTENT-CHECKLIST.md`.

### Page lengths at 1280 x 900

| Page | Height | Screens |
|---|---|---|
| index | 2309px | 2.57 |
| work | 1795px | 1.99 |
| soundexchange | 2312px | 2.57 |
| bearcheck | 2250px | 2.50 |
| lipor | 2054px | 2.28 |
| chillzu | 1909px | 2.12 |
| teaching | 2604px | 2.89 |
| about | 2304px | 2.56 |
| in-rotation | 1900px | 2.11 |

Every project page (SoundExchange, BearCheck, LIPOR, Chillzu) puts what it was, the role,
the problem, what was done, the outcome, and the skill chips above the fold — the rest is
two supporting sections. Teaching runs a bit longer because it's carrying the four
teaching→product pairs plus the four-role history; that length is content-justified, not
padding. In Rotation's whole interactive rig — crate and console — fits in the first
viewport at 900px tall.

## Run it locally

```bash
cd bellakoosh
python3 -m http.server 8000
# open http://localhost:8000
```

Opening `index.html` directly also works — every path is relative.

## Deploy

Drag the `bellakoosh` folder into Netlify, Vercel, Cloudflare Pages, or GitHub Pages.
There is nothing to compile.

## Structure

```
index.html             Home — hero, the collection, closing band
work.html              The full collection
soundexchange.html     Project — Product Management Intern
bearcheck.html         Project — Co-Founder, Sales & Growth
lipor.html             Project — LIPOR / CREW, strategy & consulting
chillzu.html           Project — founder, early product origin story
teaching.html          Thesis, four teaching→product pairs, four-role history
about.html             Hi, I'm Bella — narrative, quick facts, leadership strip
in-rotation.html       Live playlist deck/mixer concept (see "In Rotation" below)

scripts/sync-rotation.mjs        Pulls the playlist, writes assets/data/rotation.json
.github/workflows/sync-rotation.yml   Runs the sync daily via GitHub Actions
assets/data/rotation.json        The synced data. Starts as an honest empty state.

assets/css/site.css    The whole design system, one file, @layer-ordered
assets/js/site.js      Nav, scroll reveals, progress needle, section nav
assets/js/rotation.js  Deck transport, crossfader, pitch — In Rotation only
assets/resume/         Replace bella-koosh-resume.pdf (a placeholder is there)
assets/img/            Artifacts and photography
assets/audio/          Optional audio for In Rotation
_source/               The generators. Optional — see _source/README.md

EDITING.md             Where content lives and which patterns to copy
CONTENT-CHECKLIST.md   What to supply, in priority order
```

## Design system

Extracted from the Stitch export (`The Record Collection` + `Sonic Artifact`).

| Token | Value | Use |
|---|---|---|
| `--ivory` | `#FDFCF8` | base surface |
| `--paper` | `#F2EFE6` | sectional shift |
| `--paper-deep` | `#E7E3D7` | archive sections |
| `--ink` | `#000000` | type, rules, dark chapters |
| `--blue` | `#0055FF` | SoundExchange, interactive states |
| `--orange` | `#FF5500` | BearCheck, content-gap markers |
| `--purple` | `#8800FF` | LIPOR / CREW, the console's mixer accent |

Per-record accent is set with `data-accent="blue|orange|purple|ink"` on any ancestor;
everything inside inherits `--accent`.

Type: **Playfair Display** (display) / **Source Serif 4** (narrative) / **Space Mono**
(metadata, labels, metrics, catalog numbers). Google Fonts, `display=swap`.

Grid: 12 columns desktop, 4 mobile, with the outer columns as a marginalia zone.
Everything is 0px radius. Depth comes from 1px rules and tonal blocks, never shadows.

Motion runs on a 120 BPM grid: `--beat: 500ms`, `--sixteenth: 125ms`. Scroll reveals
stagger at 125ms. `prefers-reduced-motion` disables all of it, including the needle and
the spinning platter.

## The project page

One structure, four pages. The kicker, cover, name, problem sentence, anchor metric,
four-cell spec strip, and skill chips all sit above the fold. Below it: two artifacts
with one-line captions, and two or three single-sentence annotations under a
`Discover/Define/Design/Deliver`-style breakdown specific to each project. Nothing below
the fold repeats anything above it.

Governing rule: **design creates personality, copy communicates information.** Copy never
explains the design. In Rotation has no introduction at all — the rig is the first thing
on the page, fully inside the first viewport.

## The sleeve component

The signature element on the Work page's four-record shelf. On hover or keyboard focus:

1. the sleeve displaces 5px up-left, leaving a ghost border behind
2. the record disc slides 20% out into the gutter and rotates 20°
3. an ink panel covers the cover art with role / what Bella did / one piece of evidence
4. `OPEN RECORD →`

Role and one evidence line sit **below** every sleeve permanently, so the collection is
fully scannable without hovering anything. On touch devices the disc and hover panel are
suppressed rather than shrunk. (This is a different component from In Rotation's
In Rotation is unrelated — see that section below.)

## Cover art — read this before replacing it

The four covers are **data compositions built only from supplied facts**. They are not
reproductions of real project artifacts, and nothing about them asserts work that wasn't
done.

- **SoundExchange** — a repeated manual invitation sequence under a 102pt `3–5`
- **BearCheck** — outreach threads converging into a handful of real relationships
- **LIPOR** — many citizen entry points narrowing to a single reuse outcome
- **Chillzu** — an archive sleeve, mis-registered print, deliberately raw

## Content markers

Two visible markers appear throughout:

- `Content needed` — a fact, sentence, or date that must come from Bella
- `Artifact to add` — an image, screenshot, or document

They render as small burnt-orange dashed chips and are visible **on purpose**: an
incomplete site is acceptable, an inaccurate one is not. There are 2 of them left — a
LinkedIn URL and Chillzu's year, both genuinely absent from the content brief rather than
guessed at. See `CONTENT-CHECKLIST.md`.

## In Rotation

Rebuilt around a real, periodically-synced Spotify playlist, styled as an immersive
dark "deck and mixer" concept — two circular platters (Deck A / Deck B), a static EQ
and crossfader for atmosphere, a giant faint "ROTATION" watermark that drifts on
scroll, and a real, filterable track list underneath. Nothing here is hand-typed track
data: the list is read at runtime from `assets/data/rotation.json`, and that file is
written by a scheduled job, not edited by hand.

### How the data gets there

```
Spotify playlist  →  scripts/sync-rotation.mjs  →  assets/data/rotation.json  →  in-rotation.html
                      (runs in GitHub Actions,       (committed to the repo)      (fetched client-side)
                       on a daily cron)
```

No server runs at request time. A GitHub Actions workflow
(`.github/workflows/sync-rotation.yml`) runs once a day, calls the Spotify Web API,
and commits the result as a plain JSON file. The page just `fetch()`s that file like
any other static asset. This is the same pattern personal "now playing" pages
commonly use — a scheduled sync writing a static file, not a live backend.

**Going live** needs three things only you can provide, since they require your own
Spotify login:

1. A Spotify developer app (**must be created by an account with Premium** — Spotify
   requires this as of February 2026)
2. A one-time browser authorization producing a refresh token
3. Four GitHub repo secrets: `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET`,
   `SPOTIFY_REFRESH_TOKEN`, `SPOTIFY_PLAYLIST_ID`

Full walkthrough was given in chat; the short version is in
`scripts/sync-rotation.mjs`'s header comment. **The refresh token expires six months
after you authorize it** — Spotify's policy, not a bug — so budget for repeating the
one-time login step roughly twice a year. When it expires, the workflow fails loudly
in its own log rather than silently breaking the page; the site keeps showing the last
successful sync until you reauthorize.

Until those secrets exist, `assets/data/rotation.json` holds an honest empty state
(`"tracks": []`) and the page says "Not yet synced" — it does not show placeholder
track names pretending to be real.

### The page itself

`in-rotation.html` reads the JSON and renders:

- **A sync line** — "Synced {date} · {playlist name} ↗" once data exists
- **Artist filter chips** — built from whatever artists are actually in the playlist
- **A track list** — cover art, title, artist, duration, "Open ↗" straight to Spotify
- **Two decks** — clicking a track loads its art/title/artist onto Deck A; whatever was
  there slides to Deck B, same handoff pattern as the Work page's record shelf. If the
  track has a `previewUrl` (Spotify doesn't always supply one), a 30-second preview
  plays — only from that click, never automatically.

The visual language — JetBrains Mono, the specific electric-blue/burnt-orange/deep-purple
values, the glowing platters, the parallax watermark — is intentionally its own thing,
scoped under `.ir-` classes in `assets/css/site.css` (search "SONIC ARTIFACT"). It
doesn't share tokens with the rest of the site on purpose; this page is meant to feel
like a different room. Everything reveals via the sitewide `.rise` scroll system and
fully respects `prefers-reduced-motion` — the platters stop spinning and the parallax
watermark stops moving, no console output, no visual breakage.

## Accessibility floor

- skip link, visible focus rings on every interactive element
- track rows and filter chips are real `<button>`s, reachable and operable by keyboard
- mobile nav is a real button with `aria-expanded`, closes on Escape
- `aria-current="page"` on the active nav item
- SVG covers and waveforms carry `role="img"` labels or `aria-hidden`
- range inputs have `aria-label`s and screen-reader readouts
- reduced motion fully respected

## Verified

- All nine pages return 200 and throw no JavaScript errors
- No broken internal links
- No horizontal overflow at 1440px or 390px on any page
- Mobile checked at 390px, including the nav drawer and the DJ board
- Reduced-motion pass: all content renders, needle hidden, platter static
