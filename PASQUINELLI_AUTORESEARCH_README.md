# Autoresearch Playbook for Amy Pasquinelli Lab

This is a **computational autoresearch** playbook for Amy Pasquinelli's research program. It focuses on what Karpathy's [autoresearch](https://github.com/karpathy/autoresearch) framework can do for the lab today — from literature review to dataset-driven discovery.

**Lab focus areas:**

- microRNA biology and target specificity
- aging and stress recovery in _C. elegans_
- RNA processing, isoform regulation, and poly(A)-tail biology
- let-7 and small-RNA regulatory mechanisms

---

## 5 impactful applications with dataset access

These go beyond literature review. If the system is allowed to read, parse, and computationally analyze actual experimental datasets from the Pasquinelli lab or public repositories, the following become possible. Each has a detailed **how-to guide** with setup instructions and starter code.

### 1. Age-dependent isoform shift quantification

📄 **[Full How-To Guide →](amy_autoresearch_howto/01_isoform_shift_quantification.md)**

Directly reanalyze the 2024 direct RNA-seq aging data to build an age-stratified isoform usage matrix across all detected genes. Automatically flag genes where isoform switching correlates with age more strongly than overall expression change.

**Anchor paper:** 2024 NAR aging direct RNA-seq ([PMC11662692](https://pmc.ncbi.nlm.nih.gov/articles/PMC11662692/))

**Potential collaborators:** Kin Fai Au (Yale, long-read methods), Christopher Vollmers (UCSC, direct RNA-seq), Miten Jain (Northeastern, nanopore)

**Output:** Ranked list of genes with significant isoform switching, heatmaps by age group, candidate lists for follow-up.

### 2. Cross-dataset miRNA target concordance scoring

📄 **[Full How-To Guide →](amy_autoresearch_howto/02_mirna_target_concordance.md)**

Pull miRNA target predictions from TargetScan, miRDB, and published CLIP/CLASH datasets, then cross-reference against the lab's own functional data to build a concordance score for each predicted target.

**Anchor paper:** 2023 miR-238/239ab paper ([DOI:10.1371/journal.pgen.1011055](https://doi.org/10.1371/journal.pgen.1011055))

**Potential collaborators:** David Bartel (MIT, TargetScan), Markus Hafner (NIH, CLIP methods), Chi-Wing Chow (Albert Einstein, target validation)

**Output:** Concordance-scored target table, Venn diagrams of database agreement, shortlist of high-confidence targets.

### 3. Poly(A)-tail length and translation efficiency integration

📄 **[Full How-To Guide →](amy_autoresearch_howto/03_polya_translation_integration.md)**

Systematically correlate poly(A)-tail length measurements with translational output across transcripts. Identify outlier transcripts where the expected relationship breaks down.

**Anchor paper:** 2022 NAR PABP paper ([PMC9071453](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9071453/))

**Potential collaborators:** Joel Richter (UMass Medical, poly(A) regulation), Wendy Gilbert (Yale, ribosome profiling), Marvin Wickens (U. Wisconsin, PABP biology)

**Output:** Scatter plots of tail length vs. translation efficiency, outlier transcript lists, GO enrichment of outlier groups.

### 4. Stress-recovery time-series gene module detection

📄 **[Full How-To Guide →](amy_autoresearch_howto/04_stress_recovery_modules.md)**

Use heat-shock recovery data to cluster genes into co-regulated modules based on their recovery dynamics, then automatically map known miRNA targets onto those modules.

**Anchor paper:** 2021 PLoS Genetics heat-shock recovery paper ([PMC8370650](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8370650/))

**Potential collaborators:** Morimoto lab (Northwestern, proteostasis/heat-shock), Jessica Tyler (Weill Cornell, stress recovery)

**Output:** Gene module assignments, module-miRNA association scores, network visualizations, temporal expression profiles per module.

### 5. Automated cross-dataset replication of aging signatures

📄 **[Full How-To Guide →](amy_autoresearch_howto/05_cross_dataset_replication.md)**

Download and standardize public _C. elegans_ aging RNA-seq datasets from GEO, then score each one using gene signatures derived from the lab's own data. Iterates overnight to check whether aging signatures replicate.

**Anchor paper:** 2024 NAR aging direct RNA-seq ([PMC11662692](https://pmc.ncbi.nlm.nih.gov/articles/PMC11662692/))

**Potential collaborators:** Matt Kaeberlein (Optispan, cross-species aging), Sean Curran (USC, *C. elegans* aging), Coleen Murphy (Princeton, longevity transcriptomics)

**Output:** Replication score table across datasets, forest plots, meta-analysis summary, list of signatures that do and do not replicate.

### How these 5 experiments connect

```
#1 (Isoform Shifts) ──→ feeds isoform-switching gene lists
                              ↓
#2 (Target Concordance) ──→ provides curated miRNA target lists
                              ↓
#3 (Poly(A)/Translation) ──→ identifies tail-length outliers
                              ↓
#4 (Recovery Modules) ──→ maps miRNAs to recovery gene programs
                              ↓
#5 (Cross-Dataset) ──→ validates everything across independent data
```

---

## 5 starter models for a PhD post-doc or PI

These are practical, lower-barrier projects that a post-doc, advanced graduate student, or Amy herself could set up in days rather than weeks.

### 1. Literature gap-finder for a grant proposal

**Effort:** 1–2 days | **Edit `program.md` to say:** "You are a literature analyst for RNA biology. Read papers, extract key claims, grade the evidence supporting each claim (strong / moderate / weak / contested), and identify gaps."

**What you get:** A structured "state of evidence" document that can directly inform the Significance and Innovation sections of an R01 or R21.

### 2. New-paper alert and summary service

**Effort:** Half a day to set up, then automated | **Modify the autoresearch loop** to pull new abstracts from a PubMed RSS feed or Semantic Scholar API, then summarize each new paper with a relevance score.

**What you get:** A "journal club assistant" that never misses a new paper. Ranked summary lists instead of manual abstract scanning.

### 3. Figure legend and methods cross-checker

**Effort:** A few hours per manuscript | **Use `program.md` to instruct:** "You are a manuscript consistency checker. Compare the methods section against every figure legend. Report any discrepancies in sample sizes, statistical tests, strain names, or experimental conditions."

**What you get:** A pre-submission consistency check that catches the errors reviewers flag.

### 4. Hypothesis ranking board from a seed paper

**Effort:** 1–2 days | **Use `program.md` with:** "You are a hypothesis generator for miRNA biology. Start from [paper DOI]. Find related work. Rank hypotheses by how well they are supported and how testable they are."

**What you get:** A prioritized hypothesis list with citations, ready for lab meeting discussion.

### 5. Reusable lab knowledge base

**Effort:** Ongoing (a few hours to seed, then incremental) | **Set `program.md` to:** "You are the Pasquinelli Lab knowledge base. Answer questions about the lab's published work with citations."

**What you get:** An institutional memory that persists across lab members. New rotation students query the knowledge base instead of asking the same questions previous students asked.

---

## Autoresearch in biology and science: evidence from the field

The concept of AI-driven autonomous research is no longer speculative. Multiple systems, papers, and labs provide concrete evidence.

### Karpathy's autoresearch (this repo)

- **Released:** March 2026
- **Core insight:** The human programs the *research strategy* (via `program.md`), not the experiments themselves.
- **Fork ecosystem:** Within weeks, community forks appeared for macOS (1.5k stars), Windows/RTX (336 stars), "at home" setups (435 stars), Apple Neural Engine, and more. A post-doc with a laptop GPU can run the same loop designed for H100s.

### The AI Scientist (Sakana AI)

- **Papers:** arXiv:2408.06292 (Aug 2024), arXiv:2504.08066 (Apr 2025)
- **Milestone:** First fully AI-generated paper to pass peer review at an ICLR workshop
- **What it does:** Generates ideas, writes code, runs experiments, writes papers, and runs simulated review — all for <$15/paper

### FutureHouse / PaperQA2

- **Founded:** 2023 by Sam Rodriques and Andrew White; funded by Eric Schmidt
- **PaperQA2:** First AI agent to achieve **superhuman performance** on biology literature search (outperforms PhD/postdoc researchers on LitQA2)
- **ContraCrow:** Finds ~2.34 contradicted statements per paper in biology — directly applicable to miRNA literature
- **WikiCrow:** Generates gene-level summaries more accurate than Wikipedia, from 1 million papers

### Coscientist (Gomes lab, CMU)

- **Paper:** Nature, 2023 (DOI: 10.1038/s41586-023-06792-0)
- **What it does:** Autonomous chemistry experiments including catalyzed cross-coupling reactions via robotic API — the first demonstration of an AI agent closing the hypothesis-to-wet-lab loop

### ResearchAgent

- **Paper:** arXiv:2404.07738 (NAACL 2025)
- **What it does:** Starting from a core paper, defines novel problems, proposes methods, and designs experiments with iterative LLM-based review

## PIs and labs actively using autonomous research tools

| PI / Leader | Affiliation | System | Focus |
| --- | --- | --- | --- |
| **Andrej Karpathy** | Independent | autoresearch | Autonomous ML research via agent-driven code iteration |
| **Andrew White** | FutureHouse | PaperQA2, WikiCrow, ContraCrow | Superhuman biology literature search and contradiction finding |
| **Sam Rodriques** | FutureHouse | AI Scientist platform | Full AI scientist for biology; gene-level knowledge generation |
| **Gabe Gomes** | Carnegie Mellon | Coscientist | Autonomous chemistry with LLM + robotic API |
| **David Ha, Llion Jones** | Sakana AI | AI Scientist v1/v2 | First AI-generated peer-reviewed paper |
| **Jim Collins** | MIT | BioAutoMATED | Automated ML for biological sequences |
| **Connor Coley** | MIT | Synthesis planning agents | AI-driven retrosynthesis and reaction planning |

**Most directly relevant to the Pasquinelli lab:** FutureHouse's ContraCrow (contradiction finding in biology papers at scale) and WikiCrow (gene-level summaries from millions of papers) map directly onto miRNA and aging literature workflows.

---

## 10 basic computational deployment examples

For easier, literature-focused applications that don't require dataset access, see the separate guide:

📄 **[10 Basic Computational Deployments →](PASQUINELLI_10_BASIC_DEPLOYMENTS.md)**

Includes: publication timeline summarizer, miRNA-family specificity tracker, aging-miRNA pathway map, heat-shock recovery evidence board, direct RNA-seq aging watchlist, PABP/poly(A)-tail literature matrix, let-7 history deck, GEO dataset queue builder, contradiction finder, and living hypothesis board.

---

## Safe ways to use this repo

A practical and safe use of this repo:

1. Build a focused corpus from the Pasquinelli lab publications plus key related papers
2. Tune `program.md` so the agent behaves like a literature analyst
3. Ask it to extract claims, targets, pathways, datasets, and open questions
4. Keep outputs as tables, notes, and ranked hypotheses

**Good prompt directions:**

- "Summarize aging-related miRNA mechanisms across Pasquinelli lab papers after 2020."
- "Compare heat-shock recovery papers to aging papers and find shared RNA regulators."
- "Track how the lab's interpretation of miRNA specificity changes over time."
- "Build a structured reading list from foundational let-7 papers to recent aging transcriptome papers."

---

## Publication review: what stands out from the lab

The publication list shows a consistent long-term focus on **post-transcriptional gene regulation**:

- microRNAs and their targets
- Argonaute biology
- let-7 and developmental timing
- RNA processing and transcript maturation
- poly(A) tails and RNA-binding proteins
- aging and stress-response regulation in _C. elegans_

The **2020+** center of gravity:

- how miRNAs shape aging and stress responses
- how RNA processing changes with age
- how transcript isoforms and RNA tail biology carry functional information
- how genome-scale and long-read approaches reveal new RNA regulation layers

### Recent publications (2020 and after)

**2024: Full-length direct RNA sequencing reveals extensive remodeling in aging _C. elegans_** ([PMC11662692](https://pmc.ncbi.nlm.nih.gov/articles/PMC11662692/))
Long-read/native RNA profiling for aging biology. Reports age-associated changes in isoforms, RNA processing fidelity, inosine and pseudouridine signals at scale.

**2023: Expression, not sequence, distinguishes miR-238 from its miR-239ab sister miRNAs** ([DOI:10.1371/journal.pgen.1011055](https://doi.org/10.1371/journal.pgen.1011055))
Argues expression context—not sequence—explains functional distinction within a miRNA family. Ties family specificity to aging phenotypes.

**2022: New roles for microRNAs in old worms** ([PMC9261348](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9261348/))
Review connecting miRNAs to insulin signaling, diet responses, autophagy, proteostasis, and lifespan.

**2022: Nuclear and Cytoplasmic PABPs favor distinct transcripts and isoforms** ([PMC9071453](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9071453/))
Compares nuclear vs. cytoplasmic PABP-associated RNAs. Links splicing status, poly(A)-tail length, and translation status.

**2022: _C. elegans_ transposable elements harbor diverse TF DNA-binding sites**
Expands from RNA regulation into genome regulatory architecture.

**2021: Recovery from Heat Shock Requires the MicroRNA Pathway** ([PMC8370650](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8370650/))
Links miR-85 and hsp-70 regulation to post-stress survival. Focuses on recovery dynamics, not just stress induction.

**2020: Auxin-independent depletion of degron-tagged proteins by TIR1**
Tool/method paper for inducible depletion systems.

### High-impact older studies

**2000: The 21-nucleotide let-7 RNA regulates developmental timing (Nature)** ([PubMed](https://pubmed.ncbi.nlm.nih.gov/10706289/))
Landmark paper establishing miRNAs as central biological regulators.

**2000: Conservation of let-7 heterochronic regulatory RNA (Nature)**
Demonstrated evolutionary conservation of let-7 across animals.

**2001: Dicer in the maturation of let-7 small temporal RNA (Science)** ([PubMed](https://pubmed.ncbi.nlm.nih.gov/11452083/))
Linked RNAi machinery to miRNA maturation.

**2012: MicroRNAs and their targets (Nature Reviews Genetics)**
High-impact synthesis of miRNA targeting principles.

### Lab trajectory

> From foundational miRNA discovery and let-7 biology, toward increasingly systems-level studies of RNA regulation, aging, stress, transcript diversity, and RNA processing.

---

## Bottom line

For Amy Pasquinelli Lab themes, this repo serves as:

| Mode | Use case |
| --- | --- |
| **Literature only** | Review engine, mechanism mapper, dataset discovery, hypothesis ranking |
| **With dataset access** | Isoform analysis, target concordance scoring, cross-dataset replication, recovery module detection, poly(A)/translation integration |
| **Post-doc starting today** | Gap-finder for grants (1–2 days), paper alerts (½ day), hypothesis board (1–2 days), lab knowledge base (ongoing), manuscript checker (hours) |

The field is moving fast. FutureHouse's PaperQA2 already outperforms human researchers at literature retrieval in biology. Sakana AI's system already passes peer review. Karpathy's autoresearch loop is being adopted on consumer hardware worldwide.

**The question is no longer whether autonomous research tools will be useful in biology labs — it is how quickly labs like the Pasquinelli lab adopt them.**
