# Editing guide

The nine `.html` files are the site. No CMS, no build step. Open one, change the words,
save, refresh.

---

## The rule that shapes every page

**Design creates personality. Copy communicates information.** Copy never explains the
design. If a sentence describes the layout, the metaphor, or how to use the page, delete it.

Every project page is capped at roughly **two and a half screens**. If an edit pushes a
page past that, something else has to come out.

---

## The project page

Four project pages (SoundExchange, BearCheck, LIPOR / CREW, Chillzu) share one structure.
Everything a recruiter needs is above the fold.

```
┌─ kicker ─────────────────────────────────────────────────────┐
│ 01 / RECORD   [DISCIPLINE]                          DATES    │
├───────────────┬─────────────────────┬────────────────────────┤
│ cover art     │ PROJECT NAME        │ 75%+                   │
│               │ one-line problem    │ WHAT IT MEANS          │
│               │                     │ caveat, if any         │
├───────────────┴─────────────────────┴────────────────────────┤
│ PRODUCT   │ MY ROLE   │ THE PROBLEM   │ WHAT I DID           │
├──────────────────────────────────────────────────────────────┤
│ [skill] [skill] [skill] [skill] [skill]                      │
└──────────────────────────────────────────────────────────────┘
        ↑ everything above this line is the first screen

  EVIDENCE            two images, one mono caption each
  WHAT MATTERED       two to four single-sentence annotations
  (aside)             optional — a secondary signal, deliberately quiet
  NEXT RECORD
```

**Rules for keeping it short**

- The problem line is **one sentence**, at most two lines on screen.
- Each spec cell is **one or two sentences**. Never a paragraph.
- Skills are chips, not prose.
- "What mattered" rows are **one sentence each**, opening with a bolded claim. Four max
  (SoundExchange uses Discover / Define / Design / Deliver — the one page that earns four).
- Two artifact slots per page. Not three, not six.

**The anchor** (top right) is either a number or a short phrase:

```html
<!-- number, with a target/projection caveat -->
<p class="anchor__fig">75%+</p>
<p class="anchor__label">Targeted reduction in administrative effort</p>
<p class="anchor__note">6 steps &rarr; 1 flow. A target, not a measured result.</p>

<!-- phrase, when there is no number to lean on -->
<p class="anchor__phrase">Hundreds of users.<br>One relationship<br>at a time.</p>
<p class="anchor__label">Live across UC Berkeley lecture halls</p>
```

Keep the target/projection language on SoundExchange's 75%+ if you ever edit it — it is a
PRD target, not a shipped result, and the page says so on purpose.

**A spec cell**
```html
<div class="spec">
  <span class="mono">My role</span>
  <p>One or two sentences.</p>
</div>
```

**A "what mattered" row**
```html
<div class="moment">
  <span class="mono mono--accent">04</span>
  <p><b>The claim in a few words.</b> One sentence of substance.</p>
</div>
```

**The quiet aside** — a secondary signal that shouldn't compete with the main story
(SoundExchange's permissions finding, BearCheck's feedback-loop note):
```html
<p class="aside">One or two quiet sentences, set in mono, below the moments list.</p>
```

**Swap an artifact slot for a real image**
```html
<figure class="ev">
  <img src="assets/img/workflow-map.png" alt="Describe what the image shows">
  <figcaption class="mono">Workflow map — before and after</figcaption>
</figure>
```

---

## Teaching's two components

**A teaching → product pair** (the four cards under the thesis):
```html
<article class="tp">
  <span class="mono mono--accent">05</span>
  <h3 class="tp__head">The headline claim.</h3>
  <p class="tp__body">One to two sentences of support.</p>
  <p class="tp__pair"><span>Teaching</span>The classroom version <b>&rarr;</b> <span>Product</span>The product version</p>
</article>
```
Four is the right number — it's what makes the thesis feel grounded rather than stretched.
Adding a fifth dilutes it; don't.

**An experience row** — used by Teaching's "Where I've taught" *and* About's "Things I've
helped lead." Same component, different trailing label:
```html
<div class="exprow">
  <div class="exprow__head">
    <p class="exprow__org">Organization</p>
    <p class="exprow__role">Role &middot; Dates</p>
  </div>
  <p class="exprow__desc">One to two sentences of what the role actually involved.</p>
  <p class="exprow__trail"><span class="mono">What it taught me</span> One italic sentence.</p>
</div>
```
On About, swap the trailing label to `Signal` and list 2–4 skill words instead of a lesson.

---

## Other patterns

**Liner row** (label left, value right — Currently, Quick Facts):
```html
<div class="liner__row"><dt>Label</dt><dd>Value</dd></div>
```

**Skill chip:** `<li><span class="chip">Discovery</span></li>` — use `chip chip--ink`
on Chillzu and About.

**In Rotation is a different system entirely** — it reads real data from
`assets/data/rotation.json` (written by a scheduled sync, not hand-edited) rather than
using inline HTML placeholders. See the "In Rotation" section of `README.md` for how
the sync works and what the JSON looks like. There is nothing to hand-edit on that page
except, optionally, the static deck/mixer chrome around it.

---

## The content marker

```html
<span class="todo">Add</span>
```

A small burnt-orange dashed chip. There are **2** left across the site — a LinkedIn URL
in the footer and Chillzu's year. See `CONTENT-CHECKLIST.md`.

**Replace, don't hide.** If a section's only honest content is a placeholder, delete the
section rather than styling the marker away.

---

## Colour per record

`data-accent` on any ancestor sets the accent for everything inside:

```html
<main id="main" data-accent="orange">
```

`blue` (SoundExchange) &middot; `orange` (BearCheck) &middot; `purple` (LIPOR / CREW) &middot;
`ink` (Chillzu). Chips, rules, links, and the record disc on the Work page's shelf all
follow it. `ink` remaps to a pale bone tone wherever it would otherwise go
black-on-black. In Rotation is the one page that does **not** use this system — it has
its own scoped colour variables (`--ir-blue`, `--ir-orange`, `--ir-purple`) since it's
meant to feel like a different room. See `README.md`.

---

## Adding files

| What | Where | Note |
|---|---|---|
| Résumé | `assets/resume/bella-koosh-resume.pdf` | Keep the filename. A placeholder is there now — this is the only asset still genuinely missing. |
| Portrait | `assets/img/bella.jpg` | Replace the slot on About. |
| Images | `assets/img/` | ~1600px wide for artifacts. Always write real `alt` text. |
| Audio | n/a | In Rotation plays Spotify preview clips fetched live — there’s no local audio folder for this page. |

---

## Changing the nav or footer

Duplicated across all nine pages. Either find-and-replace across the nine files, or edit
`_source/parts.py` and run `_source/build.sh` — **which overwrites every HTML file and
discards content edits.** Given the content is now largely real, treat `_source/` as
read-only reference at this point rather than something you run.

---

## Before going live

- [ ] Replace the résumé placeholder
- [ ] Add the LinkedIn URL (footer, all nine pages)
- [ ] Add Chillzu's year
- [ ] Portrait photo on About
- [ ] Real artifact images in place of the evidence slots (8 total &mdash; two on each of the four project pages)
- [ ] Real `alt` text on every image you add
- [ ] Keep the target/projection language on SoundExchange's 75%+ — it's a PRD target, not a shipped number
- [ ] Re-measure page heights after any edit. Nothing over ~2.5 screens for a project page.
