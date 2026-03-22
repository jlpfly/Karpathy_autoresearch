"""
Generate the Pasquinelli Lab AI Research Agent Pitch Deck.
AI-themed presentation covering LLM agent training, corpus building,
and example prompts for Amy Pasquinelli and her postdocs.
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# ── Colour palette ──────────────────────────────────────────────────────────
DARK_BG       = RGBColor(0x0D, 0x0D, 0x1A)   # deep navy-black
PANEL_BG      = RGBColor(0x12, 0x12, 0x2E)   # slightly lighter panel
ACCENT_BLUE   = RGBColor(0x00, 0xB4, 0xFF)   # electric cyan-blue
ACCENT_PURPLE = RGBColor(0x9B, 0x59, 0xB6)   # neural-network purple
ACCENT_GREEN  = RGBColor(0x00, 0xE6, 0x76)   # bright bio-green
ACCENT_ORANGE = RGBColor(0xFF, 0x8C, 0x00)   # amber highlight
ACCENT_TEAL   = RGBColor(0x1A, 0xBC, 0x9C)   # teal for tables
WHITE         = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GRAY    = RGBColor(0xCC, 0xCC, 0xCC)
MEDIUM_GRAY   = RGBColor(0x88, 0x88, 0x99)
DARK_GRAY     = RGBColor(0x44, 0x44, 0x55)
GOLD          = RGBColor(0xF1, 0xC4, 0x0F)


# ── Helpers ──────────────────────────────────────────────────────────────────

def set_slide_bg(slide, color):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_box(slide, left, top, width, height, text,
            font_size=18, color=WHITE, bold=False,
            alignment=PP_ALIGN.LEFT, italic=False):
    txBox = slide.shapes.add_textbox(
        Inches(left), Inches(top), Inches(width), Inches(height))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.font.italic = italic
    p.alignment = alignment
    return tf


def add_p(tf, text, font_size=16, color=WHITE, bold=False,
          italic=False, space_before=4):
    p = tf.add_paragraph()
    p.text = text
    p.font.size = Pt(font_size)
    p.font.color.rgb = color
    p.font.bold = bold
    p.font.italic = italic
    p.space_before = Pt(space_before)
    return p


def add_rect(slide, left, top, width, height, fill_color, alpha=None):
    """Add a filled rectangle (decorative panel)."""
    shape = slide.shapes.add_shape(
        1,  # MSO_SHAPE_TYPE.RECTANGLE
        Inches(left), Inches(top), Inches(width), Inches(height))
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.fill.background()
    return shape


def footer(slide, text, y=6.85):
    add_box(slide, 0.4, y, 12.5, 0.45, text,
            font_size=11, color=MEDIUM_GRAY, alignment=PP_ALIGN.CENTER)


def divider_line(slide, y=1.15, width=12.5, left=0.4, color=ACCENT_BLUE):
    """Draw a thin horizontal rule using a very flat rectangle."""
    shape = slide.shapes.add_shape(
        1, Inches(left), Inches(y), Inches(width), Inches(0.02))
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 1 — Title
# ═══════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, DARK_BG)

# Decorative side bar
add_rect(slide, 0, 0, 0.18, 7.5, ACCENT_BLUE)
add_rect(slide, 0.18, 0, 0.06, 7.5, ACCENT_PURPLE)

# Decorative bottom bar
add_rect(slide, 0, 7.1, 13.333, 0.4, PANEL_BG)

add_box(slide, 0.6, 0.5, 12.2, 0.6,
        "PASQUINELLI LAB  ·  UC SAN DIEGO  ·  DEPARTMENT OF MOLECULAR BIOLOGY",
        font_size=11, color=ACCENT_BLUE, alignment=PP_ALIGN.LEFT)

add_box(slide, 0.6, 1.2, 12.0, 1.8,
        "Your Lab\u2019s Own LLM:",
        font_size=52, color=WHITE, bold=True, alignment=PP_ALIGN.LEFT)

add_box(slide, 0.6, 2.85, 12.0, 1.0,
        "An AI Research Agent for miRNA Biology, Aging & RNA Processing",
        font_size=28, color=ACCENT_BLUE, bold=False, alignment=PP_ALIGN.LEFT)

divider_line(slide, y=4.05, left=0.6, width=11.5, color=ACCENT_PURPLE)

tf = add_box(slide, 0.6, 4.25, 12.0, 0.55,
             "Built on Karpathy\u2019s autoresearch framework  \u2022  Amy_Autoresearch branch",
             font_size=15, color=LIGHT_GRAY, alignment=PP_ALIGN.LEFT)

add_box(slide, 0.6, 4.9, 12.0, 0.55,
        "github.com/jlpfly/Karpathy_autoresearch  \u2022  Runs on Dell XPS 15 (RTX 3050 Ti)",
        font_size=14, color=MEDIUM_GRAY, alignment=PP_ALIGN.LEFT)

add_box(slide, 0.6, 5.6, 12.0, 0.55,
        "Training corpus: 25 years of Pasquinelli lab publications + the full miRNA field",
        font_size=14, color=MEDIUM_GRAY, alignment=PP_ALIGN.LEFT)

add_box(slide, 0.6, 7.12, 12.0, 0.35,
        "Autoresearch \u2022 RAG \u2022 Fine-Tuning \u2022 Autonomous Agent Loop \u2022 miRNA Biology \u2022 C. elegans Aging",
        font_size=11, color=DARK_GRAY, alignment=PP_ALIGN.LEFT)


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 2 — The Vision
# ═══════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, DARK_BG)
add_rect(slide, 0, 0, 0.18, 7.5, ACCENT_PURPLE)

add_box(slide, 0.5, 0.25, 12.0, 0.7,
        "THE VISION",
        font_size=11, color=ACCENT_PURPLE, bold=True)
add_box(slide, 0.5, 0.6, 12.0, 0.75,
        "Imagine an AI that has read every paper your lab has ever published",
        font_size=30, color=WHITE, bold=True)
divider_line(slide, y=1.45, left=0.5, color=ACCENT_PURPLE)

# Left panel
add_rect(slide, 0.5, 1.6, 5.9, 4.6, PANEL_BG)
add_box(slide, 0.7, 1.75, 5.5, 0.5,
        "What this LLM knows", font_size=18, color=ACCENT_BLUE, bold=True)
tf = add_box(slide, 0.7, 2.35, 5.5, 3.7,
             "\u2022 Every Pasquinelli lab paper from let-7 (2000) through the 2024 aging RNA-seq study",
             font_size=14, color=WHITE)
add_p(tf, "\u2022 The full miRNA field: TargetScan, miRDB, AGO biology, CLIP/CLASH datasets",
      font_size=14, color=WHITE, space_before=6)
add_p(tf, "\u2022 C. elegans aging literature, heat-shock recovery, poly(A) tail biology",
      font_size=14, color=WHITE, space_before=6)
add_p(tf, "\u2022 Your unpublished datasets, protocols, and experimental notes (optional)",
      font_size=14, color=WHITE, space_before=6)

# Right panel
add_rect(slide, 6.9, 1.6, 6.0, 4.6, PANEL_BG)
add_box(slide, 7.1, 1.75, 5.6, 0.5,
        "What this means for the lab", font_size=18, color=ACCENT_GREEN, bold=True)
tf = add_box(slide, 7.1, 2.35, 5.6, 3.7,
             "\u201cWhat are the strongest open questions in let-7 biology right now?\u201d",
             font_size=13, color=ACCENT_BLUE, italic=True)
add_p(tf, "   \u2192 Amy, strategic planning", font_size=12, color=MEDIUM_GRAY)
add_p(tf, "", font_size=6, color=WHITE)
add_p(tf, "\u201cDesign a follow-up experiment for our miR-238 longevity finding.\u201d",
      font_size=13, color=ACCENT_BLUE, italic=True, space_before=6)
add_p(tf, "   \u2192 Postdoc, experimental design", font_size=12, color=MEDIUM_GRAY)
add_p(tf, "", font_size=6, color=WHITE)
add_p(tf, "\u201cExplain the ALG-1 vs ALG-2 aging phenotype to me.\u201d",
      font_size=13, color=ACCENT_BLUE, italic=True, space_before=6)
add_p(tf, "   \u2192 Rotation student, onboarding", font_size=12, color=MEDIUM_GRAY)
add_p(tf, "", font_size=6, color=WHITE)
add_p(tf, "\u201cWhat gaps in the aging-miRNA field should our R01 address?\u201d",
      font_size=13, color=ACCENT_BLUE, italic=True, space_before=6)
add_p(tf, "   \u2192 Grant writing, Significance section", font_size=12, color=MEDIUM_GRAY)

add_box(slide, 0.5, 6.35, 12.5, 0.55,
        "This is not a generic chatbot. It is trained specifically on the body of work most relevant to your research program.",
        font_size=14, color=GOLD, bold=True, alignment=PP_ALIGN.CENTER)
footer(slide, "Pasquinelli Lab AI Research Agent  \u2022  github.com/jlpfly/Karpathy_autoresearch  \u2022  Amy_Autoresearch branch")


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 3 — Architecture: Three Layers
# ═══════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, DARK_BG)
add_rect(slide, 0, 0, 0.18, 7.5, ACCENT_TEAL)

add_box(slide, 0.5, 0.25, 12.0, 0.4,
        "ARCHITECTURE", font_size=11, color=ACCENT_TEAL, bold=True)
add_box(slide, 0.5, 0.55, 12.0, 0.7,
        "Three layers make this agent work: Corpus \u2022 Model \u2022 Agent Loop",
        font_size=28, color=WHITE, bold=True)
divider_line(slide, y=1.35, left=0.5, color=ACCENT_TEAL)

# Layer 1
add_rect(slide, 0.5, 1.5, 3.8, 4.7, PANEL_BG)
add_box(slide, 0.65, 1.6, 3.5, 0.5,
        "LAYER 1", font_size=11, color=ACCENT_TEAL, bold=True)
add_box(slide, 0.65, 1.95, 3.5, 0.5,
        "The Corpus", font_size=20, color=WHITE, bold=True)
add_box(slide, 0.65, 2.45, 3.5, 0.35,
        "What it reads", font_size=13, color=MEDIUM_GRAY)
tf = add_box(slide, 0.65, 2.9, 3.5, 3.1,
             "\u2022 All Pasquinelli lab papers (2000\u20132025): ~55 papers",
             font_size=13, color=WHITE)
add_p(tf, "\u2022 Field-defining papers: Bartel, Ambros, Tuschl labs", font_size=13, color=WHITE, space_before=5)
add_p(tf, "\u2022 PubMed abstracts, PMC full text, GEO metadata", font_size=13, color=WHITE, space_before=5)
add_p(tf, "\u2022 Lab protocols, grant aims, meeting notes (optional)", font_size=13, color=WHITE, space_before=5)

# Layer 2
add_rect(slide, 4.77, 1.5, 3.8, 4.7, PANEL_BG)
add_box(slide, 4.92, 1.6, 3.5, 0.5,
        "LAYER 2", font_size=11, color=ACCENT_PURPLE, bold=True)
add_box(slide, 4.92, 1.95, 3.5, 0.5,
        "The Model", font_size=20, color=WHITE, bold=True)
add_box(slide, 4.92, 2.45, 3.5, 0.35,
        "How it learns", font_size=13, color=MEDIUM_GRAY)
tf = add_box(slide, 4.92, 2.9, 3.5, 3.1,
             "\u2022 Base: Llama 3, Mistral, or GPT-4 via API",
             font_size=13, color=WHITE)
add_p(tf, "\u2022 Method: RAG or supervised fine-tuning on corpus", font_size=13, color=WHITE, space_before=5)
add_p(tf, "\u2022 Hardware: RTX 3050 Ti (already in the lab)", font_size=13, color=WHITE, space_before=5)
add_p(tf, "\u2022 Time to first version: 1\u20132 days setup + overnight", font_size=13, color=WHITE, space_before=5)

# Layer 3
add_rect(slide, 9.04, 1.5, 3.9, 4.7, PANEL_BG)
add_box(slide, 9.19, 1.6, 3.6, 0.5,
        "LAYER 3", font_size=11, color=ACCENT_GREEN, bold=True)
add_box(slide, 9.19, 1.95, 3.6, 0.5,
        "The Agent Loop", font_size=20, color=WHITE, bold=True)
add_box(slide, 9.19, 2.45, 3.6, 0.35,
        "How it acts", font_size=13, color=MEDIUM_GRAY)
tf = add_box(slide, 9.19, 2.9, 3.6, 3.1,
             "\u2022 Reads program.md (your research strategy)",
             font_size=13, color=WHITE)
add_p(tf, "\u2022 Iterates: reads \u2192 extracts \u2192 hypothesizes \u2192 ranks", font_size=13, color=WHITE, space_before=5)
add_p(tf, "\u2022 Outputs: tables, hypothesis boards, reading queues", font_size=13, color=WHITE, space_before=5)
add_p(tf, "\u2022 Human stays in control: review, redirect, refine", font_size=13, color=WHITE, space_before=5)

footer(slide, "Pasquinelli Lab AI Research Agent  \u2022  github.com/jlpfly/Karpathy_autoresearch  \u2022  Amy_Autoresearch branch")


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 4 — How to Build It
# ═══════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, DARK_BG)
add_rect(slide, 0, 0, 0.18, 7.5, ACCENT_GREEN)

add_box(slide, 0.5, 0.25, 12.0, 0.4,
        "HOW TO BUILD IT", font_size=11, color=ACCENT_GREEN, bold=True)
add_box(slide, 0.5, 0.55, 12.0, 0.7,
        "Building the Pasquinelli Lab LLM takes one weekend, not one year",
        font_size=27, color=WHITE, bold=True)
divider_line(slide, y=1.35, left=0.5, color=ACCENT_GREEN)

steps = [
    ("01", ACCENT_BLUE,
     "Set up the environment  (Day 1, ~2 hours)",
     "git clone https://github.com/jlpfly/Karpathy_autoresearch\n"
     "git checkout Amy_Autoresearch\n"
     "uv python install 3.11  &&  uv sync  &&  uv run prepare.py\n"
     "Hardware: Dell XPS 15 with RTX 3050 Ti \u2014 already validated"),
    ("02", ACCENT_PURPLE,
     "Build the corpus  (Day 1, ~3 hours)",
     "Export PDFs of all Pasquinelli lab papers from PubMed/PMC\n"
     "Add key field papers (Bartel, Ambros, let-7 foundational work)\n"
     "Convert to text: pdftotext paper.pdf paper.txt\n"
     "Place in corpus/ directory"),
    ("03", ACCENT_TEAL,
     "Configure the agent  (Day 1, ~1 hour)",
     "Edit program.md to define the agent\u2019s role\n"
     "Set focus: \u201cYou are a research assistant for the Pasquinelli Lab\u2026\u201d\n"
     "Define output format: tables, ranked lists, hypothesis boards"),
    ("04", ACCENT_ORANGE,
     "Run overnight  (Day 2)",
     "uv run train.py   # 5-minute baseline validation\n"
     "Launch Claude/Codex with program.md \u2014 let it iterate\n"
     "Wake up to a log of experiments and structured outputs"),
    ("05", ACCENT_GREEN,
     "Query and iterate  (ongoing)",
     "Start asking questions (see example prompt slides)\n"
     "Refine program.md based on output quality\n"
     "Add new papers as they are published"),
]

col_w = 2.35
for i, (num, col, title, body) in enumerate(steps):
    x = 0.5 + i * (col_w + 0.12)
    add_rect(slide, x, 1.5, col_w, 5.1, PANEL_BG)
    add_box(slide, x + 0.12, 1.6, col_w - 0.2, 0.55,
            num, font_size=26, color=col, bold=True)
    add_box(slide, x + 0.12, 2.2, col_w - 0.2, 0.65,
            title, font_size=12, color=WHITE, bold=True)
    add_box(slide, x + 0.12, 2.95, col_w - 0.2, 3.5,
            body, font_size=11, color=LIGHT_GRAY)

footer(slide, "Pasquinelli Lab AI Research Agent  \u2022  github.com/jlpfly/Karpathy_autoresearch  \u2022  Amy_Autoresearch branch")


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 5 — The Corpus
# ═══════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, DARK_BG)
add_rect(slide, 0, 0, 0.18, 7.5, ACCENT_ORANGE)

add_box(slide, 0.5, 0.25, 12.0, 0.4,
        "THE CORPUS", font_size=11, color=ACCENT_ORANGE, bold=True)
add_box(slide, 0.5, 0.55, 12.0, 0.7,
        "The quality of the corpus determines the quality of the intelligence",
        font_size=27, color=WHITE, bold=True)
divider_line(slide, y=1.35, left=0.5, color=ACCENT_ORANGE)

# Table header
add_rect(slide, 0.5, 1.5, 12.4, 0.45, ACCENT_ORANGE)
cols = [("Layer", 1.7), ("Content", 3.5), ("Papers / Items", 1.9), ("Priority", 1.7)]
x = 0.6
for label, w in cols:
    add_box(slide, x, 1.52, w, 0.4, label, font_size=13, color=DARK_BG, bold=True)
    x += w + 0.05

rows = [
    ("Core Lab",        "All Pasquinelli lab publications 2000\u20132025",       "~55 papers",   "Essential",  ACCENT_GREEN),
    ("Field Foundation","Bartel, Ambros, Tuschl landmark miRNA papers",           "~30 papers",   "Essential",  ACCENT_GREEN),
    ("Aging & C. elegans","Kaeberlein, Murphy, Curran aging papers",              "~20 papers",   "High",       ACCENT_BLUE),
    ("Poly(A) & Translation","Richter, Gilbert, Wickens PABP/translation papers", "~15 papers",   "High",       ACCENT_BLUE),
    ("Databases",       "TargetScan, miRDB, CLIP-seq datasets (metadata)",        "~5 sources",   "Medium",     ACCENT_TEAL),
    ("Lab Materials",   "Protocols, grant aims, meeting notes",                   "Variable",     "Optional",   MEDIUM_GRAY),
]
for r_idx, (layer, content, count, priority, row_col) in enumerate(rows):
    y = 2.05 + r_idx * 0.57
    bg = PANEL_BG if r_idx % 2 == 0 else DARK_BG
    add_rect(slide, 0.5, y, 12.4, 0.55, bg)
    add_box(slide, 0.6, y + 0.05, 1.65, 0.45, layer, font_size=12, color=row_col, bold=True)
    add_box(slide, 2.3, y + 0.05, 3.45, 0.45, content, font_size=12, color=WHITE)
    add_box(slide, 5.8, y + 0.05, 1.85, 0.45, count, font_size=12, color=LIGHT_GRAY, alignment=PP_ALIGN.CENTER)
    add_box(slide, 7.7, y + 0.05, 1.65, 0.45, priority, font_size=12, color=row_col, bold=True, alignment=PP_ALIGN.CENTER)

add_box(slide, 0.5, 5.55, 12.4, 0.5,
        "Key principle: Start with the lab\u2019s own papers. The agent will already be more useful than a generic LLM after just this first layer.",
        font_size=13, color=GOLD, bold=True)
tf = add_box(slide, 0.5, 6.1, 12.4, 0.5,
             "Sources: PubMed Central (pmc.ncbi.nlm.nih.gov)  \u2022  Semantic Scholar API  \u2022  bioRxiv preprints",
             font_size=12, color=MEDIUM_GRAY)
footer(slide, "Pasquinelli Lab AI Research Agent  \u2022  github.com/jlpfly/Karpathy_autoresearch  \u2022  Amy_Autoresearch branch")


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 6 — Example Prompts: Amy
# ═══════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, DARK_BG)
add_rect(slide, 0, 0, 0.18, 7.5, ACCENT_BLUE)

add_box(slide, 0.5, 0.25, 12.0, 0.4,
        "EXAMPLE PROMPTS \u2014 AMY PASQUINELLI (PI)", font_size=11, color=ACCENT_BLUE, bold=True)
add_box(slide, 0.5, 0.55, 12.0, 0.7,
        "Strategic questions that used to take days to answer",
        font_size=27, color=WHITE, bold=True)
divider_line(slide, y=1.35, left=0.5, color=ACCENT_BLUE)

prompts_amy = [
    ("Grant strategy",
     "\u201cSummarize the strongest open questions in miRNA-mediated aging regulation in C. elegans after 2020. "
     "Rank them by how well-supported they are and how testable they are with our current tools.\u201d",
     "Ranked hypothesis table with citations, evidence strength scores, and suggested experimental approaches."),
    ("Mechanism mapping",
     "\u201cMap the evidence for how ALG-1 and ALG-2 produce opposing aging phenotypes. "
     "What are the proposed mechanisms? What is still unresolved?\u201d",
     "Mechanistic diagram in text form, evidence table, list of unresolved questions with citations."),
    ("Cross-paper synthesis",
     "\u201cCompare our heat-shock recovery paper (2021) with our aging RNA-seq paper (2024). "
     "Which miRNAs appear in both contexts? What does that suggest about shared regulatory programs?\u201d",
     "Overlap analysis, shared gene/miRNA lists, synthesis paragraph with citations."),
    ("Field positioning",
     "\u201cHow does our lab\u2019s expression-not-sequence interpretation of miRNA target specificity compare "
     "to the current consensus? Who agrees, who disagrees, and what would resolve it?\u201d",
     "Field map with lab positions, supporting/contradicting papers, resolution experiments."),
]

for i, (label, prompt, output) in enumerate(prompts_amy):
    y = 1.5 + i * 1.2
    add_rect(slide, 0.5, y, 12.4, 1.1, PANEL_BG)
    add_box(slide, 0.65, y + 0.05, 2.0, 0.35, label, font_size=11, color=ACCENT_ORANGE, bold=True)
    add_box(slide, 0.65, y + 0.32, 8.5, 0.45, prompt, font_size=12, color=ACCENT_BLUE, italic=True)
    add_box(slide, 0.65, y + 0.72, 11.5, 0.32,
            f"\u2192 Output: {output}", font_size=11, color=LIGHT_GRAY)

footer(slide, "Pasquinelli Lab AI Research Agent  \u2022  github.com/jlpfly/Karpathy_autoresearch  \u2022  Amy_Autoresearch branch")


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 7 — Example Prompts: Postdocs
# ═══════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, DARK_BG)
add_rect(slide, 0, 0, 0.18, 7.5, ACCENT_GREEN)

add_box(slide, 0.5, 0.25, 12.0, 0.4,
        "EXAMPLE PROMPTS \u2014 POSTDOCS & GRADUATE STUDENTS", font_size=11, color=ACCENT_GREEN, bold=True)
add_box(slide, 0.5, 0.55, 12.0, 0.7,
        "Daily research acceleration for every lab member",
        font_size=27, color=WHITE, bold=True)
divider_line(slide, y=1.35, left=0.5, color=ACCENT_GREEN)

prompts_pd = [
    ("Experimental design",
     "\u201cI\u2019m planning a follow-up to the miR-238/239ab longevity paper. What are the three most testable "
     "hypotheses that would extend this work? What controls would be critical for each?\u201d",
     "Three hypothesis cards with experimental design, controls, and relevant citations."),
    ("Literature catch-up",
     "\u201cI just joined the lab. Give me a structured reading path from the foundational let-7 papers "
     "through the most recent aging work. Start with what I need to understand the 2024 NAR paper.\u201d",
     "Tiered reading list with annotations, estimated reading time, key concepts per paper."),
    ("Data interpretation",
     "\u201cWe found that transcript X has a short poly(A) tail but high translation efficiency. "
     "Is this an outlier? What mechanisms could explain it based on the PABP literature?\u201d",
     "Literature-grounded interpretation, candidate mechanisms, papers to read."),
    ("Manuscript prep",
     "\u201cCheck the consistency between our methods section and figure legends for the heat-shock recovery "
     "paper. Flag any discrepancies in sample sizes, strain names, or statistical tests.\u201d",
     "Discrepancy table with line numbers and suggested corrections."),
    ("Journal club prep",
     "\u201cSummarize this new paper on miRNA-mediated translational repression in 5 points. "
     "How does it relate to our lab\u2019s work? What questions should we ask the authors?\u201d",
     "Summary, relevance assessment, 3\u20135 discussion questions."),
]

col_w = 2.38
for i, (label, prompt, output) in enumerate(prompts_pd):
    x = 0.5 + i * (col_w + 0.1)
    add_rect(slide, x, 1.5, col_w, 5.1, PANEL_BG)
    add_box(slide, x + 0.1, 1.6, col_w - 0.15, 0.4,
            label, font_size=12, color=ACCENT_GREEN, bold=True)
    add_box(slide, x + 0.1, 2.1, col_w - 0.15, 2.5,
            prompt, font_size=11, color=ACCENT_BLUE, italic=True)
    divider_line(slide, y=4.65, left=x + 0.1, width=col_w - 0.2, color=DARK_GRAY)
    add_box(slide, x + 0.1, 4.72, col_w - 0.15, 1.7,
            f"Output:\n{output}", font_size=10, color=LIGHT_GRAY)

footer(slide, "Pasquinelli Lab AI Research Agent  \u2022  github.com/jlpfly/Karpathy_autoresearch  \u2022  Amy_Autoresearch branch")


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 8 — Overnight Autonomous Research
# ═══════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, DARK_BG)
add_rect(slide, 0, 0, 0.18, 7.5, ACCENT_PURPLE)

add_box(slide, 0.5, 0.25, 12.0, 0.4,
        "OVERNIGHT AUTONOMOUS RESEARCH", font_size=11, color=ACCENT_PURPLE, bold=True)
add_box(slide, 0.5, 0.55, 12.0, 0.7,
        "Let the agent work while you sleep \u2014 wake up to structured results",
        font_size=27, color=WHITE, bold=True)
divider_line(slide, y=1.35, left=0.5, color=ACCENT_PURPLE)

overnight = [
    ("Literature sweep",
     "\u201cSearch for all papers published in the last 6 months on miRNA regulation in aging organisms. "
     "Summarize each, score relevance to our lab\u2019s work (1\u201310), and flag any that contradict our published findings.\u201d",
     "Ranked paper list \u2022 Relevance scores \u2022 Contradiction flags"),
    ("Cross-dataset replication",
     "\u201cDownload all public C. elegans aging RNA-seq datasets from GEO. Score each using the gene signatures "
     "from our 2024 NAR paper. Report which signatures replicate and which do not.\u201d",
     "Replication score table \u2022 Forest plots \u2022 Core aging marker gene set"),
    ("Target concordance",
     "\u201cFor let-7 and miR-238, pull predictions from TargetScan and miRDB. Cross-reference against our "
     "published functional data. Build a concordance score for each predicted target.\u201d",
     "Concordance-scored target table \u2022 Venn diagrams \u2022 High-confidence target shortlist"),
    ("Hypothesis generation",
     "\u201cStarting from our 2021 heat-shock recovery paper, find all related papers on miRNA-mediated stress "
     "recovery. Generate 10 testable hypotheses ranked by evidence strength and experimental feasibility.\u201d",
     "Ranked hypothesis board \u2022 Citations \u2022 Experimental sketches"),
]

for i, (label, prompt, output) in enumerate(overnight):
    y = 1.5 + i * 1.2
    add_rect(slide, 0.5, y, 12.4, 1.1, PANEL_BG)
    add_box(slide, 0.65, y + 0.04, 2.2, 0.35, f"Task {i+1}: {label}", font_size=11, color=ACCENT_PURPLE, bold=True)
    add_box(slide, 0.65, y + 0.32, 8.8, 0.45, prompt, font_size=12, color=ACCENT_BLUE, italic=True)
    add_box(slide, 0.65, y + 0.72, 11.5, 0.32,
            f"\u2192 By morning: {output}", font_size=11, color=ACCENT_GREEN)

footer(slide, "Pasquinelli Lab AI Research Agent  \u2022  github.com/jlpfly/Karpathy_autoresearch  \u2022  Amy_Autoresearch branch")


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 9 — The 5 Computational Applications
# ═══════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, DARK_BG)
add_rect(slide, 0, 0, 0.18, 7.5, ACCENT_TEAL)

add_box(slide, 0.5, 0.25, 12.0, 0.4,
        "5 IMPACTFUL COMPUTATIONAL APPLICATIONS", font_size=11, color=ACCENT_TEAL, bold=True)
add_box(slide, 0.5, 0.55, 12.0, 0.7,
        "Five experiments the agent can run on real datasets \u2014 not just literature",
        font_size=27, color=WHITE, bold=True)
divider_line(slide, y=1.35, left=0.5, color=ACCENT_TEAL)

apps = [
    ("01", "Age-Dependent Isoform Shift Quantification",
     "Reanalyzes 2024 direct RNA-seq aging data to build age-stratified isoform usage matrix.",
     "2024 NAR aging direct RNA-seq (PMC11662692)",
     "Ranked switching gene list \u2022 Age-group heatmaps \u2022 GO enrichment"),
    ("02", "Cross-Dataset miRNA Target Concordance",
     "Integrates TargetScan, miRDB, and CLIP/CLASH; cross-references against lab functional data.",
     "2023 miR-238/239ab paper (PLoS Genetics)",
     "Concordance-scored target table \u2022 Venn diagrams \u2022 Top 20 targets per miRNA"),
    ("03", "Poly(A)-Tail & Translation Efficiency Integration",
     "Correlates poly(A)-tail length with translational output; identifies outlier transcripts.",
     "2022 NAR PABP paper (PMC9071453)",
     "Tail length vs. TE scatter plots \u2022 Outlier transcript lists \u2022 GO enrichment"),
    ("04", "Stress-Recovery Time-Series Gene Module Detection",
     "Clusters genes into co-regulated modules from heat-shock recovery dynamics; maps miRNA targets.",
     "2021 PLoS Genetics heat-shock recovery (PMC8370650)",
     "Temporal profile plots \u2022 miRNA-module enrichment scores \u2022 Network visualizations"),
    ("05", "Automated Cross-Dataset Replication of Aging Signatures",
     "Downloads public C. elegans aging RNA-seq datasets from GEO; scores each with lab-derived signatures.",
     "2024 NAR aging direct RNA-seq (PMC11662692)",
     "Replication score table \u2022 Forest plots \u2022 Core aging marker gene set"),
]

col_w = 2.38
for i, (num, title, does, anchor, outputs) in enumerate(apps):
    x = 0.5 + i * (col_w + 0.1)
    add_rect(slide, x, 1.5, col_w, 5.1, PANEL_BG)
    add_box(slide, x + 0.1, 1.58, col_w - 0.15, 0.4,
            num, font_size=22, color=ACCENT_TEAL, bold=True)
    add_box(slide, x + 0.1, 1.95, col_w - 0.15, 0.65,
            title, font_size=11, color=WHITE, bold=True)
    add_box(slide, x + 0.1, 2.7, col_w - 0.15, 1.3,
            does, font_size=11, color=LIGHT_GRAY)
    add_box(slide, x + 0.1, 4.1, col_w - 0.15, 0.35,
            "Anchor:", font_size=10, color=MEDIUM_GRAY, bold=True)
    add_box(slide, x + 0.1, 4.4, col_w - 0.15, 0.45,
            anchor, font_size=10, color=MEDIUM_GRAY)
    add_box(slide, x + 0.1, 4.95, col_w - 0.15, 0.35,
            "Outputs:", font_size=10, color=ACCENT_GREEN, bold=True)
    add_box(slide, x + 0.1, 5.25, col_w - 0.15, 1.1,
            outputs, font_size=10, color=LIGHT_GRAY)

footer(slide, "Pasquinelli Lab AI Research Agent  \u2022  github.com/jlpfly/Karpathy_autoresearch  \u2022  Amy_Autoresearch branch")


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 10 — How the 5 Experiments Connect
# ═══════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, DARK_BG)
add_rect(slide, 0, 0, 0.18, 7.5, ACCENT_BLUE)

add_box(slide, 0.5, 0.25, 12.0, 0.4,
        "THE EVIDENCE NETWORK", font_size=11, color=ACCENT_BLUE, bold=True)
add_box(slide, 0.5, 0.55, 12.0, 0.7,
        "Each experiment feeds the next \u2014 a self-reinforcing evidence network",
        font_size=27, color=WHITE, bold=True)
divider_line(slide, y=1.35, left=0.5, color=ACCENT_BLUE)

flow_items = [
    ("#1  Isoform Shifts",
     "feeds isoform-switching gene lists into \u2192",
     "2024 NAR aging RNA-seq", ACCENT_TEAL),
    ("#2  Target Concordance",
     "provides curated miRNA target lists for \u2192",
     "2023 miR-238/239ab paper", ACCENT_PURPLE),
    ("#3  Poly(A) / Translation",
     "identifies tail-length outliers, checked by \u2192",
     "2022 NAR PABP paper", ACCENT_ORANGE),
    ("#4  Recovery Modules",
     "maps miRNAs to recovery programs, validated by \u2192",
     "2021 PLoS Genetics heat-shock", ACCENT_GREEN),
    ("#5  Cross-Dataset Replication",
     "validates everything across independent data",
     "2024 NAR aging RNA-seq", ACCENT_BLUE),
]

for i, (title, desc, anchor, col) in enumerate(flow_items):
    y = 1.5 + i * 0.98
    add_rect(slide, 0.5, y, 12.4, 0.88, PANEL_BG)
    add_box(slide, 0.65, y + 0.08, 2.8, 0.4, title, font_size=16, color=col, bold=True)
    add_box(slide, 3.6, y + 0.08, 6.5, 0.4, desc, font_size=14, color=LIGHT_GRAY)
    add_box(slide, 10.2, y + 0.08, 2.6, 0.4, anchor, font_size=11, color=MEDIUM_GRAY, italic=True)

add_box(slide, 0.5, 6.45, 12.4, 0.45,
        "Running all five creates a compounding evidence network. The agent can run all five overnight and synthesize the results by morning.",
        font_size=13, color=GOLD, bold=True, alignment=PP_ALIGN.CENTER)
footer(slide, "Pasquinelli Lab AI Research Agent  \u2022  github.com/jlpfly/Karpathy_autoresearch  \u2022  Amy_Autoresearch branch")


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 11 — The Field Is Moving
# ═══════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, DARK_BG)
add_rect(slide, 0, 0, 0.18, 7.5, ACCENT_ORANGE)

add_box(slide, 0.5, 0.25, 12.0, 0.4,
        "THE FIELD IS ALREADY MOVING", font_size=11, color=ACCENT_ORANGE, bold=True)
add_box(slide, 0.5, 0.55, 12.0, 0.7,
        "Autonomous AI research is no longer speculative \u2014 it is happening now",
        font_size=27, color=WHITE, bold=True)
divider_line(slide, y=1.35, left=0.5, color=ACCENT_ORANGE)

# Table header
add_rect(slide, 0.5, 1.5, 12.4, 0.45, ACCENT_ORANGE)
hdr_cols = [("System", 1.8), ("Organization", 2.2), ("Milestone", 4.5), ("Relevance to Lab", 3.5)]
hx = 0.6
for label, w in hdr_cols:
    add_box(slide, hx, 1.52, w, 0.4, label, font_size=12, color=DARK_BG, bold=True)
    hx += w + 0.05

field_rows = [
    ("autoresearch",    "Karpathy (2026)",   "Agent-driven code iteration on consumer GPU; adopted worldwide in weeks",
     "Foundation of this repo", ACCENT_BLUE),
    ("PaperQA2",        "FutureHouse",       "Beats PhD researchers at biology literature search (LitQA2 benchmark)",
     "Direct analog for miRNA literature work", ACCENT_GREEN),
    ("ContraCrow",      "FutureHouse",       "Finds ~2.34 contradicted statements per biology paper",
     "Contradiction finder for miRNA field", ACCENT_TEAL),
    ("WikiCrow",        "FutureHouse",       "Gene-level summaries from 1 million papers, more accurate than Wikipedia",
     "Gene-level knowledge base for C. elegans", ACCENT_TEAL),
    ("AI Scientist v2", "Sakana AI",         "First AI-generated paper to pass peer review at ICLR workshop",
     "Full autonomous research loop", ACCENT_PURPLE),
    ("Coscientist",     "CMU (Gomes lab)",   "Autonomous chemistry experiments via robotic API (Nature, 2023)",
     "Closes hypothesis-to-wet-lab loop", ACCENT_ORANGE),
]

for r_idx, (system, org, milestone, relevance, col) in enumerate(field_rows):
    y = 2.05 + r_idx * 0.58
    bg = PANEL_BG if r_idx % 2 == 0 else DARK_BG
    add_rect(slide, 0.5, y, 12.4, 0.55, bg)
    add_box(slide, 0.6, y + 0.06, 1.75, 0.42, system, font_size=12, color=col, bold=True)
    add_box(slide, 2.4, y + 0.06, 2.15, 0.42, org, font_size=11, color=LIGHT_GRAY)
    add_box(slide, 4.6, y + 0.06, 4.45, 0.42, milestone, font_size=11, color=WHITE)
    add_box(slide, 9.1, y + 0.06, 3.45, 0.42, relevance, font_size=11, color=MEDIUM_GRAY, italic=True)

add_box(slide, 0.5, 5.6, 12.4, 0.5,
        "The question is not whether autonomous research tools will be useful in biology labs \u2014 it is how quickly labs like the Pasquinelli lab adopt them.",
        font_size=13, color=GOLD, bold=True, alignment=PP_ALIGN.CENTER)
footer(slide, "Pasquinelli Lab AI Research Agent  \u2022  github.com/jlpfly/Karpathy_autoresearch  \u2022  Amy_Autoresearch branch")


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 12 — RAG vs. Fine-Tuning
# ═══════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, DARK_BG)
add_rect(slide, 0, 0, 0.18, 7.5, ACCENT_PURPLE)

add_box(slide, 0.5, 0.25, 12.0, 0.4,
        "TECHNICAL APPROACH", font_size=11, color=ACCENT_PURPLE, bold=True)
add_box(slide, 0.5, 0.55, 12.0, 0.7,
        "Two paths to a lab-specific LLM \u2014 choose based on your goals",
        font_size=27, color=WHITE, bold=True)
divider_line(slide, y=1.35, left=0.5, color=ACCENT_PURPLE)

# Table header
add_rect(slide, 0.5, 1.5, 12.4, 0.45, ACCENT_PURPLE)
add_box(slide, 0.6, 1.52, 3.5, 0.4, "Dimension", font_size=13, color=DARK_BG, bold=True)
add_box(slide, 4.15, 1.52, 4.1, 0.4, "RAG (Retrieval-Augmented Generation)", font_size=13, color=DARK_BG, bold=True)
add_box(slide, 8.3, 1.52, 4.3, 0.4, "Fine-Tuning", font_size=13, color=DARK_BG, bold=True)

rag_rows = [
    ("Setup time",          "Hours to days",                        "Days to weeks"),
    ("Hardware needed",     "CPU or small GPU",                     "GPU (RTX 3050 Ti sufficient)"),
    ("Corpus update",       "Add files, re-index (minutes)",        "Retrain (hours)"),
    ("Answers cite sources","Yes, automatically",                   "Requires prompting"),
    ("Best for",            "Literature Q&A, hypothesis generation","Style adaptation, specialized reasoning"),
    ("Cost",                "Near-zero (local) or low API cost",    "Near-zero (local)"),
    ("Recommended for lab", "START HERE",                           "Add later for specialized tasks"),
]

for r_idx, (dim, rag, ft) in enumerate(rag_rows):
    y = 2.05 + r_idx * 0.52
    bg = PANEL_BG if r_idx % 2 == 0 else DARK_BG
    add_rect(slide, 0.5, y, 12.4, 0.5, bg)
    add_box(slide, 0.6, y + 0.06, 3.45, 0.38, dim, font_size=12, color=LIGHT_GRAY, bold=True)
    rag_col = ACCENT_GREEN if dim == "Recommended for lab" else WHITE
    ft_col  = MEDIUM_GRAY  if dim == "Recommended for lab" else WHITE
    add_box(slide, 4.1, y + 0.06, 4.1, 0.38, rag, font_size=12, color=rag_col)
    add_box(slide, 8.25, y + 0.06, 4.3, 0.38, ft, font_size=12, color=ft_col)

tf = add_box(slide, 0.5, 5.7, 12.4, 0.5,
             "RAG in plain English: The model looks up relevant passages from your corpus before answering \u2014 like giving the LLM a searchable library of your papers.",
             font_size=12, color=MEDIUM_GRAY, italic=True)
add_p(tf, "Fine-tuning in plain English: You train the model\u2019s weights on your corpus so the knowledge is baked in. More powerful but more effort to update.",
      font_size=12, color=MEDIUM_GRAY, italic=True)
footer(slide, "Pasquinelli Lab AI Research Agent  \u2022  github.com/jlpfly/Karpathy_autoresearch  \u2022  Amy_Autoresearch branch")


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 13 — program.md Template
# ═══════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, DARK_BG)
add_rect(slide, 0, 0, 0.18, 7.5, ACCENT_TEAL)

add_box(slide, 0.5, 0.25, 12.0, 0.4,
        "THE RESEARCH STRATEGY FILE", font_size=11, color=ACCENT_TEAL, bold=True)
add_box(slide, 0.5, 0.55, 12.0, 0.7,
        "program.md is what makes this a Pasquinelli Lab agent, not a generic chatbot",
        font_size=27, color=WHITE, bold=True)
divider_line(slide, y=1.35, left=0.5, color=ACCENT_TEAL)

# Code block background
add_rect(slide, 0.5, 1.5, 7.5, 5.1, PANEL_BG)
template_lines = [
    ("You are a research assistant for the Pasquinelli Lab at UC San Diego.", WHITE),
    ("", WHITE),
    ("Your expertise covers:", ACCENT_TEAL),
    ("  \u2022 microRNA biology, biogenesis, and target regulation", LIGHT_GRAY),
    ("  \u2022 C. elegans genetics, aging, and stress response", LIGHT_GRAY),
    ("  \u2022 Poly(A) tail biology and translational regulation", LIGHT_GRAY),
    ("  \u2022 let-7 and small RNA regulatory mechanisms", LIGHT_GRAY),
    ("  \u2022 RNA processing and isoform regulation", LIGHT_GRAY),
    ("", WHITE),
    ("Your corpus includes all Pasquinelli lab publications", ACCENT_TEAL),
    ("from 2000 to 2025, plus key papers from the Bartel,", ACCENT_TEAL),
    ("Ambros, Richter, and Kaeberlein labs.", ACCENT_TEAL),
    ("", WHITE),
    ("For each task:", ACCENT_ORANGE),
    ("  1. Search the corpus for relevant evidence", LIGHT_GRAY),
    ("  2. Extract key claims with citations", LIGHT_GRAY),
    ("  3. Grade evidence: strong / moderate / weak / contested", LIGHT_GRAY),
    ("  4. Identify gaps and open questions", LIGHT_GRAY),
    ("  5. Output as structured tables and ranked lists", LIGHT_GRAY),
    ("", WHITE),
    ("Current focus: [INSERT CURRENT RESEARCH QUESTION]", GOLD),
]
tf = add_box(slide, 0.65, 1.6, 7.2, 4.8,
             template_lines[0][0], font_size=11, color=template_lines[0][1])
for line, col in template_lines[1:]:
    add_p(tf, line, font_size=11, color=col, space_before=1)

# Right side explanation
add_rect(slide, 8.3, 1.5, 4.7, 5.1, PANEL_BG)
add_box(slide, 8.45, 1.6, 4.4, 0.45,
        "Why this file matters", font_size=14, color=ACCENT_TEAL, bold=True)
tf2 = add_box(slide, 8.45, 2.15, 4.4, 4.3,
              "The program.md file is your research strategy. It tells the agent:",
              font_size=12, color=WHITE)
add_p(tf2, "", font_size=6, color=WHITE)
add_p(tf2, "\u2022 What domain it is working in", font_size=12, color=LIGHT_GRAY, space_before=5)
add_p(tf2, "\u2022 What corpus to draw from", font_size=12, color=LIGHT_GRAY, space_before=5)
add_p(tf2, "\u2022 How to format outputs", font_size=12, color=LIGHT_GRAY, space_before=5)
add_p(tf2, "\u2022 What the current research focus is", font_size=12, color=LIGHT_GRAY, space_before=5)
add_p(tf2, "", font_size=6, color=WHITE)
add_p(tf2, "Invest time in refining it. Each iteration makes the agent more useful.",
      font_size=12, color=GOLD, bold=True, space_before=8)
add_p(tf2, "", font_size=6, color=WHITE)
add_p(tf2, "Template available in:", font_size=11, color=MEDIUM_GRAY, space_before=8)
add_p(tf2, "amy_autoresearch_howto/", font_size=11, color=ACCENT_TEAL, space_before=3)
add_p(tf2, "Amy_Autoresearch branch", font_size=11, color=ACCENT_TEAL, space_before=3)

footer(slide, "Pasquinelli Lab AI Research Agent  \u2022  github.com/jlpfly/Karpathy_autoresearch  \u2022  Amy_Autoresearch branch")


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 14 — Quick Wins
# ═══════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, DARK_BG)
add_rect(slide, 0, 0, 0.18, 7.5, ACCENT_GREEN)

add_box(slide, 0.5, 0.25, 12.0, 0.4,
        "GETTING STARTED TODAY", font_size=11, color=ACCENT_GREEN, bold=True)
add_box(slide, 0.5, 0.55, 12.0, 0.7,
        "You can have a working lab LLM agent in 48 hours",
        font_size=27, color=WHITE, bold=True)
divider_line(slide, y=1.35, left=0.5, color=ACCENT_GREEN)

# Left: Quick wins
add_rect(slide, 0.5, 1.5, 5.9, 4.8, PANEL_BG)
add_box(slide, 0.65, 1.6, 5.6, 0.45,
        "This week (hours to days)", font_size=16, color=ACCENT_GREEN, bold=True)
quick_wins = [
    ("1.", "Literature gap-finder for next grant proposal", "1\u20132 days"),
    ("2.", "New-paper alert and summary service", "Half a day"),
    ("3.", "Manuscript consistency checker", "Hours per manuscript"),
    ("4.", "Hypothesis ranking board from a seed paper", "1\u20132 days"),
    ("5.", "Lab knowledge base for onboarding", "Ongoing, seed in hours"),
]
for i, (num, task, time) in enumerate(quick_wins):
    y = 2.15 + i * 0.82
    add_box(slide, 0.65, y, 0.35, 0.5, num, font_size=14, color=ACCENT_GREEN, bold=True)
    add_box(slide, 1.05, y, 4.1, 0.35, task, font_size=13, color=WHITE)
    add_box(slide, 1.05, y + 0.35, 4.1, 0.3, time, font_size=11, color=MEDIUM_GRAY, italic=True)

# Right: This month
add_rect(slide, 6.9, 1.5, 6.0, 4.8, PANEL_BG)
add_box(slide, 7.05, 1.6, 5.7, 0.45,
        "This month (days to weeks)", font_size=16, color=ACCENT_ORANGE, bold=True)
month_items = [
    ("1.", "Full corpus build: all lab papers + key field papers"),
    ("2.", "RAG-based query system: ask questions, get cited answers"),
    ("3.", "Isoform shift analysis on 2024 aging data"),
    ("4.", "Cross-dataset replication of aging signatures"),
    ("5.", "Living hypothesis board that updates as new papers appear"),
]
for i, (num, task) in enumerate(month_items):
    y = 2.15 + i * 0.82
    add_box(slide, 7.05, y, 0.35, 0.5, num, font_size=14, color=ACCENT_ORANGE, bold=True)
    add_box(slide, 7.45, y, 5.2, 0.55, task, font_size=13, color=WHITE)

add_rect(slide, 0.5, 6.4, 12.4, 0.55, PANEL_BG)
add_box(slide, 0.65, 6.45, 12.1, 0.45,
        "All how-to guides, starter code, and program.md templates: amy_autoresearch_howto/  \u2022  github.com/jlpfly/Karpathy_autoresearch",
        font_size=13, color=ACCENT_BLUE, alignment=PP_ALIGN.CENTER)
footer(slide, "Pasquinelli Lab AI Research Agent  \u2022  github.com/jlpfly/Karpathy_autoresearch  \u2022  Amy_Autoresearch branch")


# ═══════════════════════════════════════════════════════════════════════════
# SLIDE 15 — Closing
# ═══════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_slide_bg(slide, DARK_BG)
add_rect(slide, 0, 0, 0.18, 7.5, ACCENT_BLUE)
add_rect(slide, 0.18, 0, 0.06, 7.5, ACCENT_PURPLE)

add_box(slide, 0.5, 0.25, 12.0, 0.4,
        "CLOSING", font_size=11, color=ACCENT_BLUE, bold=True)
add_box(slide, 0.5, 0.55, 12.0, 0.75,
        "The Pasquinelli Lab is positioned to lead in AI-augmented RNA biology",
        font_size=28, color=WHITE, bold=True)
divider_line(slide, y=1.4, left=0.5, color=ACCENT_BLUE)

# Left: Why this lab
add_rect(slide, 0.5, 1.55, 5.9, 2.8, PANEL_BG)
add_box(slide, 0.65, 1.65, 5.6, 0.45,
        "Why this lab, why now", font_size=15, color=ACCENT_BLUE, bold=True)
tf = add_box(slide, 0.65, 2.15, 5.6, 2.1,
             "\u2022 25 years of publications = a rich, coherent training corpus",
             font_size=13, color=WHITE)
add_p(tf, "\u2022 Deep expertise in a focused domain = high-quality agent outputs", font_size=13, color=WHITE, space_before=5)
add_p(tf, "\u2022 Existing compute (RTX 3050 Ti) = no new hardware needed", font_size=13, color=WHITE, space_before=5)
add_p(tf, "\u2022 Active hiring in non-coding RNA = new members benefit immediately", font_size=13, color=WHITE, space_before=5)

# Right: What it amplifies
add_rect(slide, 6.9, 1.55, 6.0, 2.8, PANEL_BG)
add_box(slide, 7.05, 1.65, 5.7, 0.45,
        "What the agent amplifies", font_size=15, color=ACCENT_GREEN, bold=True)
tf2 = add_box(slide, 7.05, 2.15, 5.7, 2.1,
              "\u2022 Literature coverage: reads faster and more consistently than any human",
              font_size=13, color=WHITE)
add_p(tf2, "\u2022 Hypothesis generation: surfaces connections across hundreds of papers", font_size=13, color=WHITE, space_before=5)
add_p(tf2, "\u2022 Institutional memory: new lab members up to speed in days, not months", font_size=13, color=WHITE, space_before=5)
add_p(tf2, "\u2022 Grant preparation: structures evidence and identifies gaps systematically", font_size=13, color=WHITE, space_before=5)

# What it cannot replace
add_rect(slide, 0.5, 4.5, 12.4, 1.3, PANEL_BG)
add_box(slide, 0.65, 4.6, 12.0, 0.4,
        "What the agent cannot replace", font_size=14, color=ACCENT_ORANGE, bold=True)
tf3 = add_box(slide, 0.65, 5.05, 12.0, 0.65,
              "Experimental creativity and biological intuition  \u2022  Wet-lab execution and troubleshooting  "
              "\u2022  Peer relationships and collaboration  \u2022  The judgment to know which question matters",
              font_size=13, color=LIGHT_GRAY)

# Final quote
add_rect(slide, 0.5, 5.95, 12.4, 0.8, PANEL_BG)
add_box(slide, 0.65, 6.0, 12.0, 0.7,
        "\u201cThe era of AI-augmented biology is here. The Pasquinelli Lab has the corpus, the compute, "
        "and the questions. The only remaining step is to build the agent.\u201d",
        font_size=14, color=GOLD, bold=True, italic=True, alignment=PP_ALIGN.CENTER)

footer(slide, "github.com/jlpfly/Karpathy_autoresearch  \u2022  Branch: Amy_Autoresearch  \u2022  Pasquinelli Lab \u2022 UC San Diego")


# ── Save ─────────────────────────────────────────────────────────────────────
output_path = "Pasquinelli_AI_Agent_Pitch.pptx"
prs.save(output_path)
print(f"Saved: {output_path} ({len(prs.slides)} slides)")
