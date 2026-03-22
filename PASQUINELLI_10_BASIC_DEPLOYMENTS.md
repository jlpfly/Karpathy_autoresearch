# 10 Basic Computational Deployment Examples for Autoresearch

*Linked from the [Pasquinelli Autoresearch Playbook](PASQUINELLI_AUTORESEARCH_README.md)*

These are intentionally **basic but informative** and **purely computational**. They do not require lab automation or procedural biology. Each one can be set up using this repo with minor edits to `program.md`.

---

## 1. Publication timeline summarizer

Build a year-by-year map of the Pasquinelli lab's themes:

- let-7 era (2000–2005)
- miRNA targeting era (2005–2015)
- aging/stress era (2015–2022)
- long-read transcriptome era (2022–present)

**Output:**

- one-page theme timeline
- paper clusters by topic
- visual evolution of the lab's research direction

**Why it's informative:** Shows how the lab's questions have evolved and where momentum is building. Useful for grant narratives and onboarding.

---

## 2. miRNA-family specificity tracker

Use the 2023 miR-238/239ab paper as a seed and collect similar studies where shared-seed miRNAs do **not** behave redundantly.

**Output:**

- table of family members, phenotype, evidence type
- "expression-driven" versus "sequence-driven" interpretation for each case
- cross-species comparison where available

**Why it's informative:** Directly tests a core assumption in miRNA biology—that shared seeds mean shared function.

---

## 3. Aging-miRNA pathway map

Build a citation-backed graph of miRNAs connected to:

- IIS / insulin signaling
- proteostasis
- stress recovery
- autophagy
- longevity

**Output:**

- pathway-to-miRNA matrix
- shortlist of best-supported aging regulators
- gap analysis showing which pathway–miRNA connections lack strong evidence

**Why it's informative:** Provides a structured overview of the miRNA-aging field that can seed new hypotheses or identify underexplored connections.

---

## 4. Heat-shock recovery evidence board

Center the 2021 heat-shock recovery paper and gather related studies on miRNAs in:

- heat shock
- oxidative stress
- infection response
- recovery-phase regulation (not just stress onset)

**Output:**

- evidence table with paper, organism, miRNA, target, and direction of effect
- known targets and their confidence levels
- unresolved questions and contradictions

**Why it's informative:** Recovery biology is understudied relative to stress-onset biology. This board highlights what is known and what is missing.

---

## 5. Direct RNA-seq aging watchlist

Use the 2024 long-read aging paper as a seed for finding papers on:

- isoform changes with age
- RNA processing fidelity
- RNA editing (A-to-I, pseudouridine)
- long-read sequencing methods in aging contexts

**Output:**

- dataset watchlist with accession numbers
- paper queue ranked by relevance
- topic tags by mechanism

**Why it's informative:** Long-read RNA-seq is a fast-moving field. An automated watchlist ensures the lab stays current without manual PubMed searches.

---

## 6. PABP and poly(A)-tail literature matrix

Use the 2022 PABP paper to organize work on:

- poly(A)-tail length regulation
- nuclear versus cytoplasmic RNA handling
- translation efficiency
- isoform-specific RNA behavior

**Output:**

- concept matrix cross-referencing biological process × evidence type
- transcript-feature table
- open questions for follow-up reading

**Why it's informative:** Poly(A)-tail biology is central to the lab's work but the literature is fragmented. A structured matrix makes it navigable.

---

## 7. High-impact let-7 history deck

Create a structured reading path from the early landmark papers (2000 Nature, 2001 Science) through newer mechanistic work.

**Output:**

- "start here" reading list for newcomers
- historical milestones timeline
- terms and concepts glossary

**Why it's informative:** This is the easiest way to onboard a new rotation student, undergraduate, or collaborator who is new to the miRNA field.

---

## 8. GEO / PMC dataset queue builder

Collect datasets linked from Pasquinelli papers and related studies for future reanalysis.

**Output:**

- accession number table (GEO, SRA, ArrayExpress)
- species, assay type, sample sizes
- relevance notes tied to specific lab questions

**Why it's informative:** Many published datasets are never reanalyzed. Building a curated queue makes it easy for a computational lab member to pick up a reanalysis project.

---

## 9. Contradiction finder across reviews and primary papers

Compare older miRNA targeting assumptions with newer evidence on expression context, isoforms, and non-seed effects.

**Output:**

- "classic claim" vs. "updated view" comparison table
- citation pair showing the shift for each claim
- confidence assessment for each contradiction

**Why it's informative:** Contradictions are where new science lives. This is directly inspired by FutureHouse's ContraCrow system, which finds ~2.34 contradicted statements per paper in biology.

---

## 10. Living hypothesis board for Pasquinelli-lab topics

Use autoresearch to keep a rolling list of:

- strongest supported mechanisms
- weakly supported ideas
- missing experiments in the literature
- next papers worth reading

**Output:**

- evidence-ranked hypothesis list
- next-step reading queue
- "ready to test" vs. "needs more literature work" categorization

**Why it's informative:** A living hypothesis board turns autoresearch from a one-time tool into an ongoing research companion that evolves with the lab's work.

---

## How to use any of these

1. Clone this repo and run `uv sync` + `uv run prepare.py`
2. Edit `program.md` to describe the specific deployment (use the descriptions above as starting points)
3. Build a text corpus from relevant papers (PDFs → text, or use abstracts from PubMed)
4. Run `uv run train.py` for a baseline test, then switch to agent mode for iterative analysis
5. Collect outputs as structured tables, ranked lists, and hypothesis boards

See the [main Pasquinelli Playbook](PASQUINELLI_AUTORESEARCH_README.md) for the full context, 5 impactful dataset-access applications, and field evidence.
