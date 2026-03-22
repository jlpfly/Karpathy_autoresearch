# How-To: Poly(A)-Tail Length and Translation Efficiency Integration

*Application 3 of 5 from the [Pasquinelli Autoresearch Playbook](../PASQUINELLI_AUTORESEARCH_README.md)*

## What this experiment does

Systematically correlates poly(A)-tail length measurements with translational output across transcripts. Identifies outlier transcripts where the expected positive correlation between tail length and translation breaks down — these outliers are often the most interesting biology.

## Why it matters

The relationship between poly(A)-tail length and translation is known to be complex and context-dependent. The 2022 PABP paper from the Pasquinelli lab showed that nuclear and cytoplasmic PABPs favor distinct transcripts and isoforms. An automated sweep across all transcripts can identify outlier transcripts that challenge simple models of tail-length → translation efficiency.

## Anchor paper

> Nuclear and Cytoplasmic poly(A) binding proteins (PABPs) favor distinct transcripts and isoforms
> NAR, 2022. PMC: [PMC9071453](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9071453/)

## Potential collaborators

- **Joel Richter** (UMass Medical) — poly(A)-tail regulation and translational control
- **Wendy Gilbert** (Yale) — ribosome profiling and translational regulation
- **Marvin Wickens** (U. Wisconsin) — poly(A)-binding proteins and 3' UTR biology

## Prerequisites

1. This repo cloned and working
2. Python 3.10+ with `pandas`, `numpy`, `scipy`, `matplotlib`, `seaborn`, `statsmodels`
3. Poly(A)-tail length measurements (from PAL-seq, TAIL-seq, Nanopore direct RNA-seq, or similar)
4. Translation efficiency data (from Ribo-seq, polysome profiling, or reporter assays)

## Setup steps

### Step 1: Identify and obtain data

```text
Data sources to check:
1. 2022 PABP paper supplementary data (PABP-associated transcripts + properties)
2. 2024 direct RNA-seq paper (Nanopore-measured poly(A)-tail lengths)
3. Public Ribo-seq datasets for C. elegans (GEO search: "C. elegans ribosome profiling")
4. TAIL-seq or PAL-seq datasets if available
```

### Step 2: Configure program.md

```markdown
# Poly(A) / Translation Integration Agent

## Your role
You are a computational biologist who integrates poly(A)-tail length data
with translational efficiency measurements to find regulatory outliers.

## Task
1. Load poly(A)-tail length data (per-transcript median tail lengths)
2. Load translation efficiency data (TE = Ribo-seq RPKM / RNA-seq RPKM)
3. For each transcript with both measurements:
   a. Plot tail length vs. TE
   b. Fit a linear or loess regression
   c. Calculate residuals (distance from expected TE given tail length)
   d. Flag outliers: transcripts with much higher or lower TE than expected
4. Classify outliers:
   - "over-translated": short tail but high TE (tail-independent translation?)
   - "under-translated": long tail but low TE (repressed despite long tail?)
5. Run GO enrichment on each outlier class
6. Check whether outliers are enriched for known miRNA targets
7. Check PABP binding status (from 2022 paper) of outlier transcripts

## Iteration strategy
- Start with simple linear regression, then try loess/lowess
- Vary the outlier threshold (1.5σ, 2σ, 3σ from regression line)
- Try with and without filtering for lowly-expressed transcripts
- Separate analysis by developmental stage or age if data permits
- Compare nuclear-PABP-bound vs. cytoplasmic-PABP-bound subsets

## Output format
- CSV: transcript, tail_length, TE, expected_TE, residual, outlier_class
- PNG: scatter plot with regression line and highlighted outliers
- PNG: GO enrichment dot plots for each outlier class
- TXT: summary narrative
```

### Step 3: Prepare the analysis script

```python
# polya_translation.py — starter template
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

def load_tail_lengths(filepath):
    """Load poly(A)-tail length measurements per transcript."""
    df = pd.read_csv(filepath)
    # Expected columns: transcript_id, median_tail_length
    return df

def load_translation_efficiency(filepath):
    """Load translation efficiency (TE) values."""
    df = pd.read_csv(filepath)
    # Expected columns: transcript_id, ribo_rpkm, rna_rpkm, TE
    # If TE not pre-computed: TE = ribo_rpkm / rna_rpkm
    if 'TE' not in df.columns:
        df['TE'] = df['ribo_rpkm'] / df['rna_rpkm'].replace(0, np.nan)
    return df

def integrate_and_find_outliers(tails, te, sigma_threshold=2.0):
    """Merge tail length and TE data, fit regression, find outliers."""
    merged = tails.merge(te, on='transcript_id', how='inner')
    merged = merged.dropna(subset=['median_tail_length', 'TE'])

    # Log-transform for better regression behavior
    merged['log_tail'] = np.log2(merged['median_tail_length'].clip(lower=1))
    merged['log_TE'] = np.log2(merged['TE'].clip(lower=0.001))

    # Fit linear regression
    slope, intercept, r, p, se = stats.linregress(merged['log_tail'], merged['log_TE'])
    merged['expected_log_TE'] = intercept + slope * merged['log_tail']
    merged['residual'] = merged['log_TE'] - merged['expected_log_TE']

    # Flag outliers
    res_std = merged['residual'].std()
    merged['outlier_class'] = 'normal'
    merged.loc[merged['residual'] > sigma_threshold * res_std, 'outlier_class'] = 'over-translated'
    merged.loc[merged['residual'] < -sigma_threshold * res_std, 'outlier_class'] = 'under-translated'

    print(f"Regression: slope={slope:.3f}, R²={r**2:.3f}, p={p:.2e}")
    print(f"Outliers: {(merged['outlier_class'] != 'normal').sum()} / {len(merged)}")

    return merged, slope, intercept, r

def plot_results(merged, slope, intercept):
    """Scatter plot with regression line and outlier highlights."""
    fig, ax = plt.subplots(figsize=(10, 8))
    colors = {'normal': '#cccccc', 'over-translated': '#e74c3c', 'under-translated': '#3498db'}

    for cls, color in colors.items():
        subset = merged[merged['outlier_class'] == cls]
        ax.scatter(subset['log_tail'], subset['log_TE'], c=color, alpha=0.5, label=cls, s=10)

    x_line = np.linspace(merged['log_tail'].min(), merged['log_tail'].max(), 100)
    ax.plot(x_line, intercept + slope * x_line, 'k--', linewidth=1)

    ax.set_xlabel('log2(poly(A) tail length)')
    ax.set_ylabel('log2(Translation Efficiency)')
    ax.set_title('Poly(A) Tail Length vs. Translation Efficiency')
    ax.legend()
    plt.tight_layout()
    plt.savefig('output/polya_vs_TE.png', dpi=150)
    plt.close()

if __name__ == "__main__":
    tails = load_tail_lengths("data/tail_lengths.csv")
    te = load_translation_efficiency("data/translation_efficiency.csv")
    merged, slope, intercept, r = integrate_and_find_outliers(tails, te, sigma_threshold=2.0)
    plot_results(merged, slope, intercept)
    merged.to_csv("output/polya_te_outliers.csv", index=False)
```

### Step 4: Run autoresearch loop

```bash
uv run python polya_translation.py
# Then switch to agent mode for iterative refinement
```

### Step 5: Evaluate

- Do "over-translated" outliers include known cap-independent translation candidates?
- Do "under-translated" outliers include known miRNA-repressed transcripts?
- Does PABP binding status (nuclear vs. cytoplasmic) predict outlier class?

## Expected outputs

| File | Description |
| --- | --- |
| `polya_te_outliers.csv` | All transcripts with tail length, TE, residuals, and outlier class |
| `polya_vs_TE.png` | Scatter plot with regression and outlier highlights |
| `go_over_translated.csv` | GO enrichment for over-translated outliers |
| `go_under_translated.csv` | GO enrichment for under-translated outliers |
| `pabp_overlap.txt` | PABP binding status of outlier transcripts |

## What success looks like

- Clear global positive correlation between tail length and TE (validating the approach)
- Meaningful outlier classes that are enriched for biologically interpretable GO terms
- Over-translated outliers enriched for stress-response or IRES-containing transcripts
- Under-translated outliers enriched for known miRNA targets

## Next steps

1. Check whether outlier status changes with age (combine with [How-To #1](01_isoform_shift_quantification.md))
2. Test whether miRNA target concordance scores (from [How-To #2](02_mirna_target_concordance.md)) predict under-translation
3. Investigate whether PABP isoform preference explains outlier behavior
