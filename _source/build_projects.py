import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from project import project, NEED
from parts import COVER_SX, COVER_BC, COVER_LP, COVER_CZ

OUT = os.environ.get("SITE_OUT", os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

PAGES = [

    # ================================================================ SOUNDEXCHANGE
    dict(
        file="soundexchange.html", accent="blue", index="01",
        name="SoundExchange", discipline="Product Management",
        dates="Washington, D.C. &middot; Summer 2026",
        cover=COVER_SX,
        title_tag="SoundExchange — Product Management Intern — Bella Koosh",
        desc="Product management at SoundExchange: turning a fragmented internal onboarding workflow into one streamlined product experience.",
        problem="SoundExchange&rsquo;s licensee-management experience was fragmented across systems. Inviting a single user took 3&ndash;5 minutes of manual file handling and CRM backfilling.",
        figure="75%+",
        anchor_label="Targeted reduction in administrative effort",
        anchor_note="6 steps &rarr; 1 flow. A target from the defined solution, not a measured production result.",
        specs=[
            ("Product", "SoundExchange&rsquo;s internal licensee-management platform, spanning multiple systems that support royalty submissions."),
            ("My role", "Product Management Intern. Discovery through engineering handoff."),
            ("The problem", "Administrative workflows were fragmented across systems and required significant manual work &mdash; user invitation most of all."),
            ("What I did", "Ran discovery with Operations and stakeholders, then defined and scoped an in-product invitation flow engineering could build."),
        ],
        skills=["Product Discovery", "User Research", "Workflow Analysis", "Prioritization",
                "PRD Writing", "Prototyping", "Jira", "Gherkin Acceptance Criteria",
                "Engineering Collaboration", "Stakeholder Management"],
        evidence_title="From discovery to delivery",
        slots=["Discovery &mdash; mapping the existing workflow made the manual work visible",
               "PRD &mdash; prioritized requirements, phased scope, measurable success criteria"],
        moments_title="How it moved",
        moments_kicker="Discover &middot; Define &middot; Design &middot; Deliver",
        moments=[
            ("Discover.", "Interviewed stakeholders and studied existing workflows to see where friction and manual effort were accumulating."),
            ("Define.", "Synthesized findings and prioritized opportunities on user pain, business impact, feasibility, and roadmap fit."),
            ("Design.", "Defined an in-product invitation experience and rapidly prototyped concepts to validate the direction."),
            ("Deliver.", "Translated the solution into a PRD, Jira stories, and Gherkin acceptance criteria as the work moved into sprint planning."),
        ],
        aside="Research also surfaced a permissions problem creating an estimated 3&ndash;5 support calls a week &mdash; targeted for a 50%+ reduction, kept secondary to the invitation story here.",
        next_accent="orange", next_name="BearCheck", next_href="bearcheck.html",
    ),

    # ================================================================ BEARCHECK
    dict(
        file="bearcheck.html", accent="orange", index="02",
        name="BearCheck", discipline="Co-Founder &middot; Sales &amp; Growth",
        dates="Berkeley, CA &middot; 2026&ndash;Present",
        cover=COVER_BC,
        title_tag="BearCheck — Co-Founder, Sales & Growth — Bella Koosh",
        desc="Founder-led growth at BearCheck: finding who needs it, how to reach them, and where the company goes next.",
        problem="BearCheck is a classroom presence platform, live across UC Berkeley lecture halls with hundreds of registered users. The open question was never the product &mdash; it was who actually needs it and how to reach them.",
        phrase="Hundreds of users.<br>One relationship<br>at a time.",
        anchor_label="Live across UC Berkeley lecture halls",
        specs=[
            ("What it is", "A classroom presence platform &mdash; attendance that&rsquo;s faster for students and more reliable for instructors."),
            ("My role", "Co-founder, sales &amp; growth. The market-facing side of the company, not product or engineering."),
            ("The problem", "Which instructors actually need this, what makes them switch, and what stops them."),
            ("What I did", "Own outreach, positioning, instructor relationships, and the feedback loop that shapes where we go next."),
        ],
        skills=["Go-to-Market Strategy", "Growth", "Customer Relationships", "Positioning &amp; Messaging",
                "Sales &amp; Outreach", "Market Research", "Market Expansion", "Founder Decision-Making"],
        evidence_title="What I work on",
        slots=["Outreach &mdash; how BearCheck gets in front of an instructor",
               "Adoption &mdash; a lecture hall using BearCheck"],
        moments_title="From conversations to direction",
        moments_kicker="Five threads",
        moments=[
            ("Go-to-market.", "Deciding who we target, how we position BearCheck, and how we reach them."),
            ("Relationships.", "Building and maintaining relationships with the instructors using and evaluating the platform."),
            ("Feedback.", "Bringing conversations, objections, and usage back into company decisions."),
            ("Expansion.", "Helping decide which universities and markets we explore next."),
        ],
        aside="Talking directly with instructors is the real feedback loop &mdash; it surfaces why someone would switch, what would stop them, and where BearCheck might make sense beyond our first market.",
        next_accent="purple", next_name="LIPOR / CREW", next_href="lipor.html",
    ),

    # ================================================================ LIPOR / CREW
    dict(
        file="lipor.html", accent="purple", index="03",
        name="LIPOR / CREW", discipline="Strategy &middot; Consulting",
        dates="Porto, Portugal &middot; Summer 2025",
        cover=COVER_LP,
        title_tag="LIPOR / CREW — Consultant — Bella Koosh",
        desc="Strategy and consulting for CREW, LIPOR's e-waste initiative in Portugal: a behavior-change strategy and an AI-assisted product concept.",
        problem="CREW, LIPOR&rsquo;s e-waste initiative, wasn&rsquo;t only an environmental problem. Knowing electronics shouldn&rsquo;t become waste doesn&rsquo;t tell someone what to do with the broken phone sitting at home.",
        phrase="Awareness isn&rsquo;t<br>the same as<br>a next step.",
        anchor_label="Recommendations presented to LIPOR leadership",
        specs=[
            ("Client", "LIPOR / CREW &mdash; municipal e-waste initiative, Porto, Portugal."),
            ("My role", "Consultant. Strategy through client-facing recommendations."),
            ("The problem", "A behavior problem hiding inside an environmental one: awareness without a clear next action."),
            ("What I did", "Designed a citizen-engagement strategy and built an AI chatbot prototype connecting people to local repair resources."),
        ],
        skills=["Product Strategy", "Behavioral Thinking", "Customer Journeys",
                "AI Prototyping", "Consulting", "Client Communication"],
        evidence_title="The product idea",
        slots=["What do you have? &mdash; the chatbot&rsquo;s starting question",
               "Where does it go? &mdash; routing to repair, reuse, or donation"],
        moments_title="Behavior, then technology",
        moments_kicker="Three steps",
        moments=[
            ("Start with the object, not the system.", "Instead of explaining the whole e-waste ecosystem, ask what someone has and what they&rsquo;re trying to do with it."),
            ("Route, don&rsquo;t educate.", "Guide people directly to the most relevant repair, reuse, or donation pathway."),
            ("Recommend, don&rsquo;t assume.", "Presented the engagement framework and AI-assisted concept to LIPOR leadership for volunteer mobilization and donation quality."),
        ],
        next_accent="ink", next_name="Chillzu", next_href="chillzu.html",
    ),

    # ================================================================ CHILLZU
    dict(
        file="chillzu.html", accent="ink", index="04",
        name="Chillzu", discipline="Early Product &middot; Wellness",
        dates=f"Year {NEED}",
        cover=COVER_CZ,
        title_tag="Chillzu — Founder — Bella Koosh",
        desc="An early self-directed project: a wellness app for teenagers, researched, designed, and coded in React as a teenager.",
        problem="Chillzu began as a wellness product for teenagers &mdash; before I had any vocabulary for &ldquo;product management.&rdquo;",
        phrase="Building the product<br>is only half<br>the job.",
        anchor_label="Where the product instinct started",
        specs=[
            ("What it was", "A wellness app for teenagers, built end to end &mdash; research, design, code, and testing."),
            ("My role", "Founder. Product, design, and development, all at once."),
            ("The idea", "Researched existing wellness products, designed the experience, and built an early version in React/JavaScript."),
            ("What changed", "Talking to users showed the gap between what makes sense to design and what actually makes sense to use."),
        ],
        skills=["Product Development", "UX Research", "Prototyping",
                "React / JavaScript", "Usability Testing", "Iteration"],
        evidence_title="The loop",
        slots=["Research &rarr; Design &mdash; studying existing products before designing the experience",
               "Build &rarr; Test &mdash; a working prototype, put in front of real users"],
        moments_title="Why it&rsquo;s still here",
        moments_kicker="Two notes",
        moments=[
            ("The code wasn&rsquo;t the important part.", "User feedback changed how I thought about features, usability, and what to build next."),
            ("The whole loop, once.", "Research &rarr; design &rarr; build &rarr; test &rarr; learn &rarr; iterate &mdash; the experience that pushed me toward product management."),
        ],
        next_accent="blue", next_name="Teaching", next_href="teaching.html",
    ),
]

for p in PAGES:
    open(os.path.join(OUT, p["file"]), "w").write(project(p))
print("built", ", ".join(p["file"] for p in PAGES))
