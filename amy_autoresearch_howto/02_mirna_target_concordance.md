# How-To: Cross-Dataset miRNA Target Concordance Scoring

*Application 2 of 5 from the [Pasquinelli Autoresearch Playbook](../PASQUINELLI_AUTORESEARCH_README.md)*

## What this experiment does

Pulls miRNA target predictions from multiple databases (TargetScan, miRDB, published CLIP/CLASH datasets), then cross-references them against differential expression or translational efficiency data from Pasquinelli lab experiments to build a lab-specific concordance score for each predicted target.

## Why it matters

Target prediction databases disagree frequently. TargetScan, miRDB, and CLIP-based datasets each have different biases. An automated system that scores targets by how well they match the lab's own functional data produces a curated, lab-specific target list that is far more actionable than any single prediction tool.

## Anchor papers

- 2023 miR-238/239ab paper: [DOI:10.1371/journal.pgen.1011055](https://doi.org/10.1371/journal.pgen.1011055)
- 2012 NRG review on miRNA targeting: Pasquinelli AE, *Nat Rev Genet* 2012
- 2022 PABP paper for translational data context

## Potential collaborators

- **David Bartel** (MIT / Whitehead) — TargetScan developer, foundational miRNA targeting rules
- **Markus Hafner** (NIH/NIAMS) — CLIP/PAR-CLIP methods for direct target identification
- **Chi-Wing Chow** (Albert Einstein) — miRNA target validation in aging models

## Prerequisites

1. This repo cloned and working
2. Python 3.10+ with `pandas`, `numpy`, `requests`, `matplotlib`, `venn` (or `matplotlib-venn`)
3. Internet access for downloading prediction databases (or pre-downloaded files)
4. Lab-specific expression or translation data (RNA-seq, Ribo-seq, or reporter data)

## Setup steps

### Step 1: Download prediction databases

```python
# download_targets.py
import requests
import pandas as pd

# TargetScan — C. elegans conserved targets
# Download from https://www.targetscan.org/worm_52/
# File: Predicted_Targets_Context_Scores.default_predictions.txt

# miRDB — C. elegans predictions
# Download from https://mirdb.org/download.html

# For CLIP data: check GEO for published ALG-1/ALG-2 CLIP datasets in C. elegans
# Key datasets: Zisoulis et al. 2010, Grosswendt et al. 2014
```

### Step 2: Configure program.md

```markdown
# miRNA Target Concordance Agent

## Your role
You are a computational biologist who integrates miRNA target predictions
from multiple sources and scores them against experimental data.

## Task
1. Load target predictions from TargetScan, miRDB, and CLIP datasets
2. Normalize gene identifiers across databases (WormBase IDs preferred)
3. For each predicted target:
   a. Count how many databases predict it (1, 2, or 3+)
   b. Check if it appears in the lab's differential expression data
   c. If expression data shows the expected direction (target UP when miRNA DOWN, or vice versa), add concordance points
   d. Weight by prediction confidence score from each database
4. Produce a final concordance score per target per miRNA
5. Generate Venn diagrams showing database overlap
6. Output ranked target lists

## Iteration strategy
- First pass: simple overlap counting
- Second pass: add confidence weighting
- Third pass: add expression-direction concordance
- Fourth pass: separate by miRNA family and check family-specific patterns
- Compare each iteration's output to identify stable high-confidence targets

## Output format
- CSV: miRNA, target_gene, targetscan_score, mirdb_score, clip_evidence, expression_concordance, final_score
- PNG: Venn diagrams per miRNA family
- TXT: summary of top 20 targets per miRNA with evidence narrative
```

### Step 3: Prepare the analysis script

```python
# target_concordance.py — starter template
import pandas as pd
import numpy as np
from collections import defaultdict

def load_targetscan(filepath):
    """Load and parse TargetScan predictions."""
    df = pd.read_csv(filepath, sep='\t')
    # Standardize columns: miRNA, target_gene, score
    return df[['miRNA_family', 'Gene_Symbol', 'context++_score']].rename(
        columns={'miRNA_family': 'mirna', 'Gene_Symbol': 'target', 'context++_score': 'ts_score'}
    )

def load_mirdb(filepath):
    """Load and parse miRDB predictions."""
    df = pd.read_csv(filepath, sep='\t', header=None, names=['mirna', 'target', 'score'])
    return df

def load_clip_targets(filepath):
    """Load CLIP-identified targets."""
    df = pd.read_csv(filepath)
    df['clip_evidence'] = True
    return df

def load_expression_data(filepath):
    """Load lab expression data (log2FC + padj)."""
    return pd.read_csv(filepath)

def score_concordance(targetscan, mirdb, clip, expression):
    """Build concordance score across all sources."""
    # Merge all predictions
    all_targets = set(targetscan['target']) | set(mirdb['target'])

    results = []
    for target in all_targets:
        row = {'target': target}
        # Database overlap score
        row['in_targetscan'] = target in targetscan['target'].values
        row['in_mirdb'] = target in mirdb['target'].values
        row['in_clip'] = target in clip['target'].values if clip is not None else False
        row['db_count'] = sum([row['in_targetscan'], row['in_mirdb'], row['in_clip']])

        # Expression concordance
        expr_match = expression[expression['gene'] == target]
        if len(expr_match) > 0:
            row['log2fc'] = expr_match.iloc[0]['log2FoldChange']
            row['padj'] = expr_match.iloc[0]['padj']
            # Concordance: target should be DOWN if miRNA is active
            row['direction_concordant'] = row['log2fc'] < 0
        else:
            row['log2fc'] = np.nan
            row['padj'] = np.nan
            row['direction_concordant'] = None

        # Final score (agent iterates on weighting)
        row['concordance_score'] = row['db_count'] * 10
        if row['direction_concordant']:
            row['concordance_score'] += 20
        if row.get('padj') and row['padj'] < 0.05:
            row['concordance_score'] += 15

        results.append(row)

    return pd.DataFrame(results).sort_values('concordance_score', ascending=False)

if __name__ == "__main__":
    # Agent modifies file paths, scoring weights, and filtering thresholds
    ts = load_targetscan("data/targetscan_predictions.txt")
    mirdb = load_mirdb("data/mirdb_predictions.txt")
    clip = load_clip_targets("data/clip_targets.csv")
    expr = load_expression_data("data/lab_expression.csv")

    results = score_concordance(ts, mirdb, clip, expr)
    results.to_csv("output/concordance_scores.csv", index=False)
    print(f"Scored {len(results)} targets. Top 10:")
    print(results.head(10)[['target', 'db_count', 'direction_concordant', 'concordance_score']])
```

### Step 4: Run the autoresearch loop

```bash
# Test manually first
uv run python target_concordance.py

# Then agent mode — point Claude/Codex at program.md
# The agent iterates on scoring weights, filtering, and miRNA-family grouping
```

### Step 5: Evaluate results

- **Venn diagrams:** How much overlap exists between databases? Low overlap = high value of concordance scoring
- **Top targets:** Do high-concordance targets include known, validated miRNA targets?
- **Expression check:** What fraction of top targets show the expected expression direction?
- **Family patterns:** Do different miRNA families have different concordance profiles?

## Expected outputs

| File | Description |
| --- | --- |
| `concordance_scores.csv` | All targets with concordance scores |
| `venn_overlap.png` | Venn diagrams of database overlap |
| `top20_per_mirna.txt` | Top 20 targets per miRNA family |
| `concordance_summary.txt` | Statistics and key findings |
| `experiment_log.txt` | Agent iteration history |

## What success looks like

- You produce a curated target list where the top 50 targets have ≥2 database predictions AND expression concordance
- Known validated targets appear near the top (sanity check)
- Novel high-concordance targets emerge that the lab hasn't tested yet
- The scoring is robust to reasonable changes in weights (not fragile)

## Next steps

1. Validate top novel targets with luciferase reporter assays or qPCR
2. Cross-reference with isoform switching results from [How-To #1](01_isoform_shift_quantification.md)
3. Check whether high-concordance targets are enriched in aging pathways from [How-To #5](05_cross_dataset_replication.md)
