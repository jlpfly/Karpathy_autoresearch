# How-To: Age-Dependent Isoform Shift Quantification

*Application 1 of 5 from the [Pasquinelli Autoresearch Playbook](../PASQUINELLI_AUTORESEARCH_README.md)*

## What this experiment does

Directly reanalyzes the 2024 direct RNA-seq aging data to build an age-stratified isoform usage matrix across all detected genes, then automatically flags genes where isoform switching correlates with age more strongly than overall expression change.

## Why it matters

The 2024 Pasquinelli lab paper reports age-associated changes in isoforms and RNA processing, but a systematic, gene-by-gene isoform-switching analysis can reveal candidates that expression-level analyses miss. Autoresearch can iterate over parameter choices overnight without human supervision.

## Anchor paper

> Full-length direct RNA sequencing reveals extensive remodeling of RNA expression, processing and modification in aging *C. elegans*
> NAR, 2024. PMC: [PMC11662692](https://pmc.ncbi.nlm.nih.gov/articles/PMC11662692/)

## Potential collaborators

- **Kin Fai Au** (Yale) — long-read RNA-seq methods and isoform analysis tools
- **Christopher Vollmers** (UC Santa Cruz) — direct RNA-seq and full-length transcript methods
- **Miten Jain** (Northeastern) — nanopore sequencing and RNA modification detection

## Prerequisites

1. This repo cloned and working (`uv sync`, `uv run prepare.py` completed successfully)
2. Python 3.10+ with `pandas`, `numpy`, `scipy`, `matplotlib`, `seaborn`
3. Access to the 2024 direct RNA-seq dataset (check GEO for the accession number from the paper)
4. Optional: `minimap2` and `FLAIR` or `IsoQuant` for long-read isoform quantification

## Setup steps

### Step 1: Download the dataset

```bash
# Find the GEO accession from the paper's data availability section
# Example (replace GSExxxxx with actual accession):
pip install GEOparse
python -c "
import GEOparse
gse = GEOparse.get_GEO(geo='GSExxxxx', destdir='./data/isoform_aging/')
print(gse.metadata)
"
```

### Step 2: Configure program.md for isoform analysis

Edit `program.md` to contain:

```markdown
# Isoform Shift Quantification Agent

## Your role
You are a computational biologist specializing in RNA isoform analysis.
You analyze long-read RNA-seq data to identify age-dependent isoform switching.

## Task
1. Load processed isoform quantification data (counts per isoform per sample)
2. Group samples by age (young, mid, old — use the paper's age groups)
3. For each gene with ≥2 detected isoforms:
   a. Calculate the dominant isoform fraction at each age
   b. Test whether isoform usage changes with age (chi-squared or Fisher's exact)
   c. Compare isoform-switching significance to overall expression change
4. Flag genes where isoform switching is significant but total expression is stable
5. Run GO enrichment on the flagged gene set
6. Output ranked tables and heatmaps

## Iteration strategy
- Start with lenient thresholds (p < 0.1), then tighten
- Try different age binning strategies (2-bin vs 3-bin vs continuous)
- Compare results with and without lowly-expressed isoforms filtered out
- Each iteration: save results, compare to previous, keep if improvement

## Output format
- CSV: gene, isoform_id, young_fraction, old_fraction, p_value, expression_change
- PNG: heatmap of top 50 switching genes
- TXT: summary statistics and GO enrichment results
```

### Step 3: Prepare the analysis script

Create a starter script that the agent will iterate on:

```python
# isoform_analysis.py — starter template for autoresearch iteration
import pandas as pd
import numpy as np
from scipy import stats

def load_isoform_counts(filepath):
    """Load isoform-level count matrix. Rows=isoforms, cols=samples."""
    return pd.read_csv(filepath, index_col=0)

def calculate_isoform_fractions(counts, gene_to_isoforms):
    """Convert raw counts to within-gene isoform fractions."""
    fractions = counts.copy()
    for gene, isoforms in gene_to_isoforms.items():
        gene_total = counts.loc[isoforms].sum(axis=0)
        gene_total = gene_total.replace(0, np.nan)
        fractions.loc[isoforms] = counts.loc[isoforms].div(gene_total, axis=1)
    return fractions

def test_isoform_switching(fractions, young_samples, old_samples, min_counts=10):
    """Test each gene for age-dependent isoform switching."""
    results = []
    # Group isoforms by gene, run chi-squared test on usage proportions
    # ... (agent iterates on this logic)
    return pd.DataFrame(results)

if __name__ == "__main__":
    # Agent modifies parameters and logic here
    counts = load_isoform_counts("data/isoform_counts.csv")
    # ... analysis pipeline
```

### Step 4: Run the autoresearch loop

```bash
# Single manual test run
uv run python isoform_analysis.py

# Then switch to agent mode:
# Point your Claude/Codex agent at program.md and let it iterate
# The agent will modify isoform_analysis.py, run it, evaluate results, and repeat
```

### Step 5: Evaluate results

After the agent runs overnight, check:

- **Top switching genes:** Do they include known aging-related isoform switches?
- **GO enrichment:** Are the flagged genes enriched for RNA processing, splicing, or known aging pathways?
- **Comparison to paper:** Do the results recapitulate findings from the original paper? Do they extend them?

## Expected outputs

| File | Description |
| --- | --- |
| `isoform_switching_ranked.csv` | All genes ranked by isoform-switching significance |
| `top50_heatmap.png` | Heatmap of the 50 strongest switching genes |
| `go_enrichment.csv` | GO terms enriched in the switching gene set |
| `experiment_log.txt` | Log of all iterations the agent tried |
| `summary.txt` | Plain-English summary of findings |

## What success looks like

- You identify 50–200 genes with significant isoform switching that is NOT explained by overall expression change
- The gene list includes known aging biology (splicing factors, RNA processing genes) plus novel candidates
- The results are reproducible across different threshold choices (robust, not threshold-dependent)

## Next steps after this experiment

1. Cross-reference switching genes with the lab's miRNA target lists
2. Check whether switching genes overlap with heat-shock recovery modules (see [How-To #4](04_stress_recovery_modules.md))
3. Validate top candidates with targeted RT-qPCR or long-read sequencing of specific loci
