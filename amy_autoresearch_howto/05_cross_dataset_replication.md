# How-To: Automated Cross-Dataset Replication of Aging Gene Signatures

*Application 5 of 5 from the [Pasquinelli Autoresearch Playbook](../PASQUINELLI_AUTORESEARCH_README.md)*

## What this experiment does

Downloads and standardizes public *C. elegans* aging RNA-seq datasets from GEO, then scores each one using gene signatures derived from the Pasquinelli lab's own data. Autoresearch iterates overnight to check whether the lab's aging signatures replicate across independent datasets.

## Why it matters

Replication across independent datasets is one of the strongest forms of evidence in genomics. An automated system that pulls, normalizes, and scores external datasets against lab-internal signatures can massively accelerate validation work that might otherwise require a rotation student for months.

## Anchor paper

> Full-length direct RNA sequencing reveals extensive remodeling of RNA expression, processing and modification in aging *C. elegans*
> NAR, 2024. PMC: [PMC11662692](https://pmc.ncbi.nlm.nih.gov/articles/PMC11662692/)

## Potential collaborators

- **Matt Kaeberlein** (Optispan / formerly U. Washington) — aging biology and cross-species aging signatures
- **Sean Curran** (USC) — *C. elegans* aging, metabolism, and gene expression
- **Coleen Murphy** (Princeton) — *C. elegans* longevity, insulin signaling, and transcriptomics

## Prerequisites

1. This repo cloned and working
2. Python 3.10+ with `pandas`, `numpy`, `scipy`, `GEOparse`, `matplotlib`, `seaborn`, `scikit-learn`
3. Lab-derived aging gene signatures (differentially expressed genes from the 2024 paper)
4. Internet access for downloading GEO datasets

## Setup steps

### Step 1: Define lab-specific aging signatures

```python
# define_signatures.py
# Extract gene signatures from the lab's 2024 aging paper results

# Signature types to define:
# 1. "Aging UP" — genes significantly upregulated with age
# 2. "Aging DOWN" — genes significantly downregulated with age
# 3. "Isoform switching" — genes with significant isoform changes (from How-To #1)
# 4. "Processing decline" — genes showing RNA processing fidelity loss with age

# Example format:
signatures = {
    "aging_up": ["gene1", "gene2", "gene3", ...],      # from lab DE analysis
    "aging_down": ["gene4", "gene5", "gene6", ...],
    "isoform_switch": ["gene7", "gene8", ...],           # from How-To #1
    "processing_decline": ["gene9", "gene10", ...]
}
```

### Step 2: Build the GEO dataset catalog

```python
# find_aging_datasets.py
import GEOparse

# Known C. elegans aging RNA-seq datasets to check
datasets_to_check = [
    # Format: (GEO accession, description, expected samples)
    ("GSE63528", "Aging transcriptome Rangaraju 2015", "young vs old"),
    ("GSE46051", "Murphy lab aging timecourse", "multiple ages"),
    ("GSE100814", "Curran lab dietary restriction aging", "DR vs control x age"),
    # Add more as the agent discovers them via GEO search:
    # Search: "C. elegans aging RNA-seq" or "C. elegans lifespan transcriptome"
]

# The agent should also search for datasets using the Entrez API:
# from Bio import Entrez
# Entrez.email = "your_email"
# handle = Entrez.esearch(db="gds", term="C. elegans aging RNA-seq", retmax=50)
```

### Step 3: Configure program.md

```markdown
# Cross-Dataset Replication Agent

## Your role
You are a computational biologist who validates gene signatures across
independent public datasets. You specialize in meta-analysis and
reproducibility assessment.

## Task
1. Load the lab's aging gene signatures (UP, DOWN, isoform, processing)
2. Search GEO for C. elegans aging RNA-seq datasets (find at least 5-10)
3. For each external dataset:
   a. Download processed expression data (or raw counts if processed unavailable)
   b. Standardize gene identifiers to WormBase IDs
   c. Identify young vs. old samples (or equivalent age groups)
   d. Run differential expression (limma or DESeq2-style, or simple t-tests)
   e. Score each lab signature:
      - What fraction of "aging UP" genes are also up in this dataset?
      - What fraction of "aging DOWN" genes are also down?
      - Calculate a replication score: (concordant genes) / (testable genes)
   f. Compute a p-value for the replication score (vs. random gene sets)
4. Aggregate across datasets:
   - Overall replication rate per signature
   - Which genes replicate most consistently?
   - Which genes fail to replicate (dataset-specific)?
5. Generate forest plots and summary tables

## Iteration strategy
- Start with the easiest datasets (those with clear young/old labels)
- Add more complex datasets (multiple conditions, strains, interventions)
- Try different gene matching strategies (exact match, ortholog mapping)
- Vary the DE threshold for the external datasets
- Test robustness by removing one dataset at a time (leave-one-out)

## Output format
- CSV: dataset, signature, n_testable, n_concordant, replication_score, pvalue
- PNG: forest plot of replication scores across datasets
- PNG: heatmap of gene-level replication (genes × datasets)
- TXT: summary of which signatures replicate and which do not
```

### Step 4: Prepare the analysis script

```python
# cross_dataset_replication.py — starter template
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def load_signatures(filepath):
    """Load lab-specific gene signatures."""
    import json
    with open(filepath) as f:
        return json.load(f)

def download_geo_dataset(accession, destdir="data/geo/"):
    """Download and parse a GEO dataset."""
    import GEOparse
    gse = GEOparse.get_GEO(geo=accession, destdir=destdir)
    return gse

def extract_expression_matrix(gse):
    """Extract expression matrix from a GEO dataset."""
    # Handle both microarray and RNA-seq platforms
    for gsm_name, gsm in gse.gsms.items():
        # Get expression values
        pass  # Agent implements platform-specific extraction
    return expression_df, sample_metadata

def score_signature_replication(external_de, signature_genes, direction='up'):
    """Score how well a signature replicates in an external dataset."""
    testable = [g for g in signature_genes if g in external_de.index]
    if len(testable) == 0:
        return {'n_testable': 0, 'n_concordant': 0, 'score': np.nan, 'pvalue': np.nan}

    if direction == 'up':
        concordant = [g for g in testable if external_de.loc[g, 'log2fc'] > 0]
    else:
        concordant = [g for g in testable if external_de.loc[g, 'log2fc'] < 0]

    score = len(concordant) / len(testable)

    # P-value: binomial test against random expectation (50% concordant)
    pval = stats.binom_test(len(concordant), len(testable), 0.5,
                            alternative='greater')

    return {
        'n_testable': len(testable),
        'n_concordant': len(concordant),
        'score': score,
        'pvalue': pval
    }

def create_forest_plot(results_df, output_path):
    """Forest plot of replication scores across datasets."""
    fig, ax = plt.subplots(figsize=(10, len(results_df) * 0.4 + 2))

    y_positions = range(len(results_df))
    ax.barh(y_positions, results_df['score'], color='steelblue', alpha=0.7)
    ax.axvline(0.5, color='red', linestyle='--', label='Random expectation')

    ax.set_yticks(y_positions)
    ax.set_yticklabels(results_df['dataset'] + ' | ' + results_df['signature'])
    ax.set_xlabel('Replication Score (fraction concordant)')
    ax.set_title('Cross-Dataset Replication of Lab Aging Signatures')
    ax.legend()

    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()

if __name__ == "__main__":
    signatures = load_signatures("data/lab_signatures.json")

    # List of GEO datasets to test against
    geo_accessions = ["GSE63528", "GSE46051", "GSE100814"]

    all_results = []
    for accession in geo_accessions:
        print(f"Processing {accession}...")
        try:
            gse = download_geo_dataset(accession)
            expr, metadata = extract_expression_matrix(gse)
            # Run DE analysis and score signatures
            # ... (agent iterates on this)
        except Exception as e:
            print(f"  Failed: {e}")

    results_df = pd.DataFrame(all_results)
    results_df.to_csv("output/replication_scores.csv", index=False)
    create_forest_plot(results_df, "output/replication_forest.png")
```

### Step 5: Run autoresearch loop

```bash
# Install GEOparse if needed
pip install GEOparse

# Manual test
uv run python cross_dataset_replication.py

# Then agent mode for iterative refinement
```

### Step 6: Evaluate results

- **Replication rate:** What fraction of lab signatures replicate at >60% concordance?
- **Consistent genes:** Which specific genes replicate across ALL datasets?
- **Non-replicating genes:** Are these dataset-specific or biologically interesting?
- **Signature quality:** Which signature type (UP, DOWN, isoform, processing) replicates best?

## Expected outputs

| File | Description |
| --- | --- |
| `replication_scores.csv` | Score per signature per dataset |
| `replication_forest.png` | Forest plot of all replication scores |
| `gene_level_replication.csv` | Per-gene concordance across datasets |
| `gene_replication_heatmap.png` | Heatmap of gene × dataset concordance |
| `consistently_replicated.txt` | Genes that replicate in ≥80% of datasets |
| `dataset_catalog.csv` | All GEO datasets found and tested |

## What success looks like

- Lab aging signatures replicate significantly above chance (>60% concordance) in ≥3 independent datasets
- A core set of 20–50 genes replicate across ALL tested datasets (robust aging markers)
- "Isoform switching" and "processing decline" signatures show meaningful (if lower) replication
- The analysis reveals which parts of the aging transcriptome are universal vs. condition-specific

## Next steps

1. Use consistently-replicated genes as high-confidence aging markers for future studies
2. Cross-reference with miRNA target concordance ([How-To #2](02_mirna_target_concordance.md)) — are consistently-replicated aging genes also miRNA targets?
3. Build a "core aging response" gene set for the lab that is validated across multiple independent sources
4. Use non-replicating genes to identify dataset-specific biology worth investigating

---

## Integration across all 5 How-To experiments

The five experiments in this series are designed to work together:

```
How-To #1 (Isoform Shifts) ──→ feeds isoform-switching gene lists
                                     ↓
How-To #2 (Target Concordance) ──→ provides curated miRNA target lists
                                     ↓
How-To #3 (Poly(A)/Translation) ──→ identifies tail-length outliers
                                     ↓
How-To #4 (Recovery Modules) ──→ maps miRNAs to recovery gene programs
                                     ↓
How-To #5 (Cross-Dataset) ──→ validates everything across independent data
```

Each experiment produces outputs that feed into the others, creating a self-reinforcing evidence network. The autoresearch agent can be configured to run the full pipeline sequentially or to iterate on any single step.
