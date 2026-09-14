import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from parts import head, masthead, FOOT

NEED = '<span class="todo">Add</span>'


def _chips(items, ink=False):
    cls = "chip chip--ink" if ink else "chip"
    return "\n".join(f'        <li><span class="{cls}">{i}</span></li>' for i in items)


def _specs(cells):
    out = []
    for label, value in cells:
        out.append(f"""      <div class="spec">
        <span class="mono">{label}</span>
        <p>{value}</p>
      </div>""")
    return "\n".join(out)


def _slots(slots):
    out = []
    for caption in slots:
        out.append(f"""      <figure class="ev">
        <div class="slot"><p class="mono">Artifact to add</p></div>
        <figcaption class="mono">{caption}</figcaption>
      </figure>""")
    return "\n".join(out)


def _moments(rows):
    out = []
    for i, (head_, body) in enumerate(rows, 1):
        out.append(f"""      <div class="moment">
        <span class="mono mono--accent">{i:02d}</span>
        <p><b>{head_}</b> {body}</p>
      </div>""")
    return "\n".join(out)


def project(p):
    """One compressed project page. Everything a recruiter needs sits above the fold."""

    if p.get("figure"):
        anchor = f"""        <p class="anchor__fig">{p['figure']}</p>
        <p class="anchor__label">{p['anchor_label']}</p>"""
    else:
        anchor = f"""        <p class="anchor__phrase">{p['phrase']}</p>
        <p class="anchor__label">{p['anchor_label']}</p>"""

    foot_note = f'<p class="anchor__note">{p["anchor_note"]}</p>' if p.get("anchor_note") else ""

    return head(p["title_tag"], p["desc"]) + masthead("work.html") + f"""
<main id="main" data-accent="{p['accent']}">

  <!-- ===== THE BRIEF — first screen ===== -->
  <section class="shell brief">
    <p class="brief__kicker">
      <span class="mono mono--ink">{p['index']} / Record</span>
      <span class="chip{' chip--ink' if p['accent'] == 'ink' else ''}">{p['discipline']}</span>
      <span class="mono">{p['dates']}</span>
    </p>

    <div class="brief__grid">
      <div class="brief__art">{p['cover']}</div>

      <div class="brief__lead">
        <h1>{p['name']}</h1>
        <p class="brief__problem">{p['problem']}</p>
      </div>

      <div class="brief__anchor">
{anchor}
{foot_note}
      </div>
    </div>

    <div class="specs">
{_specs(p['specs'])}
    </div>

    <ul class="tags brief__skills">
{_chips(p['skills'], ink=(p['accent'] == 'ink'))}
    </ul>
  </section>

  <!-- ===== EVIDENCE ===== -->
  <section class="shell section--snug">
    <div class="sechead"><h2>{p['evidence_title']}</h2><p class="mono">Evidence</p></div>
    <div class="evgrid">
{_slots(p['slots'])}
    </div>
  </section>

  <!-- ===== WHAT MATTERED ===== -->
  <section class="section--snug section--paper">
    <div class="shell">
      <div class="sechead"><h2>{p['moments_title']}</h2><p class="mono">{p['moments_kicker']}</p></div>
      <div class="moments">
{_moments(p['moments'])}
      </div>
      {f'<p class="aside">{p["aside"]}</p>' if p.get('aside') else ''}
    </div>
  </section>

  <!-- ===== NEXT ===== -->
  <section class="shell">
    <div class="nextup" data-accent="{p['next_accent']}">
      <p class="mono">Next record</p>
      <p class="nextup__title">{p['next_name']}</p>
      <a class="btn" href="{p['next_href']}">Open <span aria-hidden="true">&rarr;</span></a>
    </div>
  </section>

</main>
""" + FOOT
