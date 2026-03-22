# Autoresearch Playbook for Amy Pasquinelli Lab Themes

This guide reviews Amy Pasquinelli Lab publications with an emphasis on **2020 and later**, while also calling out a few older **high-impact** studies from the publication list.

It is written as a **computational autoresearch** playbook, not a lab protocol.

The goal is to show how this repo could be used as a focused research assistant for topics like:

- microRNA biology
- aging in _C. elegans_
- stress recovery
- RNA processing and isoform regulation
- poly(A)-tail and PABP biology
- classic let-7 / small-RNA history

## Publications reviewed

Primary source:

- Pasquinelli Lab publications page: <https://pasquinellilab.biosci.ucsd.edu/publications/>

Representative paper pages reviewed while building this summary:

- 2024 NAR aging direct RNA-seq paper: <https://pmc.ncbi.nlm.nih.gov/articles/PMC11662692/>
- 2023 PLoS Genetics miR-238 paper: <https://doi.org/10.1371/journal.pgen.1011055>
- 2022 Front Aging review: <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9261348/>
- 2022 NAR PABP paper: <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9071453/>
- 2021 PLoS Genetics heat-shock recovery paper: <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8370650/>
- 2000 Nature let-7 paper: <https://pubmed.ncbi.nlm.nih.gov/10706289/>
- 2001 Science Dicer / let-7 paper: <https://pubmed.ncbi.nlm.nih.gov/11452083/>

## What stands out from the publication list

The publication list shows a very consistent long-term focus on **post-transcriptional gene regulation**, especially:

- microRNAs and their targets
- Argonaute biology
- let-7 and developmental timing
- RNA processing and transcript maturation
- poly(A) tails and RNA-binding proteins
- aging and stress-response regulation in _C. elegans_

Looking at the **2020+** papers, the center of gravity seems to be:

- how miRNAs shape aging and stress responses
- how RNA processing changes with age
- how transcript isoforms and RNA tail biology carry functional information
- how genome-scale and long-read approaches can reveal new RNA regulation layers

## Recent publication review: 2020 and after

### 2024: Full-length direct RNA sequencing reveals extensive remodeling of RNA expression, processing and modification in aging _C. elegans_

This paper looks like a strong example of the lab moving into **long-read/native RNA profiling** for aging biology.

What stands out:

- uses direct RNA sequencing plus standard RNA-seq
- reports age-associated changes in isoforms and RNA processing
- emphasizes declining RNA-processing fidelity with age
- maps inosine and pseudouridine signals at scale

Why it matters for autoresearch:

- it gives a rich anchor for aging transcriptome curation
- it suggests many computational follow-ups around isoforms, edits, and RNA-processing drift

### 2023: Expression, not sequence, distinguishes miR-238 from its miR-239ab sister miRNAs in promoting longevity in _C. elegans_

This paper sharpens a classic miRNA question: if family members share a seed, are they really interchangeable?

What stands out:

- re-examines potentially opposing longevity roles within a miRNA family
- argues that **expression context**, more than sequence differences, explains the functional distinction
- ties miRNA-family specificity directly to aging phenotypes

Why it matters for autoresearch:

- it is perfect for hypothesis-ranking around family-member specificity
- it gives a strong use case for separating "same-seed" from "same-function"

### 2022: New roles for microRNAs in old worms

This review helps connect miRNA biology to the broader longevity field.

What stands out:

- frames miRNAs as important regulators of insulin signaling, diet responses, autophagy, proteostasis, and lifespan
- highlights how much is known already, while making it clear that many functions remain unresolved
- is useful as a map of the field rather than a single experimental result

Why it matters for autoresearch:

- good seed document for building a literature knowledge graph
- useful for identifying open questions and recurring pathways

### 2022: Nuclear and Cytoplasmic poly(A) binding proteins (PABPs) favor distinct transcripts and isoforms

This paper extends the lab's long-standing interest in RNA tail biology into transcript-level resolution.

What stands out:

- compares nuclear and cytoplasmic PABP-associated RNAs
- highlights transcript and isoform specificity
- links splicing status, poly(A)-tail length, and translation status

Why it matters for autoresearch:

- strong candidate for structured table extraction
- useful for cross-study work on isoform-specific regulation

### 2022: _C. elegans_ transposable elements harbor diverse transcription factor DNA-binding sites

This paper points to a broader regulatory-genome direction beyond canonical miRNA target studies.

What stands out:

- transposable elements are treated as potential regulatory sequence carriers
- the work expands from RNA regulation into genome regulatory architecture

Why it matters for autoresearch:

- useful for motif cataloging, regulatory annotation summaries, and literature comparisons

### 2021: Recovery from Heat Shock Requires the MicroRNA Pathway in _C. elegans_

This paper is a very nice example of focusing not just on the stress response itself, but on **recovery** after stress.

What stands out:

- identifies a role for the miRNA pathway after heat shock
- specifically links miR-85 and `hsp-70` regulation to post-stress survival
- highlights recovery dynamics rather than only stress induction

Why it matters for autoresearch:

- excellent for building causal pathway summaries
- easy to turn into a structured stress-response evidence map

### 2020: Auxin-independent depletion of degron-tagged proteins by TIR1

This is more of a tool/method paper, but still useful.

What stands out:

- contributes to experimental toolkit awareness
- supports reproducibility and interpretation of later genetics papers that use inducible depletion systems

Why it matters for autoresearch:

- ideal for methods tracking
- helps build "which papers used which perturbation strategy?" summaries

## Older high-impact studies worth including

Even with the focus on 2020+, the publication list contains several older papers that are clearly major field anchors.

### 2000: The 21-nucleotide let-7 RNA regulates developmental timing in _C. elegans_ (Nature)

This is a landmark paper in small-RNA biology.

Why it stands out:

- identifies `let-7` as a regulatory small RNA controlling developmental timing
- helped establish miRNAs as central biological regulators instead of curiosities

### 2000: Conservation of the sequence and temporal expression of `let-7` heterochronic regulatory RNA (Nature)

This is another major impact paper from the list.

Why it stands out:

- showed evolutionary conservation of `let-7`
- helped make the case that miRNA regulation is broadly important across animals

### 2001: A cellular function for the RNA-interference enzyme Dicer in the maturation of the `let-7` small temporal RNA (Science)

This is a foundational bridge between RNAi machinery and miRNA maturation.

Why it stands out:

- directly links Dicer to let-7 processing
- helped define how miRNAs are made, not just what they do

### 2012: MicroRNAs and their targets: recognition, regulation and an emerging reciprocal relationship (Nature Reviews Genetics)

This review is a high-impact synthesis paper in the list.

Why it stands out:

- consolidates miRNA targeting principles
- helps interpret later work on specificity, seed rules, and context dependence

## Overall read on the Pasquinelli Lab publication profile

The easiest way to summarize the lab's trajectory is:

> from foundational miRNA discovery and let-7 biology, toward increasingly systems-level studies of RNA regulation, aging, stress, transcript diversity, and RNA processing.

That makes the lab especially well-suited to **computational autoresearch** because the literature naturally lends itself to:

- mechanism mapping
- paper comparison
- target/pathway prioritization
- dataset discovery
- structured evidence tables

## 10 easy computational deployment examples for autoresearch

These are intentionally **easy** and **computational**. They do not require lab automation or procedural biology.

### 1. Publication timeline summarizer

Build a year-by-year map of the lab's themes:

- let-7 era
- miRNA targeting era
- aging/stress era
- long-read transcriptome era

Output:

- one-page theme timeline
- paper clusters by topic

### 2. miRNA-family specificity tracker

Use the 2023 miR-238/239ab paper as a seed and collect similar studies where shared-seed miRNAs do **not** behave redundantly.

Output:

- table of family members
- phenotype
- evidence type
- "expression-driven" versus "sequence-driven" interpretation

### 3. Aging-miRNA pathway map

Build a citation-backed graph of miRNAs connected to:

- IIS / insulin signaling
- proteostasis
- stress recovery
- autophagy
- longevity

Output:

- pathway-to-miRNA matrix
- shortlist of best-supported aging regulators

### 4. Heat-shock recovery evidence board

Center the 2021 heat-shock recovery paper and gather related studies on miRNAs in:

- heat shock
- oxidative stress
- infection response
- recovery-phase regulation

Output:

- evidence table
- known targets
- unresolved questions

### 5. Direct RNA-seq aging watchlist

Use the 2024 long-read aging paper as a seed for finding papers on:

- isoform changes with age
- RNA processing fidelity
- RNA editing
- pseudouridine in aging

Output:

- dataset watchlist
- paper queue
- topic tags by mechanism

### 6. PABP and poly(A)-tail literature matrix

Use the 2022 PABP paper to organize work on:

- poly(A)-tail length
- nuclear versus cytoplasmic RNA handling
- translation efficiency
- isoform-specific RNA behavior

Output:

- concept matrix
- transcript-feature table
- open questions for follow-up reading

### 7. High-impact let-7 history deck

Create a structured reading path from the early landmark papers through newer mechanistic work.

Output:

- "start here" reading list
- historical milestones
- terms and concepts glossary

This is a very easy way to onboard someone new to the area.

### 8. GEO / PMC dataset queue builder

Collect datasets linked from Pasquinelli papers and related studies for future reanalysis.

Output:

- accession number table
- species
- assay type
- relevance notes

### 9. Contradiction finder across reviews and primary papers

Compare older miRNA targeting assumptions with newer evidence on expression context, isoforms, and non-seed effects.

Output:

- "classic claim"
- "updated view"
- citation pair showing the shift

### 10. Living hypothesis board for Pasquinelli-lab topics

Use autoresearch to keep a rolling list of:

- strongest supported mechanisms
- weakly supported ideas
- missing experiments in the literature
- next papers worth reading

Output:

- evidence-ranked hypothesis list
- next-step reading queue

## Safe ways to use this repo for these topics

A practical and safe use of this repo would be:

1. build a focused corpus from the Pasquinelli lab publications plus key related papers
2. tune `program.md` so the agent behaves like a literature analyst
3. ask it to extract claims, targets, pathways, datasets, and open questions
4. keep outputs as tables, notes, and ranked hypotheses

Good prompt directions include:

- "Summarize aging-related miRNA mechanisms across Pasquinelli lab papers after 2020."
- "Compare heat-shock recovery papers to aging papers and find shared RNA regulators."
- "Track how the lab's interpretation of miRNA specificity changes over time."
- "Build a structured reading list from foundational let-7 papers to recent aging transcriptome papers."

---

## 5 impactful applications if autoresearch has access to datasets

These go beyond literature review. If the system is allowed to read, parse, and computationally analyze actual experimental datasets from the Pasquinelli lab or public repositories, the following become possible.

### 1. Age-dependent isoform shift quantification

**What it does:** Directly reanalyze the 2024 direct RNA-seq aging data to build an age-stratified isoform usage matrix across all detected genes, then automatically flag genes where isoform switching correlates with age more strongly than overall expression change.

**Why it's impactful:** The 2024 paper reports age-associated changes in isoforms and RNA processing, but a systematic, gene-by-gene isoform-switching analysis can reveal candidates that expression-level analyses miss. Autoresearch can iterate over parameter choices (e.g., different age bins, filtering thresholds) overnight without human babysitting.

**Output:** Ranked list of genes with significant isoform switching, heatmaps by age group, candidate lists for follow-up.

### 2. Cross-dataset miRNA target concordance scoring

**What it does:** Pull miRNA target predictions from TargetScan, miRDB, and published CLIP/CLASH datasets, then cross-reference them against differential expression or translational efficiency data from Pasquinelli lab experiments to build a concordance score for each predicted target.

**Why it's impactful:** Target prediction databases disagree frequently. Having an automated system score targets by how well they match the lab's own functional data produces a curated, lab-specific target list that is far more actionable than any single prediction tool.

**Output:** Concordance-scored target table, Venn diagrams of database agreement, shortlist of high-confidence targets.

### 3. Poly(A)-tail length and translation efficiency integration

**What it does:** If poly(A)-tail measurement data (from the 2022 PABP paper or related experiments) and ribosome profiling or translation reporter data are available, autoresearch can systematically correlate tail length with translational output across transcripts.

**Why it's impactful:** The relationship between poly(A)-tail length and translation is known to be complex and context-dependent. An automated sweep across all transcripts with available data can identify outlier transcripts where the expected relationship breaks down—these outliers are often the most interesting biology.

**Output:** Scatter plots of tail length vs. translation efficiency, outlier transcript lists, GO enrichment of outlier groups.

### 4. Stress-recovery time-series gene module detection

**What it does:** Use the heat-shock recovery data from the 2021 paper (and any time-series experiments from the lab) to cluster genes into co-regulated modules based on their recovery dynamics, then automatically map known miRNA targets onto those modules.

**Why it's impactful:** Recovery dynamics are harder to analyze than simple stress/control comparisons. Automated clustering + miRNA target overlay can reveal which miRNAs are likely controlling which recovery gene programs—something that would take weeks of manual analysis.

**Output:** Gene module assignments, module-miRNA association scores, network visualizations, temporal expression profiles per module.

### 5. Automated re-analysis of public _C. elegans_ aging datasets with lab-specific gene signatures

**What it does:** Download and standardize public _C. elegans_ aging RNA-seq datasets from GEO (there are dozens), then score each one using gene signatures derived from the lab's own data. Autoresearch iterates overnight to check whether the lab's aging signatures replicate across independent datasets.

**Why it's impactful:** Replication across independent datasets is one of the strongest forms of evidence in genomics. An automated system that pulls, normalizes, and scores external datasets against lab-internal signatures can massively accelerate validation work that might otherwise require a rotation student for months.

**Output:** Replication score table across datasets, forest plots, meta-analysis summary, list of signatures that do and do not replicate.

---

## 5 starter or building models for a PhD post-doc or PI

These are practical, lower-barrier projects that a post-doc, advanced graduate student, or Amy herself could set up in days rather than weeks. They use this repo as-is (or with minor `program.md` edits) and require no custom infrastructure beyond what is already in the autoresearch setup.

### 1. Literature gap-finder for a grant proposal

**What to do:** Point autoresearch at the lab's 5–10 most recent papers and ask it to identify claims that are well-supported, claims that rely on a single paper, and areas where the literature is thin or contradictory.

**Effort:** 1–2 days of setup and prompt iteration.

**What you get:** A structured "state of evidence" document that can directly inform the Significance and Innovation sections of an R01 or R21. Instead of spending a week re-reading papers, the post-doc gets a first-draft evidence map in a day.

**How to start:** Edit `program.md` to say: "You are a literature analyst for RNA biology. Your job is to read papers, extract key claims, grade the evidence supporting each claim (strong / moderate / weak / contested), and identify gaps."

### 2. New-paper alert and summary service

**What to do:** Set up a weekly or daily run where autoresearch checks PubMed or bioRxiv for new papers matching keywords relevant to the lab (miRNA, C. elegans, aging, poly(A), let-7, PABP, etc.), then generates a 1-page summary of each new paper with a relevance score.

**Effort:** Half a day to set up, then automated.

**What you get:** A "journal club assistant" that never misses a new paper. The PI or post-doc reviews a ranked summary list instead of scanning dozens of abstracts manually.

**How to start:** Modify the autoresearch loop to pull new abstracts from a PubMed RSS feed or Semantic Scholar API, then run the summarizer against each one.

### 3. Figure legend and methods cross-checker

**What to do:** Feed autoresearch the methods and figure legends from a manuscript draft. Ask it to check for internal consistency: do the figure legends match the methods? Are sample sizes and statistical tests consistent? Are all abbreviations defined?

**Effort:** A few hours per manuscript.

**What you get:** A pre-submission consistency check that catches the kinds of errors that reviewers flag. This is especially useful for multi-author papers where different people wrote different sections.

**How to start:** Use `program.md` to instruct: "You are a manuscript consistency checker. Compare the methods section against every figure legend. Report any discrepancies in sample sizes, statistical tests, strain names, or experimental conditions."

### 4. Hypothesis ranking board from a single seed paper

**What to do:** Give autoresearch one anchor paper (e.g., the 2023 miR-238/239ab paper) and ask it to: (a) extract the main claims, (b) find 10–20 related papers, (c) assess which claims are supported, extended, or contradicted, and (d) generate 5 testable hypotheses ranked by strength of existing evidence.

**Effort:** 1–2 days.

**What you get:** A prioritized hypothesis list with citations, ready for discussion at a lab meeting. This is the exact workflow that FutureHouse's ContraCrow system (see below) was designed for, but run locally on your own terms.

**How to start:** Use `program.md` with: "You are a hypothesis generator for miRNA biology. Start from [paper DOI]. Find related work. Rank hypotheses by how well they are supported and how testable they are."

### 5. Reusable "lab knowledge base" builder

**What to do:** Over time, feed the lab's key papers, protocols, and internal notes into an autoresearch corpus. Use it as a queryable lab memory: "What strains did we use for the heat-shock experiments?", "Which miRNAs have we tested in aging contexts?", "What was the result of the 4EHP knockdown in the 2022 paper?"

**Effort:** Ongoing (a few hours to seed, then incremental additions).

**What you get:** An institutional memory that persists across lab members. When a new rotation student joins, they can query the knowledge base instead of asking the same questions the previous five students asked. When writing a review or grant, the PI can query across all lab papers at once.

**How to start:** Build a text corpus from PDFs of lab papers (use a PDF-to-text tool), load it as context for autoresearch, and set `program.md` to: "You are the Pasquinelli Lab knowledge base. Answer questions about the lab's published work with citations."

---

## Autoresearch in biology and science: evidence from the field

The concept of AI-driven autonomous research is no longer speculative. Multiple systems, papers, and labs now provide concrete evidence that this approach works for scientific research. Below is a summary of the most relevant precedents.

### Karpathy's autoresearch (this repo)

- **Released:** March 2026
- **What it does:** Gives an AI agent a small but real LLM training setup. The agent modifies code, trains for 5 minutes, checks results, keeps or discards, and repeats overnight.
- **Core insight:** The human programs the *research strategy* (via `program.md`), not the experiments themselves.
- **Relevance to biology:** The autoresearch loop—hypothesize, test, evaluate, iterate—is domain-agnostic. The same loop works for literature analysis, data re-analysis, and computational biology tasks, not just neural network training.
- **Fork ecosystem:** Within weeks of release, the community created forks for macOS (`miolini/autoresearch-macos`, 1.5k stars), Windows/RTX (`jsegov/autoresearch-win-rtx`, 336 stars), "at home" setups (`mutable-state-inc/autoresearch-at-home`, 435 stars), Apple Neural Engine, Chinese-language, Tenstorrent hardware, and more. This rapid adaptation shows the design is portable.

### The AI Scientist (Sakana AI)

- **Paper:** Lu et al., "The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery" (arXiv:2408.06292, August 2024)
- **Updated:** "The AI Scientist-v2" (arXiv:2504.08066, April 2025) — the first fully AI-generated paper to pass peer review at an ICLR workshop
- **What it does:** Generates novel research ideas, writes code, executes experiments, visualizes results, writes a full scientific paper, and runs a simulated review process. Cost: less than $15 per paper.
- **Key advance in v2:** Eliminates reliance on human-authored code templates. Uses a progressive agentic tree-search methodology.
- **Relevance to Pasquinelli lab:** Demonstrates that autonomous systems can handle the full research cycle (idea → experiment → paper). The same architecture could be adapted for computational biology experiments.

### FutureHouse / PaperQA2

- **Organization:** FutureHouse, a 501(c)(3) nonprofit AI-for-science lab in San Francisco, founded by Sam Rodriques and Andrew White (2023), primarily funded by Eric Schmidt.
- **Paper:** White et al., "PaperQA: Retrieval-Augmented Generative Agent for Scientific Research" (arXiv:2312.07559, December 2023)
- **Key result:** PaperQA2 is the first AI agent to achieve **superhuman performance** on scientific literature search tasks. It outperforms PhD and postdoc-level biology researchers on the LitQA2 benchmark.
- **WikiCrow:** An agent built on PaperQA2 that generates Wikipedia-style summaries **more accurate on average than actual Wikipedia articles**, as judged by blinded PhD-level biology researchers.
- **ContraCrow:** Evaluates every claim in a scientific paper to find contradictions elsewhere in the literature. Finds an average of 2.34 contradicted statements per paper in biology.
- **Scale:** Previously used PaperQA to generate Wikipedia articles for all 20,000 human genes from 1 million scientific papers.
- **Relevance to Pasquinelli lab:** ContraCrow's contradiction-finding workflow is directly analogous to what autoresearch could do for the miRNA literature. PaperQA2's superhuman literature retrieval validates the idea that AI agents can be trusted for literature synthesis in biology.
- **PI:** Andrew White (University of Rochester → FutureHouse co-founder) is both an active researcher and a builder of these tools.

### Coscientist

- **Paper:** Boiko et al., "Autonomous chemical research with large language models" (Nature, 2023; DOI: 10.1038/s41586-023-06792-0)
- **What it does:** A multi-LLM agent that autonomously designs, plans, and executes chemistry experiments, including catalyzed cross-coupling reactions using robotic APIs.
- **PI:** Gabe Gomes (Carnegie Mellon University) — the lab demonstrated that LLM agents can control real lab hardware, not just do literature work.
- **Relevance:** While chemistry-focused, this is the clearest published demonstration of an AI agent closing the loop between hypothesis and wet-lab experiment. For the Pasquinelli lab, this shows the trajectory: today's literature agents will eventually connect to lab automation.

### ResearchAgent

- **Paper:** Baek et al., "ResearchAgent: Iterative Research Idea Generation over Scientific Literature with Large Language Models" (arXiv:2404.07738, NAACL 2025)
- **What it does:** Starting from a core paper, uses an academic graph and knowledge store to define novel problems, propose methods, and design experiments. Multiple LLM-based ReviewingAgents provide iterative feedback.
- **Relevance:** This is the most direct precedent for using autoresearch as a "hypothesis generator" in the style of the starter models described above.

### Self-improving AI programs

- **Paper:** Zelikman et al., "Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation" (arXiv:2310.02304, COLM 2024)
- **What it does:** Uses a language model to write scaffolding code that calls itself to improve itself. Proposes strategies including beam search, genetic algorithms, and simulated annealing—all generated by the LLM.
- **Relevance:** This is the theoretical foundation for Karpathy's autoresearch loop. The agent is not just trying things randomly; it is iteratively improving its own experimental strategy.

---

## PIs and labs actively using or building autonomous research tools

The following investigators are publicly associated with building or using AI agent systems for scientific research. This list focuses on researchers whose work is most relevant to the Pasquinelli lab's themes.

| PI / Leader | Affiliation | System | Focus |
| --- | --- | --- | --- |
| **Andrej Karpathy** | Independent / formerly OpenAI, Tesla | autoresearch | Autonomous ML research via agent-driven code iteration |
| **Andrew White** | FutureHouse (co-founder); formerly U. Rochester | PaperQA2, WikiCrow, ContraCrow | Superhuman literature search and contradiction finding in biology |
| **Sam Rodriques** | FutureHouse (co-founder) | FutureHouse AI Scientist platform | Full AI scientist for biology; gene-level knowledge generation |
| **Gabe Gomes** | Carnegie Mellon University | Coscientist | Autonomous chemistry experiments with LLM + robotic API |
| **David Ha, Llion Jones** | Sakana AI | AI Scientist v1/v2 | Fully automated ML papers; first AI-generated peer-reviewed paper |
| **Jim Collins** | MIT | BioAutoMATED | Automated ML for biological sequence data (antimicrobial peptides, gene regulation) |
| **Connor Coley** | MIT | Various synthesis planning agents | AI-driven retrosynthesis and reaction planning |

### How these relate to Pasquinelli lab work

- **FutureHouse (White, Rodriques):** Most directly relevant. Their ContraCrow system already identifies contradictions in biology papers at scale. Their WikiCrow system already generates gene-level summaries from millions of papers. Both of these workflows map directly onto the Pasquinelli lab's miRNA and aging literature.

- **Collins lab (MIT):** BioAutoMATED automates the machine learning pipeline for biological sequences. For a lab that works with miRNA sequences, target sites, and regulatory motifs, this type of automation could be adapted to predict miRNA targeting efficiency or regulatory element function.

- **Sakana AI (Ha, Jones):** Their AI Scientist v2 was the first to pass actual peer review. While their work is ML-focused, the framework is domain-agnostic and could be adapted for computational biology experiments.

- **Karpathy's autoresearch community:** The rapid fork ecosystem (macOS, Windows/RTX, Apple Neural Engine, Tenstorrent) shows that the autoresearch design pattern is being adopted across many hardware platforms. This means the barrier to entry is falling fast—a post-doc with a laptop GPU can run the same autonomous research loop that was originally designed for H100s.

---

## Bottom line

For Amy Pasquinelli Lab themes, this repo is best used as a:

- literature review engine
- mechanism-mapping assistant
- dataset discovery helper
- hypothesis-ranking system

With **dataset access**, it becomes:

- an isoform analysis pipeline
- a target concordance scorer
- a cross-dataset replication engine
- a time-series gene module detector
- a poly(A)/translation integrator

For a **post-doc or PI starting today**, the easiest wins are:

- gap-finder for grant writing (1–2 days)
- new-paper alert service (half a day to set up)
- hypothesis ranking board from a seed paper (1–2 days)
- lab knowledge base (ongoing, low effort)
- manuscript consistency checker (a few hours per paper)

The field is moving fast. FutureHouse's PaperQA2 already outperforms human researchers at literature retrieval in biology. Sakana AI's system already passes peer review. Karpathy's autoresearch loop is being adopted on consumer hardware worldwide. The question is no longer whether autonomous research tools will be useful in biology labs—it is how quickly labs like the Pasquinelli lab adopt them.

That is the easiest and most immediately useful computational deployment path for autoresearch here.
