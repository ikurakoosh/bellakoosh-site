# Shared markup generator for bellakoosh.com
# Emits plain static HTML — no runtime templating on the live site.

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..900;1,400..900'
         '&family=Source+Serif+4:ital,opsz,wght@0,8..60,300..600;1,8..60,300..600'
         '&family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">')

NAV_ITEMS = [
    ("work.html", "Work"),
    ("teaching.html", "Teaching"),
    ("about.html", "About"),
    ("assets/resume/bella-koosh-resume.pdf", "Resume ↗"),
    ("in-rotation.html", "In Rotation"),
]


def head(title, desc, current=None, extra_head=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' fill='%23FDFCF8'/><circle cx='16' cy='16' r='14.5' fill='%23000'/><circle cx='16' cy='16' r='11' fill='none' stroke='%23303030' stroke-width='1'/><circle cx='16' cy='16' r='8.5' fill='none' stroke='%23303030' stroke-width='1'/><circle cx='16' cy='16' r='5' fill='%230055FF'/><circle cx='16' cy='16' r='1.3' fill='%23FDFCF8'/></svg>">
{FONTS}
{extra_head}
<link rel="stylesheet" href="assets/css/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="needle" aria-hidden="true"></div>
"""


def masthead(current=None):
    links = []
    for href, label in NAV_ITEMS:
        cls = ' class="nav__resume"' if "resume" in href else ""
        cur = ' aria-current="page"' if href == current else ""
        links.append(f'      <a{cls} href="{href}"{cur}>{label}</a>')
    return ("""<header class="masthead">
  <div class="shell masthead__in">
    <a class="wordmark" href="index.html">Bella Koosh</a>
    <button class="navtoggle" aria-expanded="false" aria-controls="primary-nav"><span data-label>Menu</span></button>
    <nav class="nav" id="primary-nav" aria-label="Primary">
"""
            + "\n".join(links)
            + """
    </nav>
  </div>
</header>
""")


FOOT = """<footer class="colophon">
  <div class="shell colophon__in">
    <p class="colophon__ask">Want to talk product, education, or music?</p>
    <nav class="colophon__links mono" aria-label="Footer">
      <a href="mailto:isabellakoosh@berkeley.edu">isabellakoosh@berkeley.edu</a>
      <a href="#" class="todo">LinkedIn &#8599;</a>
      <a href="assets/resume/bella-koosh-resume.pdf">Resume &#8599;</a>
      <span class="colophon__loc">Berkeley, CA</span>
    </nav>
  </div>
</footer>

<script src="assets/js/site.js" defer></script>
</body>
</html>
"""

# ---------------------------------------------------------------- covers

def _sx_lanes():
    lanes = []
    for i in range(7):
        y = 78 + i * 26
        op = 0.45 + i * 0.09
        nodes = "".join(
            f'<rect x="{40 + n * 62}" y="{y - 3.5}" width="7" height="7" '
            f'fill="{"#0055ff" if n == 0 else "none"}" stroke="#0055ff"/>'
            for n in range(5)
        )
        lanes.append(
            f'<g opacity="{op:.2f}"><line x1="43.5" y1="{y}" x2="286.5" y2="{y}" '
            f'stroke="#0055ff" stroke-width="1"/>{nodes}</g>'
        )
    return "".join(lanes)


COVER_SX = f"""<svg viewBox="0 0 400 400" role="img" aria-label="Cover art: a repeated manual invitation sequence, three to five minutes each">
  <rect width="400" height="400" fill="#f2efe6"/>
  <text x="40" y="48" font-family="Space Mono, monospace" font-size="13" letter-spacing="2.1" fill="#7e7876">MANUAL INVITATION SEQUENCE</text>
  <line x1="40" y1="58" x2="360" y2="58" stroke="#000" stroke-width="1"/>
  {_sx_lanes()}
  <text x="322" y="160" font-family="Space Mono, monospace" font-size="12.5" letter-spacing="2" fill="#7e7876" transform="rotate(90 322 160)">REPEATED</text>
  <line x1="40" y1="276" x2="360" y2="276" stroke="#000" stroke-width="1"/>
  <text x="38" y="356" font-family="Playfair Display, serif" font-weight="900" font-size="102" letter-spacing="-4" fill="#000">3&#8211;5</text>
  <text x="230" y="326" font-family="Space Mono, monospace" font-size="13" letter-spacing="2.1" fill="#0055ff">MINUTES</text>
  <text x="230" y="348" font-family="Space Mono, monospace" font-size="13" letter-spacing="2.1" fill="#0055ff">PER INVITE</text>
</svg>"""

def _bc_lines():
    """Many outreach threads converging on a handful of real relationships —
    the visual argument for GTM/relationships rather than a feature diagram."""
    out = []
    sources = [(30, 60), (30, 108), (30, 156), (30, 204), (30, 252), (30, 300)]
    targets = [(250, 120), (250, 200), (250, 280)]
    for i, s in enumerate(sources):
        t = targets[i % 3]
        op = 0.30 + (i % 3) * 0.18
        out.append(f'<path d="M{s[0]} {s[1]} C140 {s[1]} 160 {t[1]} {t[0]} {t[1]}" '
                    f'fill="none" stroke="#ff5500" stroke-width="1.1" opacity="{op:.2f}"/>')
        out.append(f'<circle cx="{s[0]}" cy="{s[1]}" r="2.6" fill="#ff5500" opacity="0.6"/>')
    for t in targets:
        out.append(f'<circle cx="{t[0]}" cy="{t[1]}" r="7" fill="#ff5500"/>')
        out.append(f'<circle cx="{t[0]}" cy="{t[1]}" r="13" fill="none" stroke="#ff5500" stroke-width="1" opacity="0.4"/>')
    return "".join(out)


COVER_BC = f"""<svg viewBox="0 0 400 400" role="img" aria-label="Cover art: many outreach conversations converging into a handful of real relationships">
  <rect width="400" height="400" fill="#f2efe6"/>
  <text x="28" y="36" font-family="Space Mono, monospace" font-size="13" letter-spacing="2.1" fill="#7e7876">OUTREACH &#8594; RELATIONSHIP</text>
  <line x1="28" y1="48" x2="372" y2="48" stroke="#000" stroke-width="1"/>
  {_bc_lines()}
  <line x1="28" y1="336" x2="372" y2="336" stroke="#000" stroke-width="1"/>
  <text x="28" y="360" font-family="Space Mono, monospace" font-size="13" letter-spacing="2.1" fill="#ff5500">UC BERKELEY LECTURE HALLS</text>
</svg>"""


def _lipor_paths():
    out = []
    for i in range(9):
        y = 92 + i * 24
        out.append(f'<path d="M150 {y} C240 {y} 250 200 318 200" fill="none" stroke="#8800ff" stroke-width="1.1" opacity="0.75"/>')
        out.append(f'<line x1="42" y1="{y}" x2="150" y2="{y}" stroke="#8800ff" stroke-width="1.1" opacity="0.35"/>')
        out.append(f'<circle cx="42" cy="{y}" r="2.4" fill="#8800ff"/>')
    return "".join(out)


COVER_LP = f"""<svg viewBox="0 0 400 400" role="img" aria-label="Cover art: many citizen entry points narrowing to a single reuse outcome">
  <rect width="400" height="400" fill="#f2efe6"/>
  <text x="30" y="42" font-family="Space Mono, monospace" font-size="13" letter-spacing="2.1" fill="#7e7876">CITIZEN ENTRY POINTS</text>
  <line x1="30" y1="54" x2="370" y2="54" stroke="#000" stroke-width="1"/>
  {_lipor_paths()}
  <rect x="318" y="188" width="24" height="24" fill="#8800ff"/>
  <text x="370" y="168" text-anchor="end" font-family="Space Mono, monospace" font-size="13" letter-spacing="2.1" fill="#8800ff">REUSE</text>
  <line x1="30" y1="336" x2="370" y2="336" stroke="#000" stroke-width="1"/>
  <text x="30" y="360" font-family="Space Mono, monospace" font-size="13" letter-spacing="2.1" fill="#000">E&#8209;WASTE &#183; PORTUGAL &#183; BEHAVIOUR</text>
</svg>"""

COVER_CZ = """<svg viewBox="0 0 400 400" role="img" aria-label="Cover art: an archive sleeve for an early self-directed project">
  <defs>
    <pattern id="cznoise" width="6" height="6" patternUnits="userSpaceOnUse">
      <circle cx="1.5" cy="1.5" r="0.6" fill="#000" opacity="0.16"/>
    </pattern>
  </defs>
  <rect width="400" height="400" fill="#e7e3d7"/>
  <rect width="400" height="400" fill="url(#cznoise)"/>
  <g fill="none" stroke="#000" stroke-width="1">
    <circle cx="200" cy="204" r="26" opacity="0.85"/>
    <circle cx="200" cy="204" r="52" opacity="0.68"/>
    <circle cx="200" cy="204" r="78" opacity="0.52"/>
    <circle cx="200" cy="204" r="104" opacity="0.36"/>
    <circle cx="200" cy="204" r="130" opacity="0.22"/>
  </g>
  <g fill="none" stroke="#ff5500" stroke-width="1" opacity="0.30" transform="translate(4,-3)">
    <circle cx="200" cy="204" r="26"/><circle cx="200" cy="204" r="52"/><circle cx="200" cy="204" r="78"/>
  </g>
  <circle cx="200" cy="204" r="8" fill="#000"/>
  <text x="26" y="36" font-family="Space Mono, monospace" font-size="13" letter-spacing="2.1" fill="#000">ARCHIVE / EARLY RELEASE</text>
  <line x1="26" y1="50" x2="374" y2="50" stroke="#000" stroke-width="1"/>
  <text x="26" y="374" font-family="Space Mono, monospace" font-size="13" letter-spacing="2.1" fill="#000">BUILT BEFORE THE VOCABULARY</text>
</svg>"""

# ---------------------------------------------------------------- records

RECORDS = [
    dict(
        n="01", slug="soundexchange", cat="BK-01", accent="blue",
        title="SoundExchange", spine="SoundExchange", chip="Product Management",
        role="Product Management Intern",
        did="Led discovery on a fragmented internal workflow and defined the fix engineering could build.",
        evidence="PRD, Jira stories, Gherkin acceptance criteria.",
        scan='Turning a fragmented internal onboarding workflow into one streamlined product experience. <strong>6 steps &rarr; 1 flow &middot; 75%+ targeted reduction in administrative effort.</strong>',
        cover=COVER_SX,
    ),
    dict(
        n="02", slug="bearcheck", cat="BK-02", accent="orange",
        title="BearCheck", spine="BearCheck", chip="Sales &amp; Growth",
        role="Co-Founder &middot; Sales &amp; Growth",
        did="Finding who needs BearCheck, how to reach them, and where the company goes next.",
        evidence="Live across UC Berkeley lecture halls.",
        scan="Growing a classroom attendance startup by figuring out who needs it, how to reach them, and where we go next.",
        cover=COVER_BC,
    ),
    dict(
        n="03", slug="lipor", cat="BK-03", accent="purple",
        title="LIPOR / CREW", spine="LIPOR / CREW", chip="Strategy",
        role="Consultant",
        did="Designed a citizen-engagement strategy and an AI-assisted concept for e-waste reuse and donation.",
        evidence="Recommendations presented to LIPOR leadership.",
        scan="Designed a behavior-change strategy and AI-assisted product concept around e-waste repair, reuse, and donation.",
        cover=COVER_LP,
    ),
    dict(
        n="04", slug="chillzu", cat="BK-04", accent="ink",
        title="Chillzu", spine="Chillzu", chip="Early Product",
        role="Founder",
        did="Researched, designed, and coded a wellness app for teenagers, then rebuilt it around what users actually needed.",
        evidence="React/JavaScript prototype, tested with real users.",
        scan="The project where I first learned that building the product is only half the job.",
        cover=COVER_CZ,
    ),
]


def record(r):
    chip_cls = "chip chip--ink" if r["accent"] == "ink" else "chip"
    return f"""      <article class="record rise" data-accent="{r['accent']}">
        <a class="sleeve" href="{r['slug']}.html" aria-labelledby="rec-{r['slug']}">
          <span class="sleeve__disc"></span>
          <span class="sleeve__body">
            <span class="sleeve__spine"><b>{r['n']}</b><span>{r['spine']}</span></span>
            <span class="sleeve__face">
              <span class="sleeve__art">
                {r['cover']}
                <span class="sleeve__reveal">
                  <span class="sleeve__revealgrid">
                    <b>Role</b><i>{r['role']}</i>
                    <b>What Bella did</b><i>{r['did']}</i>
                    <b>Evidence</b><i>{r['evidence']}</i>
                  </span>
                  <span class="sleeve__open">Open record <span aria-hidden="true">&rarr;</span></span>
                </span>
              </span>
              <span class="sleeve__meta">
                <span class="{chip_cls}">{r['chip']}</span>
                <span class="mono mono--sm">{r['cat']}</span>
              </span>
              <span class="sleeve__title" id="rec-{r['slug']}">{r['title']}</span>
            </span>
          </span>
        </a>
        <span class="record__scan">
          <span class="record__role">{r['role']}</span>
          <span class="record__evidence">{r['scan']}</span>
        </span>
      </article>"""


def shelf():
    return '    <div class="shelf">\n' + "\n\n".join(record(r) for r in RECORDS) + "\n    </div>"
