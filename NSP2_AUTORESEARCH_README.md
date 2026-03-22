# Autoresearch Playbook for the NSP2 / microRNA Repression Paper

This guide does two things in one place:

1. consolidates the updated training-output explanation, including the new two-line live terminal display
2. shows how this repo could be used as a **safe, high-level computational autoresearch workflow** around the paper:

> Naeli P, Zhang X, Snell PH, Chatterjee S, Kamran M, Ladak RJ, Orr N, Duchaine T, Sonenberg N, Jafarnejad SM.  
> *The SARS-CoV-2 protein NSP2 enhances microRNA-mediated translational repression.*  
> *J Cell Sci.* 2023. DOI: `10.1242/jcs.261286`

This file is intentionally **not** a wet-lab protocol and **not** an instruction set for pathogen manipulation. The examples below stay at the level of literature synthesis, computational prioritization, hypothesis organization, and experiment planning support.

## Source links reviewed for this guide

- DOI landing page: <https://doi.org/10.1242/jcs.261286>
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/37732428/>
- PMC full text: <https://pmc.ncbi.nlm.nih.gov/articles/PMC10617620/>

## What the paper says, in plain English

Based on the paper abstract and PMC full text:

- the authors report that SARS-CoV-2 NSP2 enhances miRNA-mediated **translational repression**
- NSP2 appears to connect to the miRNA silencing machinery through **GIGYF2**, and AGO2 is brought into that picture indirectly through GIGYF2
- the effect was shown across multiple reporter systems, including miR-20a, miR-92, and let-7-related setups
- the paper frames the mechanism as stronger repression at the **translation** level, rather than simply causing broad mRNA loss
- the authors connect this to host-gene-expression control and impaired antiviral response, including the previously discussed interferon pathway context

Very short summary:

> The paper argues that NSP2 helps the virus push host cells toward stronger miRNA-guided shutdown of selected host translation programs.

## How the updated terminal output should be read

When `uv run train.py` is active in a real terminal, the live progress area now has **two lines**.

### Line 1: changing numbers

```text
step: 00369 | done:  35.0% | loss: 2.372307 | lrm: 1.00 | dt:  296ms | tok/sec: 110,832 | mfu: 8.7% | epoch: 1 | remaining: 195s
```

### Line 2: built-in explainer words

```text
study round | run done | wrongness | learning pace | time for 1 study | text speed | GPU busy | data lap | time left
```

### What each field means

| Field | Plain-English meaning |
| --- | --- |
| `step` | How many training updates have happened |
| `done` | How far through the 5-minute run you are |
| `loss` | How wrong the model currently is |
| `lrm` | How strong the learning-rate schedule is right now |
| `dt` | How long one training step took |
| `tok/sec` | How fast the run is processing text |
| `mfu` | Roughly how hard the GPU is being utilized |
| `epoch` | Which pass through the dataset the run is on |
| `remaining` | Approximate time left in the run |

### What the top startup lines mean

Before the live two-line display begins, the run prints model and run settings such as:

- parameter counts like `wte`, `value_embeds`, and `total`
- `Estimated FLOPs per token`
- `Time budget: 300s`
- `Gradient accumulation steps: 2`
- compile-mode messages such as the Triton fallback on Windows

In plain English, that startup block answers:

- how big the model is
- how much math each token costs
- how long the run is supposed to last
- whether the model is using compiled fast paths or plain eager mode

### What the final scorecard means

At the end you will see values such as:

- `val_bpb`
- `training_seconds`
- `peak_vram_mb`
- `mfu_percent`
- `total_tokens_M`

The simplest way to read those is:

- lower `val_bpb` is better
- `training_seconds` tells you whether the timed run actually completed
- `peak_vram_mb` tells you whether the config fit the GPU
- `total_tokens_M` tells you how much text the model processed

## How this repo could be deployed for this paper

In this repo, "deploying autoresearch" does **not** have to mean changing viruses or doing biology in the loop. A safer and more realistic meaning is:

- load a focused text corpus
- tune `program.md` so the agent behaves like a narrow research assistant
- let the agent iteratively read, summarize, compare, hypothesize, and rank ideas overnight
- keep the output as notes, structured tables, candidate hypotheses, and reproducible prompts

## Ten safe, high-level deployment examples

### 1. Literature triage for the NSP2-GIGYF2-AGO2 axis

Use autoresearch to collect and summarize papers about NSP2, GIGYF2, 4EHP/EIF4E2, AGO2, and miRISC.

Useful output:

- a one-page map of who binds whom
- a list of agreements vs contradictions across papers
- a ranked list of the most central host factors

### 2. Figure-to-table extraction from the paper and related papers

Use the system to turn reporter-assay figures, captions, and supplement notes into structured tables.

Useful output:

- condition
- reporter type
- cell line
- miRNA family
- WT versus mutant control
- reported direction of effect

This makes the paper easier to compare against later studies without manually re-reading each figure.

### 3. miRNA family prioritization

Point the workflow at papers and datasets involving miR-20a, miR-92, let-7, and related host miRNAs in coronavirus infection contexts.

Useful output:

- a ranked list of miRNA families most repeatedly linked to NSP2-relevant phenotypes
- notes on whether the evidence is translational, transcript-level, or indirect

### 4. Host-target ranking for antiviral and inflammatory genes

Use autoresearch to build a shortlist of host mRNAs that could be most plausibly affected if NSP2 strengthens miRNA-mediated translational repression.

Useful output:

- interferon-pathway candidates
- cytokine-regulation candidates
- cell-cycle or stress-response candidates
- confidence notes tied to citations

### 5. Translation-versus-mRNA-effect evidence classifier

Train the workflow to separate claims about:

- translational repression
- mRNA destabilization
- deadenylation
- general shutdown of cap-dependent translation

Useful output:

- a labeled evidence matrix showing what kind of regulation each paper actually measured

That is especially relevant here because the paper emphasizes translation-level repression.

### 6. Cell-line sensitivity comparison

Use autoresearch to compare how the reported effect behaves across HEK293, HEK293T, U87, and any later follow-up cell models.

Useful output:

- where the signal looks strongest
- where dependencies on GIGYF2 or 4EHP were tested
- which models appear underexplored

### 7. Replication checklist builder

Use the system to generate a replication-oriented checklist from the paper.

Useful output:

- which controls were critical
- which knockouts mattered
- which reporter constructs separated translation effects from mRNA-abundance effects
- which results look robust versus more context-sensitive

This is useful for planning and review, even before anyone touches an experiment.

### 8. Public-dataset reanalysis queue

Use autoresearch to find public RNA-seq, Ribo-seq, proteomics, or CLIP-style datasets that could be re-examined in light of the paper's mechanism.

Useful output:

- candidate datasets
- likely relevance score
- matched keywords
- which parts of the paper each dataset could help test computationally

### 9. Variant-monitoring watchlist for NSP2

At a high level, autoresearch can monitor new literature and public annotations for NSP2 sequence changes and ask whether any are discussed in connection with host-translation or host-silencing pathways.

Useful output:

- a literature watchlist
- a sequence-annotation watchlist
- a "mentioned in mechanism papers / not mentioned" tracker

This keeps the work at the surveillance and interpretation level, not the design level.

### 10. Living evidence dashboard for decision support

Use autoresearch as a rolling dashboard that answers:

- what is strongly supported
- what is weakly supported
- what is still missing
- what would be the next best computational or literature task

Useful output:

- a running evidence summary
- an open-questions list
- a "next papers to read" queue
- a prioritized hypothesis board

## A practical way to adapt this repo for this topic

If you wanted to use this repo as a narrow research assistant around this paper, the safest practical setup would be:

1. build a text corpus from the paper, its references, related reviews, and later follow-up papers
2. rewrite `program.md` so the agent focuses on mechanism mapping, contradiction finding, evidence grading, and hypothesis ranking
3. keep outputs structured as summaries, tables, and candidate questions
4. avoid prompting for procedural virology or pathogen-engineering instructions

## Suggested prompt direction for this domain

Good autoresearch directions here would look like:

- "Map the evidence for NSP2 -> GIGYF2 -> AGO2 / miRISC -> translational repression."
- "Separate translation-level evidence from transcript-level evidence."
- "Rank the most likely host pathways affected according to the cited papers."
- "Find contradictions, caveats, and weak points in the current evidence."

## Bottom line

This repo is best deployed for this paper as a **paper-reading, evidence-structuring, and hypothesis-ranking engine**, not as a lab automation tool.

That is the safest and most realistic way to use autoresearch here:

- read faster
- compare papers more consistently
- keep a structured memory of the mechanism
- surface the next best questions
