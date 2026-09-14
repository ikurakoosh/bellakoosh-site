import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from parts import head, masthead, FOOT, shelf, RECORDS, record

OUT = os.environ.get("SITE_OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

# ------------------------------------------------------------------ HOME
home = head(
    "Bella Koosh — Product / Education / Technology",
    "Bella Koosh is a UC Berkeley computer science student working across product management, startup growth, strategy, and teaching.",
) + masthead("index.html") + f"""
<main id="main">

  <section class="shell hero">
    <p class="hero__school rise">Computer Science <span aria-hidden="true">&#183;</span> UC Berkeley</p>

    <h1 class="hero__name rise"><span>Bella</span><span>Koosh</span></h1>

      <a class="decks2" href="in-rotation.html" aria-label="In Rotation">
        <span class="disc disc--b" aria-hidden="true"><b><i></i></b></span>
        <span class="disc disc--a" aria-hidden="true"><b><i></i></b></span>
      </a>

    <p class="hero__disciplines rise">Product <i>/</i> Education <i>/</i> Technology</p>

    <div class="grid hero__grid">
      <div class="hero__statement rise">
        <p>I like figuring out what people actually need, then making it easier to build.</p>
        <div class="hero__cta">
          <a class="btn btn--solid" href="work.html">View my work <span aria-hidden="true">&rarr;</span></a>
          <a class="btn" href="assets/resume/bella-koosh-resume.pdf">Resume <span aria-hidden="true">&#8599;</span></a>
        </div>
      </div>

      <aside class="hero__side rise" aria-label="Current status">
        <p class="mono mono--ink hero__sidehead">Currently</p>
        <dl class="liner">
          <div class="liner__row"><dt>Studying</dt><dd>Computer Science &mdash; UC Berkeley</dd></div>
          <div class="liner__row"><dt>Building</dt><dd>BearCheck &mdash; Co-Founder, Sales &amp; Growth</dd></div>
          <div class="liner__row"><dt>Teaching</dt><dd>Product Management &mdash; SCET</dd></div>
          <div class="liner__row"><dt>Playing</dt><dd><a href="in-rotation.html">In Rotation &rarr;</a></dd></div>
        </dl>
      </aside>
    </div>
  </section>

  <section class="shell section--snug" aria-labelledby="collection-h">
    <div class="sechead">
      <h2 id="collection-h">The Collection</h2>
      <p class="mono">Vol. 01 <span aria-hidden="true">&middot;</span> Four records <span aria-hidden="true">&middot;</span> <a href="work.html">Index view &rarr;</a></p>
    </div>
{shelf()}
  </section>

  <section class="section section--ink">
    <div class="shell">
      <div class="grid">
        <div class="closing rise">
          <p class="mono">Also</p>
          <h2 class="closing__h">I care whether the thing works &mdash; and whether anyone can actually use it.</h2>
          <div class="hero__cta">
            <a class="btn" href="teaching.html">Teaching <span aria-hidden="true">&rarr;</span></a>
            <a class="btn" href="about.html">About <span aria-hidden="true">&rarr;</span></a>
            <a class="btn" href="in-rotation.html">In Rotation <span aria-hidden="true">&rarr;</span></a>
          </div>
        </div>
      </div>
    </div>
  </section>

</main>
""" + FOOT

open(os.path.join(OUT, "index.html"), "w").write(home)

# ------------------------------------------------------------------ WORK
work = head(
    "Work — Bella Koosh",
    "Four records: SoundExchange (product management), BearCheck (sales and growth), LIPOR (strategy), Chillzu (early product).",
) + masthead("work.html") + f"""
<main id="main">

  <section class="shell hero hero--page">
    <p class="mono rise">Vol. 01 &middot; The record collection</p>
    <h1 class="hero__name hero__name--page rise"><span>Work</span></h1>
    <div class="grid hero__grid">
      <div class="hero__statement rise">
        <p>Four releases, in the order they explain each other: <em>a product definition, a market, a system, and the thing built first.</em></p>
      </div>
      <aside class="hero__side rise" aria-label="How to read the collection">
        <p class="mono mono--ink hero__sidehead">How to read this</p>
        <dl class="liner">
          <div class="liner__row"><dt>01</dt><dd>SoundExchange &mdash; product management</dd></div>
          <div class="liner__row"><dt>02</dt><dd>BearCheck &mdash; growth &amp; GTM</dd></div>
          <div class="liner__row"><dt>03</dt><dd>LIPOR / CREW &mdash; strategy</dd></div>
          <div class="liner__row"><dt>04</dt><dd>Chillzu &mdash; early product</dd></div>
        </dl>
      </aside>
    </div>
  </section>

  <section class="shell section--snug" aria-label="The collection">
{shelf()}
  </section>

  <section class="section--snug section--paper">
    <div class="shell">
      <div class="sechead"><h2>Also on the shelf</h2><p class="mono">Adjacent volumes</p></div>
      <div class="nextup">
        <p class="nextup__title">Teaching</p>
        <p class="u-measure-sm">Course coordination at Berkeley and computing instruction with ANova. Kept separate from the work collection on purpose.</p>
        <a class="btn" href="teaching.html">Open teaching <span aria-hidden="true">&rarr;</span></a>
      </div>
    </div>
  </section>

</main>
""" + FOOT

open(os.path.join(OUT, "work.html"), "w").write(work)
print("built index.html, work.html")
