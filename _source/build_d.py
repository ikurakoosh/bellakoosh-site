import sys, os, math
sys.path.insert(0, os.path.dirname(__file__))
from parts import head, masthead, FOOT

OUT = os.environ.get("SITE_OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
NEED = '<span class="todo">Add</span>'


# ==================================================================== SHARED: experience strip
# Used by Teaching ("Where I've taught") and About ("Things I've helped lead").
# Org/role/date up top, a one-to-two sentence description, then a short
# trailing line — "What it taught me" or "Signal" — set quietly in italics.

def exprow(org, role, date, desc, trail_label, trail, ident=None):
    idattr = f' id="{ident}"' if ident else ""
    return f"""        <div class="exprow"{idattr}>
          <div class="exprow__head">
            <p class="exprow__org">{org}</p>
            <p class="exprow__role">{role} <span aria-hidden="true">&middot;</span> {date}</p>
          </div>
          <p class="exprow__desc">{desc}</p>
          <p class="exprow__trail"><span class="mono">{trail_label}</span> {trail}</p>
        </div>"""


def exprows(rows):
    return "\n".join(exprow(*r) for r in rows)


# ==================================================================== TEACHING

TP_PAIRS = [
    dict(n="01", head="Start with the person, not the solution.",
         body="You can&rsquo;t teach without understanding what someone already knows. Before deciding what to build, I want to understand a user&rsquo;s current behavior, assumptions, and workarounds.",
         teach="Understand the learner", prod="Understand the user"),
    dict(n="02", head="Confusion is information.",
         body="Teaching taught me not to assume an explanation landed. When several students struggle at the same point, that&rsquo;s a signal about the lesson &mdash; not just the learner.",
         teach="Student confusion", prod="Product signal"),
    dict(n="03", head="Make complicated things feel simple.",
         body="I&rsquo;ve taught programming to kids, English across proficiency levels, and product management to Berkeley students from 8+ majors. Each audience needs a different explanation.",
         teach="Lesson design", prod="Information architecture"),
    dict(n="04", head="Meet people where they are.",
         body="The best lesson doesn&rsquo;t exist independently of the learner. I&rsquo;m not designing for myself &mdash; I&rsquo;m designing for people with different context, confidence, and familiarity.",
         teach="Different learners", prod="Different users"),
]


def tp_card(c):
    return f"""      <article class="tp">
        <span class="mono mono--accent">{c['n']}</span>
        <h3 class="tp__head">{c['head']}</h3>
        <p class="tp__body">{c['body']}</p>
        <p class="tp__pair"><span>Teaching</span>{c['teach']} <b aria-hidden="true">&rarr;</b> <span>Product</span>{c['prod']}</p>
      </article>"""


TAUGHT = [
    ("UC Berkeley SCET", "Product Management Course Coordinator", "2026&ndash;Present",
     "Co-develop curriculum and facilitate an interdisciplinary product management course for about 60 students spanning 8+ majors. Helped reposition the course to be more approachable for students outside traditional technical backgrounds.",
     "What it taught me", "How to design for people entering with radically different context."),
    ("Berkeley ANova", "Computer Science Mentor", "Berkeley, CA",
     "Develop and teach computer science curriculum for middle and high school students from under-resourced Bay Area schools, adapting technical concepts across ages and experience levels.",
     "What it taught me", "Technical complexity is often a communication problem before it&rsquo;s a capability problem."),
    ("Software Programming Instructor", "Independent", "M&eacute;rida, Mexico",
     "Designed a Scratch curriculum for 4th&ndash;5th graders and authored a beginner-friendly Python coding book for kids.",
     "What it taught me", "Sequence matters &mdash; the order someone encounters complexity can decide whether it feels intuitive or impossible."),
    ("Froggin English for Kids", "English Teacher", "M&eacute;rida, Mexico",
     "Taught English to students ages 6&ndash;12 across proficiency levels, covering reading, writing, speaking, and listening.",
     "What it taught me", "When an explanation isn&rsquo;t working, change the explanation."),
]

teaching = head(
    "Teaching — Bella Koosh",
    "Teaching made me better at product — how years of teaching shaped the way Bella Koosh understands users and designs experiences.",
) + masthead("teaching.html") + f"""
<main id="main" data-accent="blue">

  <section class="shell brief">
    <p class="brief__kicker">
      <span class="mono mono--ink">Vol. 02</span>
      <span class="chip">Teaching</span>
    </p>
    <div class="brief__grid brief__grid--wide">
      <div class="brief__lead">
        <h1>Teaching</h1>
        <p class="brief__problem">Teaching made me better at product.</p>
        <p class="lede u-mt-sm">I started teaching long before I knew what product management was.
        Looking back, a lot of what I learned in the classroom is now how I approach building products:
        understand where someone is starting, figure out where they&rsquo;re getting stuck, and design
        the next step so it feels intuitive.</p>
      </div>
    </div>
  </section>

  <section class="shell section--snug" aria-label="Teaching, applied to product">
    <div class="tpgrid">
{chr(10).join(tp_card(c) for c in TP_PAIRS)}
    </div>
  </section>

  <section class="section--snug section--paper">
    <div class="shell">
      <div class="sechead"><h2>Where I&rsquo;ve taught</h2><p class="mono">Evidence for the story above</p></div>
      <div class="exprows">
{exprows(TAUGHT)}
      </div>
    </div>
  </section>

  <section class="shell section--snug">
    <p class="lede u-measure">I still teach because I love teaching. Education matters to me independently
    of my career &mdash; but it&rsquo;s also become one of the lenses I bring into product work. Good
    teaching and good product management both require curiosity about how another person sees the world.</p>
  </section>

  <section class="shell">
    <div class="nextup" data-accent="purple">
      <p class="mono">Next</p>
      <p class="nextup__title">About</p>
      <a class="btn" href="about.html">Open <span aria-hidden="true">&rarr;</span></a>
    </div>
  </section>

</main>
""" + FOOT

open(os.path.join(OUT, "teaching.html"), "w").write(teaching)


# ==================================================================== ABOUT

LEADERSHIP = [
    ("Berkeley ANova", "Vice President of Finance", "2025&ndash;2026",
     "Helped operate a 60-member education nonprofit expanding access to computer science across 9+ Bay Area schools. Managed $30K+ in organizational accounts, budgeting, and resource allocation, and personally conducted 22 candidate interviews across officer and member recruiting.",
     "Signal", "Operations &middot; Financial Leadership &middot; Recruiting"),
    ("Berkeley ANova", "General Meetings Officer", "Spring 2025",
     "Led a team of 5 developing educational materials for 40+ mentors and delivered weekly pedagogy-focused training, and implemented feedback and data-collection systems to track program effectiveness.",
     "Signal", "Team Leadership &middot; Curriculum &middot; Training"),
    ("Girl Up M&eacute;rida United Voices", "Founder &amp; President", "2023&ndash;2024",
     "Founded and led a UN-affiliated Girl Up chapter: 70+ girls and women engaged, 12+ events, MXN$6,000+ raised, 3 NGO partnerships. Grew the leadership team to 12+ directors and built succession structures that carried the chapter through two generations of new presidents.",
     "Signal", "Community Building &middot; Leadership &middot; Partnerships"),
]

about = head(
    "About — Bella Koosh",
    "Hi, I'm Bella — a UC Berkeley computer science student working across product, startup growth, and teaching.",
) + masthead("about.html") + f"""
<main id="main" data-accent="purple">

  <section class="shell brief">
    <p class="brief__kicker">
      <span class="mono mono--ink">Vol. 03</span>
      <span class="chip">About</span>
    </p>

    <div class="brief__grid">
      <div class="about__portrait">
        <!-- Replace with: <img src="assets/img/bella.jpg" alt="Bella Koosh"> -->
        <div class="slot slot--portrait"><p class="mono">Portrait to add</p></div>
      </div>
      <div class="brief__lead">
        <h1>Hi, I&rsquo;m Bella.</h1>
        <div class="about__copy u-mt-sm">
          <p>I&rsquo;m a Computer Science student at UC Berkeley interested in product management and
          the messy questions that happen before something gets built: who is this actually for, what
          problem matters most, and what should we do about it?</p>
          <p>I&rsquo;ve explored those questions from very different angles. At SoundExchange, I worked
          inside a product organization taking a workflow from discovery through engineering planning.
          With BearCheck, I&rsquo;m on the market-facing side of a startup &mdash; growth, outreach,
          relationships, feedback, and where we expand next. And through teaching, I&rsquo;ve spent years
          learning how to make unfamiliar ideas understandable to very different people.</p>
          <p>That last piece has shaped me more than I expected. Teaching taught me to pay attention to
          where people get confused, change my approach instead of blaming the learner, and think
          carefully about the sequence in which someone encounters information. Those instincts now
          follow me into product.</p>
          <p>I&rsquo;ve also gravitated toward leadership roles, especially when there&rsquo;s a chance to
          build a team, system, or community that can continue without me. Outside of product and
          teaching, I DJ, travel whenever I can, and take espresso disproportionately seriously.</p>
        </div>
        <p class="u-mt"><a class="btn btn--solid" href="assets/resume/bella-koosh-resume.pdf">Resume <span aria-hidden="true">&#8599;</span></a></p>
      </div>
      <div class="brief__anchor brief__anchor--plain">
        <p class="mono mono--ink hero__sidehead">Quick facts</p>
        <dl class="liner">
          <div class="liner__row"><dt>School</dt><dd>UC Berkeley &mdash; B.A. Computer Science, expected 2027</dd></div>
          <div class="liner__row"><dt>Also</dt><dd>SCET Certificate in Entrepreneurship &amp; Technology</dd></div>
          <div class="liner__row"><dt>Languages</dt><dd>English &middot; Spanish &middot; French</dd></div>
          <div class="liner__row"><dt>Interests</dt><dd>Product &middot; Education &middot; Music</dd></div>
        </dl>
        <p class="mono mono--ink hero__sidehead u-mt">Currently</p>
        <dl class="liner">
          <div class="liner__row"><dt>Studying</dt><dd>Computer Science @ Berkeley</dd></div>
          <div class="liner__row"><dt>Building</dt><dd>BearCheck</dd></div>
          <div class="liner__row"><dt>Teaching</dt><dd>Product Management @ SCET &middot; CS @ ANova</dd></div>
          <div class="liner__row"><dt>Playing</dt><dd><a href="in-rotation.html">In Rotation &rarr;</a></dd></div>
        </dl>
      </div>
    </div>
  </section>

  <section class="section--snug section--paper">
    <div class="shell">
      <div class="sechead"><h2>Things I&rsquo;ve helped lead</h2><p class="mono">Not titles &mdash; systems</p></div>
      <div class="exprows">
{exprows(LEADERSHIP)}
      </div>
      <p class="mono earlier">
        <span class="mono--ink">Earlier &mdash; </span>Madison Student Council, VP/Treasurer.
        Raised MXN$70K+ through fundraising and product sales; managed organizational finances,
        established financial procedures, and trained a successor.
      </p>
      <p class="lede u-measure u-mt">The pattern isn&rsquo;t that I accumulated titles. It&rsquo;s that I
      repeatedly found myself building systems, organizing people, raising resources, and eventually
      figuring out how the work could continue without me.</p>
    </div>
  </section>

  <section class="shell">
    <div class="nextup" data-accent="blue">
      <p class="mono">Next</p>
      <p class="nextup__title">The work</p>
      <a class="btn" href="work.html">Open <span aria-hidden="true">&rarr;</span></a>
    </div>
  </section>

</main>
""" + FOOT

open(os.path.join(OUT, "about.html"), "w").write(about)


# ==================================================================== IN ROTATION
# The Stitch "Sonic Artifact" concept: an immersive dark deck/mixer page,
# combined with a real, periodically-synced Spotify playlist (see
# scripts/sync-rotation.mjs and .github/workflows/sync-rotation.yml).
# The page reads assets/data/rotation.json at runtime — nothing here is
# hand-typed track data, and nothing plays until the visitor clicks a track.

rotation = head(
    "In Rotation — Bella Koosh",
    "What Bella Koosh is playing lately — synced from a real Spotify playlist.",
    extra_head='<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">',
) + masthead("in-rotation.html") + """
<main id="main">

  <!-- This page's data comes from assets/data/rotation.json, written by a
       scheduled GitHub Action (see .github/workflows/sync-rotation.yml and
       scripts/sync-rotation.mjs). Nothing on this page is hand-typed track
       data, and nothing autoplays — clicking a row is what loads a deck
       and, where a preview exists, starts audio. -->

  <section class="ir" aria-label="In Rotation">
    <div class="ir-parallax" aria-hidden="true"><span id="ir-parallax-text">ROTATION</span></div>

    <div class="ir-in">

      <div class="ir-head rise">
        <div class="ir-marg">
          <span class="ir-mono ir-mono--glow-blue">[PHASE: ACTIVE]</span>
          <span class="ir-mono">01</span>
        </div>
        <div>
          <h1 class="ir-title">In Rotation</h1>
          <p class="ir-sub">What I&rsquo;m playing lately.</p>
        </div>
        <div class="ir-marg ir-marg--r">
          <span class="ir-mono ir-mono--glow-orange">VOL. 004</span>
          <span class="ir-mono">BPM: SYNC</span>
        </div>
      </div>

      <div class="ir-decks rise">
        <div class="ir-deck" data-deck="A" style="--deck-accent: var(--ir-blue)">
          <div class="ir-deck__frame"></div>
          <div class="ir-deck__chan"><span>CH 1</span><span>L IN</span></div>
          <div class="ir-platter">
            <div class="ir-platter__ring">
              <img class="ir-platter__img" data-deck-art alt="" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' fill='%23151515'/%3E%3C/svg%3E">
            </div>
          </div>
          <div class="ir-track-info">
            <h2 data-deck-title>Deck A</h2>
            <p data-deck-meta>No track loaded yet</p>
          </div>
        </div>

        <div class="ir-mixer" aria-hidden="true">
          <div class="ir-eq ir-eq--hi"><span>EQ HI</span><div class="ir-eq__track"><div class="ir-eq__dot"></div></div></div>
          <div class="ir-eq ir-eq--mid"><span>EQ MID</span><div class="ir-eq__track"><div class="ir-eq__dot"></div></div></div>
          <div class="ir-eq ir-eq--low"><span>EQ LOW</span><div class="ir-eq__track"><div class="ir-eq__dot"></div></div></div>
          <div class="ir-xfade">
            <span class="ir-xfade__label">X-FADE</span>
            <div class="ir-xfade__track">
              <div class="ir-xfade__grad"></div>
              <div class="ir-xfade__thumb"></div>
            </div>
          </div>
        </div>

        <div class="ir-deck ir-deck--b" data-deck="B" style="--deck-accent: var(--ir-orange)">
          <div class="ir-deck__frame"></div>
          <div class="ir-deck__chan"><span>CH 2</span><span>R IN</span></div>
          <div class="ir-platter">
            <div class="ir-platter__ring">
              <img class="ir-platter__img" data-deck-art alt="" src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' fill='%23151515'/%3E%3C/svg%3E">
            </div>
          </div>
          <div class="ir-track-info">
            <h2 data-deck-title>Deck B</h2>
            <p data-deck-meta>No track loaded yet</p>
          </div>
        </div>
      </div>

      <div class="ir-endrule rise"><span>[END OF SET]</span></div>

      <div class="ir-list rise" data-rotation-list>
        <div class="ir-list__head">
          <h2>Tracklist</h2>
          <p class="ir-sync" data-sync-status>Loading&hellip;</p>
        </div>
        <div class="ir-filters" data-filters hidden></div>
        <div class="ir-tracks" data-tracks></div>
        <div class="ir-empty" data-empty hidden>
          <p>Not yet synced.</p>
          <p>This list is wired to a real Spotify playlist via a scheduled sync &mdash;
          see <code>README.md</code> for how it goes live.</p>
        </div>
      </div>

    </div>
  </section>

  <section class="shell">
    <div class="nextup" data-accent="blue">
      <p class="mono">Back to it</p>
      <p class="nextup__title">The work</p>
      <a class="btn" href="work.html">Open <span aria-hidden="true">&rarr;</span></a>
    </div>
  </section>

</main>
""" + FOOT.replace(
    '<script src="assets/js/site.js" defer></script>',
    '<script src="assets/js/site.js" defer></script>\n<script src="assets/js/rotation.js" defer></script>')

open(os.path.join(OUT, "in-rotation.html"), "w").write(rotation)
print("built teaching.html, about.html, in-rotation.html")
