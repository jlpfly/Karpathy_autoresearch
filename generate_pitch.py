"""Generate the Pasquinelli Lab Autoresearch Pitch PowerPoint deck."""
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

DARK_BG = RGBColor(0x1B, 0x1B, 0x2F)
ACCENT_BLUE = RGBColor(0x4E, 0xA8, 0xDE)
ACCENT_GREEN = RGBColor(0x2E, 0xCC, 0x71)
ACCENT_ORANGE = RGBColor(0xE6, 0x7E, 0x22)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GRAY = RGBColor(0xCC, 0xCC, 0xCC)
MEDIUM_GRAY = RGBColor(0x88, 0x88, 0x99)


def set_slide_bg(slide, color):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_text_box(slide, left, top, width, height, text,
                 font_size=18, color=WHITE, bold=False, alignment=PP_ALIGN.LEFT):
    txBox = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.alignment = alignment
    return tf


def add_p(tf, text, font_size=18, color=WHITE, bold=False):
    p = tf.add_paragraph()
    p.text = text
    p.font.size = Pt(font_size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.space_before = Pt(4)
    return p


# ---------- SLIDE 1: Title ----------
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, DARK_BG)
add_text_box(slide, 1.5, 1.0, 10, 1.5,
    "Autoresearch for the Pasquinelli Lab",
    font_size=40, color=ACCENT_BLUE, bold=True, alignment=PP_ALIGN.CENTER)
add_text_box(slide, 1.5, 2.8, 10, 1.0,
    "5 Impactful Applications of AI-Driven Autonomous Research",
    font_size=24, color=WHITE, alignment=PP_ALIGN.CENTER)
tf = add_text_box(slide, 1.5, 4.2, 10, 2.5,
    "Built on Karpathy\u2019s autoresearch framework",
    font_size=16, color=MEDIUM_GRAY, alignment=PP_ALIGN.CENTER)
add_p(tf, "Adapted for miRNA biology, aging, stress recovery, and RNA processing",
      font_size=16, color=MEDIUM_GRAY)
add_p(tf, "", font_size=12, color=MEDIUM_GRAY)
add_p(tf, "github.com/karpathy/autoresearch  |  Runs on Dell XPS 15 (RTX 3050 Ti)",
      font_size=14, color=MEDIUM_GRAY)

# ---------- SLIDE 2: Why Autoresearch? ----------
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, DARK_BG)
add_text_box(slide, 0.8, 0.5, 11, 0.8,
    "Why Autoresearch for Biology?", font_size=32, color=ACCENT_BLUE, bold=True)

tf = add_text_box(slide, 0.8, 1.8, 5.5, 4.5,
    "The Challenge", font_size=22, color=ACCENT_ORANGE, bold=True)
for item in [
    "\u2022 Literature grows faster than anyone can read",
    "\u2022 Target prediction databases disagree",
    "\u2022 Public datasets sit un-reanalyzed in GEO",
    "\u2022 Cross-study comparisons are tedious and slow",
    "\u2022 Recovery dynamics need time-series analysis"
]:
    add_p(tf, item, font_size=16, color=WHITE)

tf = add_text_box(slide, 7.0, 1.8, 5.5, 4.5,
    "What Autoresearch Offers", font_size=22, color=ACCENT_GREEN, bold=True)
for item in [
    "\u2022 Runs overnight without supervision",
    "\u2022 Iterates on parameters automatically",
    "\u2022 Processes entire datasets systematically",
    "\u2022 Produces structured, reproducible outputs",
    "\u2022 Costs nothing beyond existing hardware"
]:
    add_p(tf, item, font_size=16, color=WHITE)

add_text_box(slide, 0.8, 6.2, 11.5, 0.8,
    "PaperQA2 beats PhD researchers at lit search  \u2022  AI Scientist v2 passed peer review  "
    "\u2022  Autoresearch adopted worldwide in weeks",
    font_size=13, color=MEDIUM_GRAY, alignment=PP_ALIGN.CENTER)

# ---------- APP SLIDE TEMPLATE ----------
apps = [
    {
        "num": "01",
        "title": "Age-Dependent Isoform Shift Quantification",
        "does": "Reanalyzes 2024 direct RNA-seq aging data to build an age-stratified "
                "isoform usage matrix. Flags genes where isoform switching correlates "
                "with age more strongly than overall expression change.",
        "why": "Expression-level analyses miss isoform-level biology. Autoresearch "
               "iterates over parameter choices (age bins, thresholds) overnight.",
        "outputs": [
            "Ranked switching gene list",
            "Age-group heatmaps",
            "GO enrichment results",
            "Experiment iteration log"
        ],
        "anchor": "2024 NAR aging direct RNA-seq (PMC11662692)",
        "collabs": "Kin Fai Au (Yale) \u2022 Christopher Vollmers (UCSC) \u2022 Miten Jain (Northeastern)",
        "howto": "amy_autoresearch_howto/01_isoform_shift_quantification.md"
    },
    {
        "num": "02",
        "title": "Cross-Dataset miRNA Target Concordance Scoring",
        "does": "Integrates predictions from TargetScan, miRDB, and CLIP/CLASH datasets. "
                "Cross-references against the lab\u2019s functional data to build a "
                "concordance score per target.",
        "why": "Target prediction databases disagree frequently. Scoring targets against "
               "the lab\u2019s own data produces a curated, lab-specific target list.",
        "outputs": [
            "Concordance-scored target table",
            "Database overlap Venn diagrams",
            "Top 20 targets per miRNA",
            "Novel target shortlist"
        ],
        "anchor": "2023 miR-238/239ab paper (PLoS Genetics)",
        "collabs": "David Bartel (MIT) \u2022 Markus Hafner (NIH) \u2022 Chi-Wing Chow (Albert Einstein)",
        "howto": "amy_autoresearch_howto/02_mirna_target_concordance.md"
    },
    {
        "num": "03",
        "title": "Poly(A)-Tail Length & Translation Efficiency Integration",
        "does": "Correlates poly(A)-tail length with translational output across all "
                "transcripts. Identifies outliers where the expected relationship breaks down.",
        "why": "Outlier transcripts \u2014 short tails but high translation, or long tails "
               "but repressed \u2014 are often the most interesting biology.",
        "outputs": [
            "Tail length vs. TE scatter plots",
            "Outlier transcript lists",
            "GO enrichment per outlier class",
            "PABP binding overlap"
        ],
        "anchor": "2022 NAR PABP paper (PMC9071453)",
        "collabs": "Joel Richter (UMass) \u2022 Wendy Gilbert (Yale) \u2022 Marvin Wickens (U. Wisconsin)",
        "howto": "amy_autoresearch_howto/03_polya_translation_integration.md"
    },
    {
        "num": "04",
        "title": "Stress-Recovery Time-Series Gene Module Detection",
        "does": "Clusters genes into co-regulated modules based on heat-shock recovery "
                "dynamics. Maps known miRNA targets onto modules to identify which miRNAs "
                "control which recovery programs.",
        "why": "Recovery dynamics are harder to analyze than stress/control comparisons. "
               "Automated clustering + miRNA overlay does weeks of work overnight.",
        "outputs": [
            "Temporal profile plots per module",
            "miRNA-module enrichment scores",
            "Network visualizations",
            "miR-85 target analysis"
        ],
        "anchor": "2021 PLoS Genetics heat-shock recovery (PMC8370650)",
        "collabs": "Morimoto lab (Northwestern) \u2022 Jessica Tyler (Weill Cornell)",
        "howto": "amy_autoresearch_howto/04_stress_recovery_modules.md"
    },
    {
        "num": "05",
        "title": "Automated Cross-Dataset Replication of Aging Signatures",
        "does": "Downloads public C. elegans aging RNA-seq datasets from GEO. Scores each "
                "using lab-derived gene signatures. Iterates overnight to check replication.",
        "why": "Cross-dataset replication is the strongest evidence in genomics. Automated "
               "validation that would take months can run unattended overnight.",
        "outputs": [
            "Replication score table",
            "Forest plots",
            "Gene-level replication heatmap",
            "Core aging marker gene set"
        ],
        "anchor": "2024 NAR aging direct RNA-seq (PMC11662692)",
        "collabs": "Matt Kaeberlein (Optispan) \u2022 Sean Curran (USC) \u2022 Coleen Murphy (Princeton)",
        "howto": "amy_autoresearch_howto/05_cross_dataset_replication.md"
    }
]

for app in apps:
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide, DARK_BG)

    add_text_box(slide, 0.8, 0.3, 0.8, 0.5,
        app["num"], font_size=28, color=ACCENT_BLUE, bold=True)
    add_text_box(slide, 1.7, 0.3, 10, 0.5,
        app["title"], font_size=28, color=WHITE, bold=True)

    tf = add_text_box(slide, 0.8, 1.3, 7, 2.8,
        "What it does:", font_size=18, color=ACCENT_GREEN, bold=True)
    add_p(tf, app["does"], font_size=15, color=WHITE)
    add_p(tf, "", font_size=8, color=WHITE)
    add_p(tf, "Why it matters:", font_size=18, color=ACCENT_ORANGE, bold=True)
    add_p(tf, app["why"], font_size=15, color=WHITE)

    tf = add_text_box(slide, 8.5, 1.3, 4, 2.5,
        "Outputs", font_size=18, color=ACCENT_BLUE, bold=True)
    for o in app["outputs"]:
        add_p(tf, f"\u2022 {o}", font_size=14, color=WHITE)

    tf = add_text_box(slide, 0.8, 4.8, 11.5, 1.0,
        f"Anchor: {app['anchor']}", font_size=13, color=MEDIUM_GRAY)
    add_p(tf, f"Collaborators: {app['collabs']}", font_size=13, color=MEDIUM_GRAY)

    add_text_box(slide, 0.8, 6.2, 11.5, 0.8,
        f"\U0001f4c4 How-To: {app['howto']}", font_size=14, color=ACCENT_BLUE)

# ---------- SLIDE 8: How They Connect ----------
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, DARK_BG)
add_text_box(slide, 0.8, 0.3, 11, 0.8,
    "How the 5 Experiments Connect", font_size=32, color=ACCENT_BLUE, bold=True)

flow = [
    ("#1  Isoform Shifts", "feeds isoform-switching gene lists into..."),
    ("#2  Target Concordance", "provides curated miRNA target lists for..."),
    ("#3  Poly(A) / Translation", "identifies tail-length outliers, checked by..."),
    ("#4  Recovery Modules", "maps miRNAs to recovery programs, validated by..."),
    ("#5  Cross-Dataset Replication", "validates everything across independent data"),
]
tf = add_text_box(slide, 1.5, 1.5, 10, 5.0,
    flow[0][0], font_size=20, color=ACCENT_GREEN, bold=True)
add_p(tf, f"     {flow[0][1]}", font_size=15, color=LIGHT_GRAY)
for title, desc in flow[1:]:
    add_p(tf, "", font_size=8, color=WHITE)
    add_p(tf, title, font_size=20, color=ACCENT_GREEN, bold=True)
    add_p(tf, f"     {desc}", font_size=15, color=LIGHT_GRAY)

add_text_box(slide, 1.5, 6.5, 10, 0.6,
    "Each experiment produces outputs that feed into the others \u2014 a self-reinforcing evidence network",
    font_size=15, color=MEDIUM_GRAY, alignment=PP_ALIGN.CENTER)

# ---------- SLIDE 9: Getting Started ----------
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, DARK_BG)
add_text_box(slide, 0.8, 0.3, 11, 0.8,
    "Getting Started Today", font_size=32, color=ACCENT_BLUE, bold=True)

tf = add_text_box(slide, 0.8, 1.5, 5.5, 4.5,
    "Quick Wins (days, not weeks)", font_size=22, color=ACCENT_GREEN, bold=True)
for item in [
    "1. Gap-finder for grant proposals (1\u20132 days)",
    "2. New-paper alert service (half a day)",
    "3. Manuscript consistency checker (hours)",
    "4. Hypothesis ranking board (1\u20132 days)",
    "5. Lab knowledge base (ongoing)"
]:
    add_p(tf, item, font_size=16, color=WHITE)

tf = add_text_box(slide, 7.0, 1.5, 5.5, 4.5,
    "What the Field Shows", font_size=22, color=ACCENT_ORANGE, bold=True)
for item in [
    "\u2022 PaperQA2 beats PhD researchers at lit search",
    "\u2022 AI Scientist v2 passed peer review",
    "\u2022 Coscientist runs real chemistry experiments",
    "\u2022 Autoresearch runs on a laptop GPU",
    "\u2022 Cost: $0 beyond existing hardware"
]:
    add_p(tf, item, font_size=15, color=WHITE)

add_text_box(slide, 0.8, 6.2, 11.5, 0.8,
    "All how-to guides, starter code, and program.md templates are in amy_autoresearch_howto/",
    font_size=16, color=ACCENT_BLUE, alignment=PP_ALIGN.CENTER)

# ---------- Save ----------
prs.save("Pasquinelli_Autoresearch_Pitch.pptx")
print(f"Saved: Pasquinelli_Autoresearch_Pitch.pptx ({len(prs.slides)} slides)")
