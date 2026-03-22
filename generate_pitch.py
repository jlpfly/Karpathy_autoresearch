"""
Pasquinelli Lab AI Research Agent — Steampunk AI Pitch Deck
Generates: Pasquinelli_AI_Agent_Pitch.pptx  (15 slides)

Theme: Deep teal-navy AI neural-network base + copper/brass steampunk
       gear decorations on every slide.  Fonts and spacing are calibrated
       for correct PowerPoint rendering (no clipping, no overflow).
"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from lxml import etree

# ── Asset paths ──────────────────────────────────────────────────────────────
ASSETS = os.path.join(os.path.dirname(__file__), "..", "steampunk_assets")
if not os.path.isdir(ASSETS):
    ASSETS = os.path.expanduser("~/steampunk_assets")

IMG_GEAR_TL  = os.path.join(ASSETS, "gear_corner_tl_t.png")
IMG_GEAR_BR  = os.path.join(ASSETS, "gear_corner_br_t.png")
IMG_GEAR_SM  = os.path.join(ASSETS, "gear_cluster_sm_t.png")
IMG_BORDER   = os.path.join(ASSETS, "border_strip.png")
IMG_DIVIDER  = os.path.join(ASSETS, "divider_ornament.png")
IMG_CLOCK    = os.path.join(ASSETS, "clockface_t.png")

# ── Slide dimensions ─────────────────────────────────────────────────────────
W = Inches(13.333)
H = Inches(7.5)

# ── Colour palette ────────────────────────────────────────────────────────────
DARK_BG       = RGBColor(0x08, 0x10, 0x18)   # near-black navy
PANEL_BG      = RGBColor(0x0E, 0x1A, 0x26)   # dark teal panel
PANEL_MID     = RGBColor(0x14, 0x24, 0x32)   # mid teal panel
BRASS         = RGBColor(0xC8, 0x79, 0x41)   # warm copper-brass
BRASS_LIGHT   = RGBColor(0xE8, 0xA8, 0x60)   # light brass highlight
BRASS_DARK    = RGBColor(0x7A, 0x42, 0x18)   # dark amber
ACCENT_BLUE   = RGBColor(0x00, 0xB4, 0xFF)   # electric cyan-blue
ACCENT_PURPLE = RGBColor(0x9B, 0x59, 0xB6)   # neural purple
ACCENT_GREEN  = RGBColor(0x00, 0xD4, 0x6A)   # bio green
ACCENT_TEAL   = RGBColor(0x1A, 0xBC, 0x9C)   # teal
ACCENT_ORANGE = RGBColor(0xFF, 0x8C, 0x00)   # amber highlight
WHITE         = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GRAY    = RGBColor(0xCC, 0xCC, 0xCC)
MEDIUM_GRAY   = RGBColor(0x88, 0x88, 0x99)
DARK_GRAY     = RGBColor(0x44, 0x44, 0x55)
GOLD          = RGBColor(0xF1, 0xC4, 0x0F)
RIVET_GOLD    = RGBColor(0xD4, 0xA0, 0x17)

# ── Presentation ─────────────────────────────────────────────────────────────
prs = Presentation()
prs.slide_width  = W
prs.slide_height = H


# ════════════════════════════════════════════════════════════════════════════
# HELPERS
# ════════════════════════════════════════════════════════════════════════════

def _rgb_hex(rgb: RGBColor) -> str:
    return f"{rgb[0]:02X}{rgb[1]:02X}{rgb[2]:02X}"


def set_bg(slide, color: RGBColor):
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_rect(slide, left, top, width, height, fill_color: RGBColor,
             line_color=None, line_width_pt=0):
    """Add a filled rectangle shape (in Inches)."""
    shape = slide.shapes.add_shape(
        1,
        Inches(left), Inches(top), Inches(width), Inches(height))
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    if line_color:
        shape.line.color.rgb = line_color
        shape.line.width = Pt(line_width_pt)
    else:
        shape.line.fill.background()
    return shape


def add_img(slide, path, left, top, width, height):
    """Add an image (in Inches). Skips silently if file missing."""
    if not os.path.isfile(path):
        return None
    return slide.shapes.add_picture(
        path,
        Inches(left), Inches(top), Inches(width), Inches(height))


def _set_para(para, text, size_pt, color: RGBColor,
              bold=False, italic=False,
              align=PP_ALIGN.LEFT, space_before_pt=0, space_after_pt=0,
              line_spacing_pt=None):
    para.clear()
    para.alignment = align
    pPr = para._pPr
    if pPr is None:
        pPr = para._p.get_or_add_pPr()
    if space_before_pt:
        pPr.set(qn("a:spcBef"), "")
        spcBef = etree.SubElement(pPr, qn("a:spcBef"))
        spcPts = etree.SubElement(spcBef, qn("a:spcPts"))
        spcPts.set("val", str(int(space_before_pt * 100)))
    if space_after_pt:
        spcAft = etree.SubElement(pPr, qn("a:spcAft"))
        spcPts2 = etree.SubElement(spcAft, qn("a:spcPts"))
        spcPts2.set("val", str(int(space_after_pt * 100)))
    if line_spacing_pt:
        lnSpc = etree.SubElement(pPr, qn("a:lnSpc"))
        spcPts3 = etree.SubElement(lnSpc, qn("a:spcPts"))
        spcPts3.set("val", str(int(line_spacing_pt * 100)))
    run = para.add_run()
    run.text = text
    run.font.size = Pt(size_pt)
    run.font.color.rgb = color
    run.font.bold = bold
    run.font.italic = italic
    return para


def add_textbox(slide, left, top, width, height,
                text, size_pt, color: RGBColor,
                bold=False, italic=False,
                align=PP_ALIGN.LEFT,
                wrap=True, auto_size=False):
    """Add a single-paragraph textbox (in Inches)."""
    txBox = slide.shapes.add_textbox(
        Inches(left), Inches(top), Inches(width), Inches(height))
    tf = txBox.text_frame
    tf.word_wrap = wrap
    _set_para(tf.paragraphs[0], text, size_pt, color,
              bold=bold, italic=italic, align=align)
    return tf


def add_para(tf, text, size_pt, color: RGBColor,
             bold=False, italic=False,
             align=PP_ALIGN.LEFT, space_before_pt=4):
    """Append a paragraph to an existing text frame."""
    p = tf.add_paragraph()
    _set_para(p, text, size_pt, color,
              bold=bold, italic=italic, align=align,
              space_before_pt=space_before_pt)
    return p


# ── Steampunk chrome helpers ──────────────────────────────────────────────────

def brass_border(slide, thickness=0.06):
    """Thin brass outer border around the entire slide."""
    add_rect(slide, 0, 0, 13.333, thickness, BRASS)          # top
    add_rect(slide, 0, 7.5 - thickness, 13.333, thickness, BRASS)  # bottom
    add_rect(slide, 0, 0, thickness, 7.5, BRASS)              # left
    add_rect(slide, 13.333 - thickness, 0, thickness, 7.5, BRASS)  # right


def gear_corners(slide, size=1.55, alpha_tl=True, alpha_br=True):
    """Place gear corner images at TL and BR with low opacity feel via sizing."""
    if alpha_tl:
        add_img(slide, IMG_GEAR_TL, -0.1, -0.1, size, size)
    if alpha_br:
        add_img(slide, IMG_GEAR_BR,
                13.333 - size + 0.1, 7.5 - size + 0.1, size, size)


def bottom_border_strip(slide, height=0.38):
    """Place the ornate border strip at the bottom of the slide."""
    add_img(slide, IMG_BORDER, 0, 7.5 - height, 13.333, height)


def top_border_strip(slide, height=0.28):
    """Place a thin border strip at the top."""
    add_img(slide, IMG_BORDER, 0, 0, 13.333, height)


def steampunk_divider(slide, y, width=10.5, left=1.4, h=0.28):
    """Place the ornamental divider at y (Inches from top)."""
    add_img(slide, IMG_DIVIDER, left, y, width, h)


def rivet_row(slide, y, count=14, color=BRASS):
    """Draw a row of small rivet dots across the slide."""
    spacing = 13.333 / (count + 1)
    for i in range(count):
        x = spacing * (i + 1) - 0.06
        shape = slide.shapes.add_shape(
            9,  # oval
            Inches(x), Inches(y), Inches(0.12), Inches(0.12))
        shape.fill.solid()
        shape.fill.fore_color.rgb = color
        shape.line.fill.background()


def section_label(slide, text, x, y, color=BRASS_LIGHT):
    """Small all-caps section label."""
    add_textbox(slide, x, y, 12.0, 0.32, text,
                size_pt=9.5, color=color, bold=True, align=PP_ALIGN.LEFT)


def slide_footer(slide, text):
    """Consistent footer line just above the bottom border."""
    add_textbox(slide, 0.5, 7.05, 12.3, 0.28, text,
                size_pt=9, color=MEDIUM_GRAY, align=PP_ALIGN.CENTER)


def panel_box(slide, left, top, width, height,
              fill=PANEL_BG, line_color=BRASS_DARK, line_pt=0.75):
    """Steampunk panel: dark fill with thin brass border."""
    shape = add_rect(slide, left, top, width, height, fill,
                     line_color=line_color, line_width_pt=line_pt)
    return shape


def accent_bar(slide, left, top, height, color=BRASS, width=0.14):
    """Vertical accent bar (steampunk column)."""
    add_rect(slide, left, top, width, height, color)


def heading(slide, label, title, label_color=BRASS_LIGHT,
            title_color=WHITE, label_y=0.22, title_y=0.52,
            title_size=26):
    """Standard slide heading: small label + large title."""
    add_textbox(slide, 0.55, label_y, 12.0, 0.32,
                label, size_pt=9.5, color=label_color, bold=True)
    add_textbox(slide, 0.55, title_y, 12.0, 0.65,
                title, size_pt=title_size, color=title_color, bold=True)


FOOTER_TEXT = (
    "Pasquinelli Lab AI Research Agent  \u2022  "
    "github.com/jlpfly/Karpathy_autoresearch  \u2022  Amy_Autoresearch branch"
)


# ════════════════════════════════════════════════════════════════════════════
# SLIDE 1 — Title
# ════════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide, DARK_BG)

# Steampunk chrome
top_border_strip(slide, height=0.22)
bottom_border_strip(slide, height=0.38)
gear_corners(slide, size=2.2)
rivet_row(slide, y=0.26, count=16, color=BRASS_DARK)
rivet_row(slide, y=7.1, count=16, color=BRASS_DARK)

# Vertical brass accent bars
accent_bar(slide, 0.22, 0.22, 6.88, color=BRASS, width=0.14)
accent_bar(slide, 0.36, 0.22, 6.88, color=BRASS_DARK, width=0.05)

# Clock face (ghosted, right side)
add_img(slide, IMG_CLOCK, 9.5, 0.9, 3.5, 3.5)
# Overlay to dim the clock
add_rect(slide, 9.5, 0.9, 3.5, 3.5, DARK_BG)
# Re-add at reduced visual weight via a semi-transparent-feel overlay
add_img(slide, IMG_CLOCK, 9.6, 1.0, 3.2, 3.2)

# Content
add_textbox(slide, 0.6, 0.35, 12.0, 0.38,
            "PASQUINELLI LAB  \u00b7  UC SAN DIEGO  \u00b7  DEPARTMENT OF MOLECULAR BIOLOGY",
            size_pt=10, color=BRASS_LIGHT, bold=True)

add_textbox(slide, 0.6, 0.9, 8.5, 1.6,
            "Your Lab\u2019s Own LLM:",
            size_pt=48, color=WHITE, bold=True)

add_textbox(slide, 0.6, 2.4, 8.5, 0.85,
            "An AI Research Agent for miRNA Biology,\nAging & RNA Processing",
            size_pt=22, color=BRASS_LIGHT, bold=False)

steampunk_divider(slide, y=3.38, left=0.6, width=8.0, h=0.26)

tf = add_textbox(slide, 0.6, 3.72, 8.5, 0.42,
                 "Built on Karpathy\u2019s autoresearch framework  \u2022  Amy_Autoresearch branch",
                 size_pt=13, color=LIGHT_GRAY)
add_para(tf, "github.com/jlpfly/Karpathy_autoresearch  \u2022  Dell XPS 15 (RTX 3050 Ti)",
         size_pt=12, color=MEDIUM_GRAY, space_before_pt=3)
add_para(tf, "Training corpus: 25 years of Pasquinelli lab publications + the full miRNA field",
         size_pt=12, color=MEDIUM_GRAY, space_before_pt=3)

# Small gear cluster bottom-left content area
add_img(slide, IMG_GEAR_SM, 0.55, 5.5, 0.9, 0.9)
add_textbox(slide, 1.55, 5.6, 10.5, 0.38,
            "Autoresearch  \u2022  RAG  \u2022  Fine-Tuning  \u2022  Autonomous Agent Loop  \u2022  miRNA Biology  \u2022  C. elegans Aging",
            size_pt=11, color=BRASS_DARK)

slide_footer(slide, FOOTER_TEXT)
brass_border(slide)


# ════════════════════════════════════════════════════════════════════════════
# SLIDE 2 — The Vision
# ════════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide, DARK_BG)
top_border_strip(slide, height=0.22)
bottom_border_strip(slide, height=0.38)
gear_corners(slide, size=1.6)
rivet_row(slide, y=0.26, count=16, color=BRASS_DARK)
accent_bar(slide, 0.22, 0.22, 7.0, color=ACCENT_PURPLE, width=0.14)

heading(slide,
        "THE VISION",
        "Imagine an AI that has read every paper your lab has ever published",
        label_color=BRASS_LIGHT, title_color=WHITE, title_size=24)

steampunk_divider(slide, y=1.28, left=0.5, width=12.3, h=0.24)

# Left panel
panel_box(slide, 0.5, 1.6, 5.9, 4.7)
add_textbox(slide, 0.68, 1.72, 5.5, 0.38,
            "What this LLM knows", size_pt=15, color=BRASS_LIGHT, bold=True)
tf = add_textbox(slide, 0.68, 2.18, 5.5, 3.9,
                 "\u2022  Every Pasquinelli lab paper from let-7 (2000) through the 2024 aging RNA-seq study",
                 size_pt=12.5, color=WHITE)
add_para(tf, "\u2022  Full miRNA field: TargetScan, miRDB, AGO biology, CLIP/CLASH datasets",
         size_pt=12.5, color=WHITE, space_before_pt=5)
add_para(tf, "\u2022  C. elegans aging literature, heat-shock recovery, poly(A) tail biology",
         size_pt=12.5, color=WHITE, space_before_pt=5)
add_para(tf, "\u2022  Unpublished datasets, protocols, and experimental notes (optional)",
         size_pt=12.5, color=WHITE, space_before_pt=5)

# Right panel
panel_box(slide, 6.9, 1.6, 6.0, 4.7)
add_textbox(slide, 7.08, 1.72, 5.7, 0.38,
            "What this means for the lab", size_pt=15, color=ACCENT_GREEN, bold=True)
tf2 = add_textbox(slide, 7.08, 2.18, 5.7, 3.9,
                  "\u201cWhat are the strongest open questions in let-7 biology right now?\u201d",
                  size_pt=12, color=ACCENT_BLUE, italic=True)
add_para(tf2, "   \u2192 Amy, strategic planning", size_pt=11, color=MEDIUM_GRAY, space_before_pt=2)
add_para(tf2, " ", size_pt=5, color=WHITE, space_before_pt=2)
add_para(tf2, "\u201cDesign a follow-up experiment for our miR-238 longevity finding.\u201d",
         size_pt=12, color=ACCENT_BLUE, italic=True, space_before_pt=5)
add_para(tf2, "   \u2192 Postdoc, experimental design", size_pt=11, color=MEDIUM_GRAY, space_before_pt=2)
add_para(tf2, " ", size_pt=5, color=WHITE, space_before_pt=2)
add_para(tf2, "\u201cExplain the ALG-1 vs ALG-2 aging phenotype to me.\u201d",
         size_pt=12, color=ACCENT_BLUE, italic=True, space_before_pt=5)
add_para(tf2, "   \u2192 Rotation student, onboarding", size_pt=11, color=MEDIUM_GRAY, space_before_pt=2)
add_para(tf2, " ", size_pt=5, color=WHITE, space_before_pt=2)
add_para(tf2, "\u201cWhat gaps in the aging-miRNA field should our R01 address?\u201d",
         size_pt=12, color=ACCENT_BLUE, italic=True, space_before_pt=5)
add_para(tf2, "   \u2192 Grant writing, Significance section", size_pt=11, color=MEDIUM_GRAY, space_before_pt=2)

# Gear cluster between panels
add_img(slide, IMG_GEAR_SM, 6.1, 2.8, 0.7, 0.7)

panel_box(slide, 0.5, 6.38, 12.4, 0.52, fill=PANEL_MID)
add_textbox(slide, 0.65, 6.44, 12.1, 0.38,
            "This is not a generic chatbot. It is trained specifically on the body of work most relevant to your research program.",
            size_pt=12, color=GOLD, bold=True, align=PP_ALIGN.CENTER)

slide_footer(slide, FOOTER_TEXT)
brass_border(slide)


# ════════════════════════════════════════════════════════════════════════════
# SLIDE 3 — Architecture
# ════════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide, DARK_BG)
top_border_strip(slide, height=0.22)
bottom_border_strip(slide, height=0.38)
gear_corners(slide, size=1.6)
rivet_row(slide, y=0.26, count=16, color=BRASS_DARK)
accent_bar(slide, 0.22, 0.22, 7.0, color=ACCENT_TEAL, width=0.14)

heading(slide,
        "ARCHITECTURE",
        "Three layers make this agent work: Corpus  \u2022  Model  \u2022  Agent Loop",
        label_color=BRASS_LIGHT, title_color=WHITE, title_size=24)

steampunk_divider(slide, y=1.28, left=0.5, width=12.3, h=0.24)

layer_data = [
    ("LAYER 1", "The Corpus", "What it reads",
     ["\u2022 All Pasquinelli lab papers (2000\u20132025): ~55 papers",
      "\u2022 Field-defining papers: Bartel, Ambros, Tuschl labs",
      "\u2022 PubMed abstracts, PMC full text, GEO metadata",
      "\u2022 Lab protocols, grant aims, meeting notes (optional)"],
     ACCENT_TEAL),
    ("LAYER 2", "The Model", "How it learns",
     ["\u2022 Base: Llama 3, Mistral, or GPT-4 via API",
      "\u2022 Method: RAG or supervised fine-tuning on corpus",
      "\u2022 Hardware: RTX 3050 Ti (already in the lab)",
      "\u2022 Time to first version: 1\u20132 days setup + overnight"],
     ACCENT_PURPLE),
    ("LAYER 3", "The Agent Loop", "How it acts",
     ["\u2022 Reads program.md (your research strategy)",
      "\u2022 Iterates: reads \u2192 extracts \u2192 hypothesizes \u2192 ranks",
      "\u2022 Outputs: tables, hypothesis boards, reading queues",
      "\u2022 Human stays in control: review, redirect, refine"],
     ACCENT_GREEN),
]

col_w = 3.9
for i, (num, title, sub, bullets, col) in enumerate(layer_data):
    x = 0.5 + i * (col_w + 0.22)
    panel_box(slide, x, 1.6, col_w, 5.0)
    # Gear image in top of each panel
    add_img(slide, IMG_GEAR_SM, x + col_w - 0.9, 1.65, 0.75, 0.75)
    add_textbox(slide, x + 0.18, 1.68, col_w - 1.0, 0.34,
                num, size_pt=10, color=col, bold=True)
    add_textbox(slide, x + 0.18, 2.05, col_w - 0.3, 0.44,
                title, size_pt=18, color=WHITE, bold=True)
    add_textbox(slide, x + 0.18, 2.54, col_w - 0.3, 0.3,
                sub, size_pt=11, color=MEDIUM_GRAY)
    # Thin brass rule
    add_rect(slide, x + 0.18, 2.9, col_w - 0.36, 0.02, BRASS_DARK)
    tf = add_textbox(slide, x + 0.18, 3.0, col_w - 0.3, 3.4,
                     bullets[0], size_pt=12, color=WHITE)
    for b in bullets[1:]:
        add_para(tf, b, size_pt=12, color=WHITE, space_before_pt=5)

slide_footer(slide, FOOTER_TEXT)
brass_border(slide)


# ════════════════════════════════════════════════════════════════════════════
# SLIDE 4 — How to Build It
# ════════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide, DARK_BG)
top_border_strip(slide, height=0.22)
bottom_border_strip(slide, height=0.38)
gear_corners(slide, size=1.6)
rivet_row(slide, y=0.26, count=16, color=BRASS_DARK)
accent_bar(slide, 0.22, 0.22, 7.0, color=ACCENT_GREEN, width=0.14)

heading(slide,
        "HOW TO BUILD IT",
        "Building the Pasquinelli Lab LLM takes one weekend, not one year",
        label_color=BRASS_LIGHT, title_color=WHITE, title_size=24)

steampunk_divider(slide, y=1.28, left=0.5, width=12.3, h=0.24)

steps = [
    ("01", ACCENT_BLUE,
     "Set up the environment",
     "Day 1  \u00b7  ~2 hours",
     "git clone https://github.com/jlpfly/\nKarpathy_autoresearch\n"
     "git checkout Amy_Autoresearch\n"
     "uv python install 3.11\nuv sync\nuv run prepare.py\n\n"
     "Hardware: Dell XPS 15 with RTX 3050 Ti\n\u2014 already validated"),
    ("02", ACCENT_PURPLE,
     "Build the corpus",
     "Day 1  \u00b7  ~3 hours",
     "Export PDFs of all Pasquinelli lab\npapers from PubMed/PMC\n\n"
     "Add key field papers (Bartel, Ambros,\nlet-7 foundational work)\n\n"
     "pdftotext paper.pdf paper.txt\n\nPlace in corpus/ directory"),
    ("03", ACCENT_TEAL,
     "Configure the agent",
     "Day 1  \u00b7  ~1 hour",
     "Edit program.md to define the\nagent\u2019s role\n\n"
     "Set focus: \u201cYou are a research\nassistant for the Pasquinelli Lab\u2026\u201d\n\n"
     "Define output format: tables,\nranked lists, hypothesis boards"),
    ("04", ACCENT_ORANGE,
     "Run overnight",
     "Day 2",
     "uv run train.py\n# 5-minute baseline validation\n\n"
     "Launch Claude/Codex with\nprogram.md \u2014 let it iterate\n\n"
     "Wake up to a log of experiments\nand structured outputs"),
    ("05", ACCENT_GREEN,
     "Query and iterate",
     "Ongoing",
     "Start asking questions\n(see example prompt slides)\n\n"
     "Refine program.md based on\noutput quality\n\n"
     "Add new papers as they\nare published"),
]

col_w = 2.38
for i, (num, col, title, sub, body) in enumerate(steps):
    x = 0.5 + i * (col_w + 0.12)
    panel_box(slide, x, 1.6, col_w, 5.1)
    add_textbox(slide, x + 0.14, 1.68, 0.7, 0.5,
                num, size_pt=22, color=col, bold=True)
    add_img(slide, IMG_GEAR_SM, x + col_w - 0.72, 1.65, 0.62, 0.62)
    add_textbox(slide, x + 0.14, 2.22, col_w - 0.28, 0.38,
                title, size_pt=12.5, color=WHITE, bold=True)
    add_textbox(slide, x + 0.14, 2.62, col_w - 0.28, 0.28,
                sub, size_pt=10, color=BRASS_LIGHT)
    add_rect(slide, x + 0.14, 2.95, col_w - 0.28, 0.02, BRASS_DARK)
    add_textbox(slide, x + 0.14, 3.04, col_w - 0.28, 3.5,
                body, size_pt=10.5, color=LIGHT_GRAY, wrap=True)

slide_footer(slide, FOOTER_TEXT)
brass_border(slide)


# ════════════════════════════════════════════════════════════════════════════
# SLIDE 5 — The Corpus
# ════════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide, DARK_BG)
top_border_strip(slide, height=0.22)
bottom_border_strip(slide, height=0.38)
gear_corners(slide, size=1.6)
rivet_row(slide, y=0.26, count=16, color=BRASS_DARK)
accent_bar(slide, 0.22, 0.22, 7.0, color=ACCENT_ORANGE, width=0.14)

heading(slide,
        "THE CORPUS",
        "The quality of the corpus determines the quality of the intelligence",
        label_color=BRASS_LIGHT, title_color=WHITE, title_size=24)

steampunk_divider(slide, y=1.28, left=0.5, width=12.3, h=0.24)

# Table header
add_rect(slide, 0.5, 1.6, 12.4, 0.42, BRASS_DARK)
add_rect(slide, 0.5, 1.6, 12.4, 0.02, BRASS)
add_rect(slide, 0.5, 2.02, 12.4, 0.02, BRASS)
hdr = [("Layer", 0.6, 1.65), ("Content", 2.35, 1.65),
       ("Papers / Items", 5.9, 1.65), ("Priority", 7.85, 1.65)]
for label, x, y in hdr:
    add_textbox(slide, x, y, 1.9, 0.34, label,
                size_pt=11.5, color=BRASS_LIGHT, bold=True)

rows = [
    ("Core Lab",         "All Pasquinelli lab publications 2000\u20132025",         "~55 papers",  "Essential",  ACCENT_GREEN),
    ("Field Foundation", "Bartel, Ambros, Tuschl landmark miRNA papers",            "~30 papers",  "Essential",  ACCENT_GREEN),
    ("Aging & C. elegans","Kaeberlein, Murphy, Curran aging papers",                "~20 papers",  "High",       ACCENT_BLUE),
    ("Poly(A) & Translation","Richter, Gilbert, Wickens PABP/translation papers",   "~15 papers",  "High",       ACCENT_BLUE),
    ("Databases",        "TargetScan, miRDB, CLIP-seq datasets (metadata)",         "~5 sources",  "Medium",     ACCENT_TEAL),
    ("Lab Materials",    "Protocols, grant aims, meeting notes",                    "Variable",    "Optional",   MEDIUM_GRAY),
]

for r, (layer, content, count, priority, col) in enumerate(rows):
    y = 2.1 + r * 0.56
    bg = PANEL_BG if r % 2 == 0 else PANEL_MID
    add_rect(slide, 0.5, y, 12.4, 0.54, bg)
    add_rect(slide, 0.5, y + 0.54, 12.4, 0.01, BRASS_DARK)
    add_textbox(slide, 0.6, y + 0.06, 1.7, 0.38, layer,
                size_pt=11.5, color=col, bold=True)
    add_textbox(slide, 2.35, y + 0.06, 3.5, 0.38, content,
                size_pt=11.5, color=WHITE)
    add_textbox(slide, 5.9, y + 0.06, 1.9, 0.38, count,
                size_pt=11.5, color=LIGHT_GRAY, align=PP_ALIGN.CENTER)
    add_textbox(slide, 7.85, y + 0.06, 1.8, 0.38, priority,
                size_pt=11.5, color=col, bold=True, align=PP_ALIGN.CENTER)

add_textbox(slide, 0.5, 5.5, 12.4, 0.42,
            "Key principle: Start with the lab\u2019s own papers. The agent will already be more useful than a generic LLM after just this first layer.",
            size_pt=12, color=GOLD, bold=True, align=PP_ALIGN.CENTER)
add_textbox(slide, 0.5, 5.96, 12.4, 0.32,
            "Sources: PubMed Central (pmc.ncbi.nlm.nih.gov)  \u2022  Semantic Scholar API  \u2022  bioRxiv preprints",
            size_pt=11, color=MEDIUM_GRAY, align=PP_ALIGN.CENTER)

slide_footer(slide, FOOTER_TEXT)
brass_border(slide)


# ════════════════════════════════════════════════════════════════════════════
# SLIDE 6 — Example Prompts: Amy (PI)
# ════════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide, DARK_BG)
top_border_strip(slide, height=0.22)
bottom_border_strip(slide, height=0.38)
gear_corners(slide, size=1.6)
rivet_row(slide, y=0.26, count=16, color=BRASS_DARK)
accent_bar(slide, 0.22, 0.22, 7.0, color=ACCENT_BLUE, width=0.14)

heading(slide,
        "EXAMPLE PROMPTS \u2014 AMY PASQUINELLI (PI)",
        "Strategic questions that used to take days to answer",
        label_color=BRASS_LIGHT, title_color=WHITE, title_size=24)

steampunk_divider(slide, y=1.28, left=0.5, width=12.3, h=0.24)

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
    y = 1.6 + i * 1.22
    panel_box(slide, 0.5, y, 12.4, 1.14)
    # Small gear
    add_img(slide, IMG_GEAR_SM, 12.05, y + 0.04, 0.42, 0.42)
    add_textbox(slide, 0.65, y + 0.06, 2.2, 0.3,
                label, size_pt=10.5, color=BRASS_LIGHT, bold=True)
    add_textbox(slide, 0.65, y + 0.36, 11.3, 0.42,
                prompt, size_pt=11.5, color=ACCENT_BLUE, italic=True)
    add_textbox(slide, 0.65, y + 0.78, 11.3, 0.3,
                f"\u2192 Output: {output}", size_pt=10.5, color=LIGHT_GRAY)

slide_footer(slide, FOOTER_TEXT)
brass_border(slide)


# ════════════════════════════════════════════════════════════════════════════
# SLIDE 7 — Example Prompts: Postdocs
# ════════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide, DARK_BG)
top_border_strip(slide, height=0.22)
bottom_border_strip(slide, height=0.38)
gear_corners(slide, size=1.6)
rivet_row(slide, y=0.26, count=16, color=BRASS_DARK)
accent_bar(slide, 0.22, 0.22, 7.0, color=ACCENT_GREEN, width=0.14)

heading(slide,
        "EXAMPLE PROMPTS \u2014 POSTDOCS & GRADUATE STUDENTS",
        "Daily research acceleration for every lab member",
        label_color=BRASS_LIGHT, title_color=WHITE, title_size=24)

steampunk_divider(slide, y=1.28, left=0.5, width=12.3, h=0.24)

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
    panel_box(slide, x, 1.6, col_w, 5.1)
    add_img(slide, IMG_GEAR_SM, x + col_w - 0.62, 1.64, 0.52, 0.52)
    add_textbox(slide, x + 0.12, 1.68, col_w - 0.7, 0.36,
                label, size_pt=11, color=ACCENT_GREEN, bold=True)
    add_textbox(slide, x + 0.12, 2.1, col_w - 0.24, 2.5,
                prompt, size_pt=10.5, color=ACCENT_BLUE, italic=True, wrap=True)
    add_rect(slide, x + 0.12, 4.65, col_w - 0.24, 0.02, BRASS_DARK)
    add_textbox(slide, x + 0.12, 4.72, col_w - 0.24, 1.72,
                f"Output:\n{output}", size_pt=10, color=LIGHT_GRAY, wrap=True)

slide_footer(slide, FOOTER_TEXT)
brass_border(slide)


# ════════════════════════════════════════════════════════════════════════════
# SLIDE 8 — Overnight Autonomous Research
# ════════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide, DARK_BG)
top_border_strip(slide, height=0.22)
bottom_border_strip(slide, height=0.38)
gear_corners(slide, size=1.6)
rivet_row(slide, y=0.26, count=16, color=BRASS_DARK)
accent_bar(slide, 0.22, 0.22, 7.0, color=ACCENT_PURPLE, width=0.14)

heading(slide,
        "OVERNIGHT AUTONOMOUS RESEARCH",
        "Let the agent work while you sleep \u2014 wake up to structured results",
        label_color=BRASS_LIGHT, title_color=WHITE, title_size=24)

steampunk_divider(slide, y=1.28, left=0.5, width=12.3, h=0.24)

# Clock image (right side, ghosted)
add_img(slide, IMG_CLOCK, 11.2, 1.5, 1.9, 1.9)

overnight = [
    ("Task 1: Literature sweep",
     "\u201cSearch for all papers published in the last 6 months on miRNA regulation in aging organisms. "
     "Summarize each, score relevance to our lab\u2019s work (1\u201310), and flag any that contradict our published findings.\u201d",
     "Ranked paper list  \u2022  Relevance scores  \u2022  Contradiction flags"),
    ("Task 2: Cross-dataset replication",
     "\u201cDownload all public C. elegans aging RNA-seq datasets from GEO. Score each using the gene signatures "
     "from our 2024 NAR paper. Report which signatures replicate and which do not.\u201d",
     "Replication score table  \u2022  Forest plots  \u2022  Core aging marker gene set"),
    ("Task 3: Target concordance",
     "\u201cFor let-7 and miR-238, pull predictions from TargetScan and miRDB. Cross-reference against our "
     "published functional data. Build a concordance score for each predicted target.\u201d",
     "Concordance-scored target table  \u2022  Venn diagrams  \u2022  High-confidence target shortlist"),
    ("Task 4: Hypothesis generation",
     "\u201cStarting from our 2021 heat-shock recovery paper, find all related papers on miRNA-mediated stress "
     "recovery. Generate 10 testable hypotheses ranked by evidence strength and experimental feasibility.\u201d",
     "Ranked hypothesis board  \u2022  Citations  \u2022  Experimental sketches"),
]

for i, (label, prompt, output) in enumerate(overnight):
    y = 1.6 + i * 1.22
    panel_box(slide, 0.5, y, 12.4, 1.14)
    add_img(slide, IMG_GEAR_SM, 12.05, y + 0.04, 0.42, 0.42)
    add_textbox(slide, 0.65, y + 0.06, 3.0, 0.3,
                label, size_pt=10.5, color=ACCENT_PURPLE, bold=True)
    add_textbox(slide, 0.65, y + 0.36, 11.3, 0.42,
                prompt, size_pt=11.5, color=ACCENT_BLUE, italic=True)
    add_textbox(slide, 0.65, y + 0.78, 11.3, 0.3,
                f"\u2192 By morning: {output}", size_pt=10.5, color=ACCENT_GREEN)

slide_footer(slide, FOOTER_TEXT)
brass_border(slide)


# ════════════════════════════════════════════════════════════════════════════
# SLIDE 9 — 5 Computational Applications
# ════════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide, DARK_BG)
top_border_strip(slide, height=0.22)
bottom_border_strip(slide, height=0.38)
gear_corners(slide, size=1.6)
rivet_row(slide, y=0.26, count=16, color=BRASS_DARK)
accent_bar(slide, 0.22, 0.22, 7.0, color=ACCENT_TEAL, width=0.14)

heading(slide,
        "5 IMPACTFUL COMPUTATIONAL APPLICATIONS",
        "Five experiments the agent can run on real datasets \u2014 not just literature",
        label_color=BRASS_LIGHT, title_color=WHITE, title_size=24)

steampunk_divider(slide, y=1.28, left=0.5, width=12.3, h=0.24)

apps = [
    ("01", "Age-Dependent Isoform Shift Quantification",
     "Reanalyzes 2024 direct RNA-seq aging data to build age-stratified isoform usage matrix.",
     "2024 NAR aging direct RNA-seq\n(PMC11662692)",
     "Ranked switching gene list\nAge-group heatmaps\nGO enrichment"),
    ("02", "Cross-Dataset miRNA Target Concordance",
     "Integrates TargetScan, miRDB, and CLIP/CLASH; cross-references against lab functional data.",
     "2023 miR-238/239ab paper\n(PLoS Genetics)",
     "Concordance-scored target table\nVenn diagrams\nTop 20 targets per miRNA"),
    ("03", "Poly(A)-Tail & Translation Efficiency Integration",
     "Correlates poly(A)-tail length with translational output; identifies outlier transcripts.",
     "2022 NAR PABP paper\n(PMC9071453)",
     "Tail length vs. TE scatter plots\nOutlier transcript lists\nGO enrichment"),
    ("04", "Stress-Recovery Time-Series Gene Module Detection",
     "Clusters genes into co-regulated modules from heat-shock recovery dynamics; maps miRNA targets.",
     "2021 PLoS Genetics heat-shock\n(PMC8370650)",
     "Temporal profile plots\nmiRNA-module enrichment scores\nNetwork visualizations"),
    ("05", "Automated Cross-Dataset Replication",
     "Downloads public C. elegans aging RNA-seq datasets from GEO; scores each with lab-derived signatures.",
     "2024 NAR aging direct RNA-seq\n(PMC11662692)",
     "Replication score table\nForest plots\nCore aging marker gene set"),
]

col_w = 2.38
for i, (num, title, does, anchor, outputs) in enumerate(apps):
    x = 0.5 + i * (col_w + 0.1)
    panel_box(slide, x, 1.6, col_w, 5.1)
    add_textbox(slide, x + 0.12, 1.66, 0.7, 0.44,
                num, size_pt=20, color=ACCENT_TEAL, bold=True)
    add_img(slide, IMG_GEAR_SM, x + col_w - 0.62, 1.64, 0.52, 0.52)
    add_textbox(slide, x + 0.12, 2.14, col_w - 0.24, 0.6,
                title, size_pt=11, color=WHITE, bold=True, wrap=True)
    add_textbox(slide, x + 0.12, 2.8, col_w - 0.24, 1.2,
                does, size_pt=10.5, color=LIGHT_GRAY, wrap=True)
    add_textbox(slide, x + 0.12, 4.06, col_w - 0.24, 0.28,
                "Anchor:", size_pt=9.5, color=MEDIUM_GRAY, bold=True)
    add_textbox(slide, x + 0.12, 4.36, col_w - 0.24, 0.42,
                anchor, size_pt=9.5, color=MEDIUM_GRAY, wrap=True)
    add_textbox(slide, x + 0.12, 4.84, col_w - 0.24, 0.28,
                "Outputs:", size_pt=9.5, color=ACCENT_GREEN, bold=True)
    add_textbox(slide, x + 0.12, 5.14, col_w - 0.24, 1.3,
                outputs, size_pt=9.5, color=LIGHT_GRAY, wrap=True)

slide_footer(slide, FOOTER_TEXT)
brass_border(slide)


# ════════════════════════════════════════════════════════════════════════════
# SLIDE 10 — Evidence Network
# ════════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide, DARK_BG)
top_border_strip(slide, height=0.22)
bottom_border_strip(slide, height=0.38)
gear_corners(slide, size=1.6)
rivet_row(slide, y=0.26, count=16, color=BRASS_DARK)
accent_bar(slide, 0.22, 0.22, 7.0, color=ACCENT_BLUE, width=0.14)

heading(slide,
        "THE EVIDENCE NETWORK",
        "Each experiment feeds the next \u2014 a self-reinforcing evidence network",
        label_color=BRASS_LIGHT, title_color=WHITE, title_size=24)

steampunk_divider(slide, y=1.28, left=0.5, width=12.3, h=0.24)

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
    y = 1.6 + i * 0.98
    panel_box(slide, 0.5, y, 12.4, 0.88)
    # Gear between each row
    add_img(slide, IMG_GEAR_SM, 12.1, y + 0.08, 0.66, 0.66)
    add_textbox(slide, 0.65, y + 0.1, 2.8, 0.38,
                title, size_pt=15, color=col, bold=True)
    add_textbox(slide, 3.55, y + 0.1, 6.5, 0.38,
                desc, size_pt=13, color=LIGHT_GRAY)
    add_textbox(slide, 10.1, y + 0.1, 2.7, 0.38,
                anchor, size_pt=10.5, color=MEDIUM_GRAY, italic=True)

panel_box(slide, 0.5, 6.55, 12.4, 0.44, fill=PANEL_MID)
add_textbox(slide, 0.65, 6.6, 12.1, 0.36,
            "Running all five creates a compounding evidence network. The agent can run all five overnight and synthesize the results by morning.",
            size_pt=12, color=GOLD, bold=True, align=PP_ALIGN.CENTER)

slide_footer(slide, FOOTER_TEXT)
brass_border(slide)


# ════════════════════════════════════════════════════════════════════════════
# SLIDE 11 — The Field Is Moving
# ════════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide, DARK_BG)
top_border_strip(slide, height=0.22)
bottom_border_strip(slide, height=0.38)
gear_corners(slide, size=1.6)
rivet_row(slide, y=0.26, count=16, color=BRASS_DARK)
accent_bar(slide, 0.22, 0.22, 7.0, color=ACCENT_ORANGE, width=0.14)

heading(slide,
        "THE FIELD IS ALREADY MOVING",
        "Autonomous AI research is no longer speculative \u2014 it is happening now",
        label_color=BRASS_LIGHT, title_color=WHITE, title_size=24)

steampunk_divider(slide, y=1.28, left=0.5, width=12.3, h=0.24)

# Table header
add_rect(slide, 0.5, 1.6, 12.4, 0.4, BRASS_DARK)
add_rect(slide, 0.5, 1.6, 12.4, 0.02, BRASS)
add_rect(slide, 0.5, 2.0, 12.4, 0.02, BRASS)
for label, x in [("System", 0.6), ("Organization", 2.45),
                  ("Milestone", 4.7), ("Relevance to Lab", 9.25)]:
    add_textbox(slide, x, 1.64, 2.2, 0.3, label,
                size_pt=11, color=BRASS_LIGHT, bold=True)

field_rows = [
    ("autoresearch",    "Karpathy (2026)",
     "Agent-driven code iteration on consumer GPU; adopted worldwide in weeks",
     "Foundation of this repo", ACCENT_BLUE),
    ("PaperQA2",        "FutureHouse",
     "Beats PhD researchers at biology literature search (LitQA2 benchmark)",
     "Direct analog for miRNA literature work", ACCENT_GREEN),
    ("ContraCrow",      "FutureHouse",
     "Finds ~2.34 contradicted statements per biology paper",
     "Contradiction finder for miRNA field", ACCENT_TEAL),
    ("WikiCrow",        "FutureHouse",
     "Gene-level summaries from 1 million papers, more accurate than Wikipedia",
     "Gene-level knowledge base for C. elegans", ACCENT_TEAL),
    ("AI Scientist v2", "Sakana AI",
     "First AI-generated paper to pass peer review at ICLR workshop",
     "Full autonomous research loop", ACCENT_PURPLE),
    ("Coscientist",     "CMU (Gomes lab)",
     "Autonomous chemistry experiments via robotic API (Nature, 2023)",
     "Closes hypothesis-to-wet-lab loop", ACCENT_ORANGE),
]

for r, (system, org, milestone, relevance, col) in enumerate(field_rows):
    y = 2.08 + r * 0.57
    bg = PANEL_BG if r % 2 == 0 else PANEL_MID
    add_rect(slide, 0.5, y, 12.4, 0.55, bg)
    add_rect(slide, 0.5, y + 0.55, 12.4, 0.01, BRASS_DARK)
    add_textbox(slide, 0.6, y + 0.07, 1.8, 0.38, system,
                size_pt=11.5, color=col, bold=True)
    add_textbox(slide, 2.45, y + 0.07, 2.2, 0.38, org,
                size_pt=11, color=LIGHT_GRAY)
    add_textbox(slide, 4.7, y + 0.07, 4.5, 0.38, milestone,
                size_pt=11, color=WHITE)
    add_textbox(slide, 9.25, y + 0.07, 3.5, 0.38, relevance,
                size_pt=10.5, color=MEDIUM_GRAY, italic=True)

add_textbox(slide, 0.5, 5.55, 12.4, 0.44,
            "The question is not whether autonomous research tools will be useful in biology labs \u2014 it is how quickly labs like the Pasquinelli lab adopt them.",
            size_pt=12, color=GOLD, bold=True, align=PP_ALIGN.CENTER)

slide_footer(slide, FOOTER_TEXT)
brass_border(slide)


# ════════════════════════════════════════════════════════════════════════════
# SLIDE 12 — RAG vs. Fine-Tuning
# ════════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide, DARK_BG)
top_border_strip(slide, height=0.22)
bottom_border_strip(slide, height=0.38)
gear_corners(slide, size=1.6)
rivet_row(slide, y=0.26, count=16, color=BRASS_DARK)
accent_bar(slide, 0.22, 0.22, 7.0, color=ACCENT_PURPLE, width=0.14)

heading(slide,
        "TECHNICAL APPROACH",
        "Two paths to a lab-specific LLM \u2014 choose based on your goals",
        label_color=BRASS_LIGHT, title_color=WHITE, title_size=24)

steampunk_divider(slide, y=1.28, left=0.5, width=12.3, h=0.24)

# Table header
add_rect(slide, 0.5, 1.6, 12.4, 0.4, BRASS_DARK)
add_rect(slide, 0.5, 1.6, 12.4, 0.02, BRASS)
add_rect(slide, 0.5, 2.0, 12.4, 0.02, BRASS)
for label, x, w in [("Dimension", 0.6, 3.4),
                     ("RAG (Retrieval-Augmented Generation)", 4.1, 4.1),
                     ("Fine-Tuning", 8.3, 4.3)]:
    add_textbox(slide, x, 1.64, w, 0.3, label,
                size_pt=11, color=BRASS_LIGHT, bold=True)

rag_rows = [
    ("Setup time",           "Hours to days",                        "Days to weeks"),
    ("Hardware needed",      "CPU or small GPU",                     "GPU (RTX 3050 Ti sufficient)"),
    ("Corpus update",        "Add files, re-index (minutes)",        "Retrain (hours)"),
    ("Answers cite sources", "Yes, automatically",                   "Requires prompting"),
    ("Best for",             "Literature Q&A, hypothesis generation","Style adaptation, specialized reasoning"),
    ("Cost",                 "Near-zero (local) or low API cost",    "Near-zero (local)"),
    ("Recommended for lab",  "START HERE \u2192",                    "Add later for specialized tasks"),
]

for r, (dim, rag, ft) in enumerate(rag_rows):
    y = 2.08 + r * 0.54
    bg = PANEL_BG if r % 2 == 0 else PANEL_MID
    add_rect(slide, 0.5, y, 12.4, 0.52, bg)
    add_rect(slide, 0.5, y + 0.52, 12.4, 0.01, BRASS_DARK)
    add_textbox(slide, 0.6, y + 0.07, 3.4, 0.38, dim,
                size_pt=11.5, color=LIGHT_GRAY, bold=True)
    rag_col = ACCENT_GREEN if dim == "Recommended for lab" else WHITE
    ft_col  = MEDIUM_GRAY  if dim == "Recommended for lab" else WHITE
    add_textbox(slide, 4.1, y + 0.07, 4.1, 0.38, rag,
                size_pt=11.5, color=rag_col)
    add_textbox(slide, 8.3, y + 0.07, 4.3, 0.38, ft,
                size_pt=11.5, color=ft_col)

tf = add_textbox(slide, 0.5, 5.88, 12.4, 0.38,
                 "RAG in plain English: The model looks up relevant passages from your corpus before answering \u2014 like giving the LLM a searchable library of your papers.",
                 size_pt=11, color=MEDIUM_GRAY, italic=True)
add_para(tf, "Fine-tuning in plain English: You train the model\u2019s weights on your corpus so the knowledge is baked in. More powerful but more effort to update.",
         size_pt=11, color=MEDIUM_GRAY, italic=True, space_before_pt=3)

slide_footer(slide, FOOTER_TEXT)
brass_border(slide)


# ════════════════════════════════════════════════════════════════════════════
# SLIDE 13 — program.md Template
# ════════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide, DARK_BG)
top_border_strip(slide, height=0.22)
bottom_border_strip(slide, height=0.38)
gear_corners(slide, size=1.6)
rivet_row(slide, y=0.26, count=16, color=BRASS_DARK)
accent_bar(slide, 0.22, 0.22, 7.0, color=ACCENT_TEAL, width=0.14)

heading(slide,
        "THE RESEARCH STRATEGY FILE",
        "program.md is what makes this a Pasquinelli Lab agent, not a generic chatbot",
        label_color=BRASS_LIGHT, title_color=WHITE, title_size=22)

steampunk_divider(slide, y=1.28, left=0.5, width=12.3, h=0.24)

# Code block panel
panel_box(slide, 0.5, 1.6, 7.5, 5.1)
code_lines = [
    ("You are a research assistant for the Pasquinelli Lab at UC San Diego.", WHITE, False),
    ("", WHITE, False),
    ("Your expertise covers:", ACCENT_TEAL, True),
    ("  \u2022 microRNA biology, biogenesis, and target regulation", LIGHT_GRAY, False),
    ("  \u2022 C. elegans genetics, aging, and stress response", LIGHT_GRAY, False),
    ("  \u2022 Poly(A) tail biology and translational regulation", LIGHT_GRAY, False),
    ("  \u2022 let-7 and small RNA regulatory mechanisms", LIGHT_GRAY, False),
    ("  \u2022 RNA processing and isoform regulation", LIGHT_GRAY, False),
    ("", WHITE, False),
    ("Your corpus includes all Pasquinelli lab publications", ACCENT_TEAL, True),
    ("from 2000 to 2025, plus key papers from the Bartel,", ACCENT_TEAL, False),
    ("Ambros, Richter, and Kaeberlein labs.", ACCENT_TEAL, False),
    ("", WHITE, False),
    ("For each task:", BRASS_LIGHT, True),
    ("  1. Search the corpus for relevant evidence", LIGHT_GRAY, False),
    ("  2. Extract key claims with citations", LIGHT_GRAY, False),
    ("  3. Grade evidence: strong / moderate / weak / contested", LIGHT_GRAY, False),
    ("  4. Identify gaps and open questions", LIGHT_GRAY, False),
    ("  5. Output as structured tables and ranked lists", LIGHT_GRAY, False),
    ("", WHITE, False),
    ("Current focus: [INSERT CURRENT RESEARCH QUESTION]", GOLD, True),
]
tf = add_textbox(slide, 0.65, 1.68, 7.2, 4.9,
                 code_lines[0][0], size_pt=10.5, color=code_lines[0][1],
                 bold=code_lines[0][2])
for line, col, bold in code_lines[1:]:
    add_para(tf, line, size_pt=10.5, color=col, bold=bold, space_before_pt=1)

# Right explanation panel
panel_box(slide, 8.3, 1.6, 4.7, 5.1)
add_img(slide, IMG_GEAR_SM, 12.1, 1.64, 0.78, 0.78)
add_textbox(slide, 8.48, 1.72, 4.35, 0.38,
            "Why this file matters", size_pt=14, color=ACCENT_TEAL, bold=True)
tf2 = add_textbox(slide, 8.48, 2.18, 4.35, 4.3,
                  "The program.md file is your research strategy. It tells the agent:",
                  size_pt=11.5, color=WHITE)
add_para(tf2, " ", size_pt=5, color=WHITE, space_before_pt=2)
add_para(tf2, "\u2022 What domain it is working in", size_pt=11.5, color=LIGHT_GRAY, space_before_pt=4)
add_para(tf2, "\u2022 What corpus to draw from", size_pt=11.5, color=LIGHT_GRAY, space_before_pt=4)
add_para(tf2, "\u2022 How to format outputs", size_pt=11.5, color=LIGHT_GRAY, space_before_pt=4)
add_para(tf2, "\u2022 What the current research focus is", size_pt=11.5, color=LIGHT_GRAY, space_before_pt=4)
add_para(tf2, " ", size_pt=5, color=WHITE, space_before_pt=2)
add_para(tf2, "Invest time in refining it. Each iteration makes the agent more useful.",
         size_pt=11.5, color=GOLD, bold=True, space_before_pt=6)
add_para(tf2, " ", size_pt=5, color=WHITE, space_before_pt=2)
add_para(tf2, "Template available in:", size_pt=10.5, color=MEDIUM_GRAY, space_before_pt=6)
add_para(tf2, "amy_autoresearch_howto/", size_pt=10.5, color=ACCENT_TEAL, space_before_pt=2)
add_para(tf2, "Amy_Autoresearch branch", size_pt=10.5, color=ACCENT_TEAL, space_before_pt=2)

slide_footer(slide, FOOTER_TEXT)
brass_border(slide)


# ════════════════════════════════════════════════════════════════════════════
# SLIDE 14 — Quick Wins
# ════════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide, DARK_BG)
top_border_strip(slide, height=0.22)
bottom_border_strip(slide, height=0.38)
gear_corners(slide, size=1.6)
rivet_row(slide, y=0.26, count=16, color=BRASS_DARK)
accent_bar(slide, 0.22, 0.22, 7.0, color=ACCENT_GREEN, width=0.14)

heading(slide,
        "GETTING STARTED TODAY",
        "You can have a working lab LLM agent in 48 hours",
        label_color=BRASS_LIGHT, title_color=WHITE, title_size=24)

steampunk_divider(slide, y=1.28, left=0.5, width=12.3, h=0.24)

# Left: This week
panel_box(slide, 0.5, 1.6, 5.9, 4.8)
add_img(slide, IMG_GEAR_SM, 5.8, 1.64, 0.52, 0.52)
add_textbox(slide, 0.68, 1.72, 5.5, 0.38,
            "This week (hours to days)", size_pt=14, color=ACCENT_GREEN, bold=True)
quick_wins = [
    ("1.", "Literature gap-finder for next grant proposal", "1\u20132 days"),
    ("2.", "New-paper alert and summary service", "Half a day"),
    ("3.", "Manuscript consistency checker", "Hours per manuscript"),
    ("4.", "Hypothesis ranking board from a seed paper", "1\u20132 days"),
    ("5.", "Lab knowledge base for onboarding", "Ongoing, seed in hours"),
]
for i, (num, task, time) in enumerate(quick_wins):
    y = 2.2 + i * 0.82
    add_textbox(slide, 0.68, y, 0.38, 0.38, num,
                size_pt=13, color=ACCENT_GREEN, bold=True)
    add_textbox(slide, 1.1, y, 4.1, 0.32, task,
                size_pt=12, color=WHITE)
    add_textbox(slide, 1.1, y + 0.33, 4.1, 0.28, time,
                size_pt=10.5, color=MEDIUM_GRAY, italic=True)

# Right: This month
panel_box(slide, 6.9, 1.6, 6.0, 4.8)
add_img(slide, IMG_GEAR_SM, 12.3, 1.64, 0.52, 0.52)
add_textbox(slide, 7.08, 1.72, 5.7, 0.38,
            "This month (days to weeks)", size_pt=14, color=ACCENT_ORANGE, bold=True)
month_items = [
    ("1.", "Full corpus build: all lab papers + key field papers"),
    ("2.", "RAG-based query system: ask questions, get cited answers"),
    ("3.", "Isoform shift analysis on 2024 aging data"),
    ("4.", "Cross-dataset replication of aging signatures"),
    ("5.", "Living hypothesis board that updates as new papers appear"),
]
for i, (num, task) in enumerate(month_items):
    y = 2.2 + i * 0.82
    add_textbox(slide, 7.08, y, 0.38, 0.38, num,
                size_pt=13, color=ACCENT_ORANGE, bold=True)
    add_textbox(slide, 7.5, y, 5.1, 0.55, task,
                size_pt=12, color=WHITE, wrap=True)

panel_box(slide, 0.5, 6.45, 12.4, 0.44, fill=PANEL_MID)
add_textbox(slide, 0.65, 6.5, 12.1, 0.36,
            "All how-to guides, starter code, and program.md templates: amy_autoresearch_howto/  \u2022  github.com/jlpfly/Karpathy_autoresearch",
            size_pt=12, color=ACCENT_BLUE, align=PP_ALIGN.CENTER)

slide_footer(slide, FOOTER_TEXT)
brass_border(slide)


# ════════════════════════════════════════════════════════════════════════════
# SLIDE 15 — Closing
# ════════════════════════════════════════════════════════════════════════════
slide = prs.slides.add_slide(prs.slide_layouts[6])
set_bg(slide, DARK_BG)
top_border_strip(slide, height=0.22)
bottom_border_strip(slide, height=0.38)
gear_corners(slide, size=2.0)
rivet_row(slide, y=0.26, count=16, color=BRASS_DARK)
accent_bar(slide, 0.22, 0.22, 7.0, color=ACCENT_BLUE, width=0.14)
accent_bar(slide, 0.36, 0.22, 7.0, color=BRASS_DARK, width=0.05)

# Clock (ghosted right side)
add_img(slide, IMG_CLOCK, 10.2, 1.2, 2.8, 2.8)

heading(slide,
        "CLOSING",
        "The Pasquinelli Lab is positioned to lead in AI-augmented RNA biology",
        label_color=BRASS_LIGHT, title_color=WHITE, title_size=24)

steampunk_divider(slide, y=1.28, left=0.5, width=12.3, h=0.24)

# Why this lab
panel_box(slide, 0.5, 1.6, 5.9, 2.8)
add_textbox(slide, 0.68, 1.72, 5.5, 0.38,
            "Why this lab, why now", size_pt=14, color=ACCENT_BLUE, bold=True)
tf = add_textbox(slide, 0.68, 2.18, 5.5, 2.1,
                 "\u2022 25 years of publications = a rich, coherent training corpus",
                 size_pt=12, color=WHITE)
add_para(tf, "\u2022 Deep expertise in a focused domain = high-quality agent outputs",
         size_pt=12, color=WHITE, space_before_pt=5)
add_para(tf, "\u2022 Existing compute (RTX 3050 Ti) = no new hardware needed",
         size_pt=12, color=WHITE, space_before_pt=5)
add_para(tf, "\u2022 Active hiring in non-coding RNA = new members benefit immediately",
         size_pt=12, color=WHITE, space_before_pt=5)

# What it amplifies
panel_box(slide, 6.9, 1.6, 6.0, 2.8)
add_textbox(slide, 7.08, 1.72, 5.7, 0.38,
            "What the agent amplifies", size_pt=14, color=ACCENT_GREEN, bold=True)
tf2 = add_textbox(slide, 7.08, 2.18, 5.7, 2.1,
                  "\u2022 Literature coverage: reads faster and more consistently than any human",
                  size_pt=12, color=WHITE)
add_para(tf2, "\u2022 Hypothesis generation: surfaces connections across hundreds of papers",
         size_pt=12, color=WHITE, space_before_pt=5)
add_para(tf2, "\u2022 Institutional memory: new lab members up to speed in days, not months",
         size_pt=12, color=WHITE, space_before_pt=5)
add_para(tf2, "\u2022 Grant preparation: structures evidence and identifies gaps systematically",
         size_pt=12, color=WHITE, space_before_pt=5)

# What it cannot replace
panel_box(slide, 0.5, 4.52, 12.4, 1.3, fill=PANEL_MID)
add_textbox(slide, 0.68, 4.62, 12.0, 0.36,
            "What the agent cannot replace", size_pt=13, color=BRASS_LIGHT, bold=True)
add_textbox(slide, 0.68, 5.04, 12.0, 0.65,
            "Experimental creativity and biological intuition  \u2022  Wet-lab execution and troubleshooting  "
            "\u2022  Peer relationships and collaboration  \u2022  The judgment to know which question matters",
            size_pt=12, color=LIGHT_GRAY)

# Final quote
panel_box(slide, 0.5, 5.96, 12.4, 0.82, fill=PANEL_MID)
steampunk_divider(slide, y=5.98, left=0.55, width=12.2, h=0.18)
add_textbox(slide, 0.65, 6.18, 12.1, 0.55,
            "\u201cThe era of AI-augmented biology is here. The Pasquinelli Lab has the corpus, the compute, "
            "and the questions. The only remaining step is to build the agent.\u201d",
            size_pt=13, color=GOLD, bold=True, italic=True, align=PP_ALIGN.CENTER)

slide_footer(slide, "github.com/jlpfly/Karpathy_autoresearch  \u2022  Branch: Amy_Autoresearch  \u2022  Pasquinelli Lab  \u2022  UC San Diego")
brass_border(slide)


# ════════════════════════════════════════════════════════════════════════════
# SAVE
# ════════════════════════════════════════════════════════════════════════════
out = "Pasquinelli_AI_Agent_Pitch.pptx"
prs.save(out)
print(f"Saved: {out}  ({len(prs.slides)} slides)")
