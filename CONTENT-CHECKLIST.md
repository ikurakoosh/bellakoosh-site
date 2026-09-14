# Content checklist

Most of the site now carries real content — positioning, roles, dates, the SoundExchange
metrics, the teaching thesis, the leadership strip, the footer. What's left is short.

---

## Tier 1 — the two actual gaps

**1. LinkedIn URL.**
The footer on all nine pages has a `LinkedIn ↗` link with no href — marked with the
orange `todo` chip rather than a guessed-at URL. Find `class="todo"` in the footer of any
page (it's identical across all nine) and add the real link once, or run
`_source/build.sh` after editing `_source/parts.py`'s `FOOT` constant.

**2. Chillzu's year.**
`chillzu.html`'s kicker reads "Year `[Add]`." One date, one edit.

---

## Tier 2 — assets, not text

Nothing here is a content gap in the sense of "what do I say" — it's "what do I show."
The copy is already written to work with or without these; adding them only strengthens
the page.

**Résumé.** `assets/resume/bella-koosh-resume.pdf` is a placeholder that says so in plain
text. Every Resume link on the site points here. Replace the file, keep the filename.

**Portrait.** About has one slot for a photo of you.

**Eight project artifacts.** Two per project page — SoundExchange (workflow map, one real
Gherkin scenario), BearCheck (an outreach message, adoption in a lecture hall), LIPOR / CREW
(the chatbot's opening question, where it routes to), Chillzu (original UI, a code
fragment or repo link). Each has a one-line caption already written; the image slot is
what's missing.

**In Rotation isn't a content gap anymore — it's a setup task.** The page has no
hand-typed placeholders left to fill in; it reads a real Spotify playlist through a
scheduled sync. What's actually needed is the one-time account setup (a Spotify
developer app, a login authorization, four GitHub repo secrets) covered in the "In
Rotation" section of `README.md`. Until that's done, the page honestly shows "Not yet
synced" rather than fake track names.

---

## Decisions, not content

**In Rotation without the Spotify setup.** The page is a legitimate final state even
unsynced — the deck/mixer visual and the honest "not yet synced" list are real content,
not a broken placeholder. Audio previews depend on Spotify actually supplying a
`preview_url` per track, which isn't guaranteed; tracks without one still display and
link out to Spotify, they just don't play in place.

**Marker visibility.** Keep the two remaining orange chips (LinkedIn URL, Chillzu's
year) visible until they're filled — they're the forcing function. Don't hide them with CSS.

**`_source/`.** The generators that produced this content pass. Safe to keep as reference;
running `build.sh` again will overwrite any further hand-edits to the HTML files, so treat
it as read-only unless you're making a sitewide change (like the nav or footer) that's
worth scripting.
