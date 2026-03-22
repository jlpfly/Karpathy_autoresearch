# How-To: Stress-Recovery Time-Series Gene Module Detection

*Application 4 of 5 from the [Pasquinelli Autoresearch Playbook](../PASQUINELLI_AUTORESEARCH_README.md)*

## What this experiment does

Uses heat-shock recovery data from the 2021 Pasquinelli lab paper (and any time-series experiments from the lab) to cluster genes into co-regulated modules based on their recovery dynamics, then automatically maps known miRNA targets onto those modules to identify which miRNAs control which recovery programs.

## Why it matters

Recovery dynamics are harder to analyze than simple stress/control comparisons. Most studies look at "stress vs. normal," but the 2021 paper specifically focused on the **recovery phase** — what happens after the stress is removed. Automated clustering + miRNA target overlay can reveal which miRNAs are likely controlling which recovery gene programs.

## Anchor paper

> Recovery from Heat Shock Requires the MicroRNA Pathway in *C. elegans*
> PLoS Genetics, 2021. PMC: [PMC8370650](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8370650/)

## Potential collaborators

- **Gary Bhatt** — heat-shock biology and stress granule dynamics
- **Morimoto lab** (Northwestern) — proteostasis and heat-shock response in *C. elegans*
- **Jessica Tyler** (Weill Cornell) — chromatin and stress recovery

## Prerequisites

1. This repo cloned and working
2. Python 3.10+ with `pandas`, `numpy`, `scipy`, `scikit-learn`, `matplotlib`, `seaborn`
3. Time-series expression data from heat-shock recovery experiments
4. miRNA target lists (from TargetScan or from [How-To #2](02_mirna_target_concordance.md))

## Setup steps

### Step 1: Obtain time-series data

```text
Data sources:
1. 2021 heat-shock recovery paper — check GEO supplementary data
2. Any lab-internal time-course experiments (0h, 2h, 4h, 8h, 24h post-heat-shock)
3. Public C. elegans heat-shock datasets from GEO
   Search: "C. elegans heat shock time course RNA-seq"
```

### Step 2: Configure program.md

```markdown
# Stress-Recovery Module Detection Agent

## Your role
You are a computational biologist specializing in time-series gene expression
analysis and gene regulatory module detection.

## Task
1. Load time-series expression data from heat-shock recovery experiments
2. Normalize and filter: keep genes with detectable expression at ≥2 time points
3. Cluster genes by their temporal recovery profile using multiple methods:
   a. K-means (try k=4,6,8,10,12)
   b. Hierarchical clustering with dynamic tree cutting
   c. Soft clustering (e.g., Mfuzz) to allow genes in multiple modules
4. For each detected module:
   a. Plot the average temporal profile
   b. Run GO enrichment
   c. Count how many genes are predicted targets of each miRNA
   d. Test whether any miRNA's targets are enriched in the module (hypergeometric test)
5. Identify "miRNA-controlled recovery modules" — modules significantly enriched for specific miRNA targets
6. Focus especially on miR-85 targets (highlighted in the paper)

## Iteration strategy
- Try different numbers of clusters (k)
- Compare clustering algorithms
- Test with different normalization methods (z-score, quantile, VST)
- Try adding a lag component (some recovery may be delayed)
- Check whether results change when restricting to protein-coding genes only

## Output format
- CSV: gene, module_id, temporal_profile (comma-separated values per time point)
- CSV: module_id, enriched_miRNAs, enrichment_p_value, GO_terms
- PNG: temporal profile plots per module (one subplot per module)
- PNG: heatmap of all genes grouped by module
- TXT: summary of miRNA-module associations
```

### Step 3: Prepare the analysis script

```python
# stress_recovery_modules.py — starter template
import pandas as pd
import numpy as np
from scipy import stats
from scipy.cluster.hierarchy import linkage, fcluster
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

def load_timeseries(filepath):
    """Load time-series expression matrix. Rows=genes, columns=timepoints."""
    df = pd.read_csv(filepath, index_col=0)
    return df

def normalize_profiles(df, method='zscore'):
    """Normalize each gene's profile across time points."""
    if method == 'zscore':
        scaler = StandardScaler()
        normalized = pd.DataFrame(
            scaler.fit_transform(df.T).T,
            index=df.index, columns=df.columns
        )
    elif method == 'minmax':
        normalized = df.sub(df.min(axis=1), axis=0).div(
            df.max(axis=1) - df.min(axis=1), axis=0
        )
    return normalized.dropna()

def cluster_genes(normalized, n_clusters=8, method='kmeans'):
    """Cluster genes by temporal profile."""
    if method == 'kmeans':
        km = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        labels = km.fit_predict(normalized.values)
    elif method == 'hierarchical':
        Z = linkage(normalized.values, method='ward')
        labels = fcluster(Z, t=n_clusters, criterion='maxclust') - 1
    return labels

def test_mirna_enrichment(module_genes, mirna_targets, background_size):
    """Hypergeometric test for miRNA target enrichment in a module."""
    overlap = len(set(module_genes) & set(mirna_targets))
    module_size = len(module_genes)
    target_size = len(mirna_targets)

    pval = stats.hypergeom.sf(overlap - 1, background_size, target_size, module_size)
    fold_enrichment = (overlap / module_size) / (target_size / background_size) if target_size > 0 else 0

    return overlap, fold_enrichment, pval

def plot_modules(normalized, labels, n_clusters):
    """Plot average temporal profile per module."""
    fig, axes = plt.subplots(2, (n_clusters + 1) // 2, figsize=(16, 8))
    axes = axes.flatten()
    timepoints = normalized.columns

    for i in range(n_clusters):
        module_genes = normalized.iloc[labels == i]
        mean_profile = module_genes.mean(axis=0)
        std_profile = module_genes.std(axis=0)

        axes[i].fill_between(range(len(timepoints)),
                             mean_profile - std_profile,
                             mean_profile + std_profile,
                             alpha=0.3)
        axes[i].plot(range(len(timepoints)), mean_profile, 'b-', linewidth=2)
        axes[i].set_title(f'Module {i} (n={len(module_genes)})')
        axes[i].set_xticks(range(len(timepoints)))
        axes[i].set_xticklabels(timepoints, rotation=45)

    plt.tight_layout()
    plt.savefig('output/recovery_modules.png', dpi=150)
    plt.close()

if __name__ == "__main__":
    # Load data
    ts = load_timeseries("data/heat_shock_recovery_timeseries.csv")

    # Normalize
    norm = normalize_profiles(ts, method='zscore')

    # Cluster
    n_clusters = 8  # Agent iterates on this
    labels = cluster_genes(norm, n_clusters=n_clusters)

    # Plot
    plot_modules(norm, labels, n_clusters)

    # Test miRNA enrichment per module
    mirna_targets = pd.read_csv("data/mirna_targets.csv")  # From How-To #2
    # ... enrichment testing per module per miRNA

    print(f"Clustered {len(norm)} genes into {n_clusters} modules")
```

### Step 4: Run autoresearch loop

```bash
uv run python stress_recovery_modules.py
# Then agent mode for iterative refinement of clustering and enrichment
```

### Step 5: Evaluate results

- **Module profiles:** Do modules show distinct temporal patterns (early recovery, late recovery, sustained, oscillating)?
- **miR-85 enrichment:** Is miR-85 target enrichment concentrated in specific recovery modules (as the paper would predict)?
- **GO enrichment:** Do module GO terms match expected biology (proteostasis, chaperones, translation, autophagy)?
- **Robustness:** Do key module–miRNA associations persist across different k values?

## Expected outputs

| File | Description |
| --- | --- |
| `recovery_modules.png` | Temporal profiles per module |
| `module_assignments.csv` | Gene-to-module mapping |
| `mirna_module_enrichment.csv` | miRNA enrichment p-values per module |
| `module_go_terms.csv` | GO enrichment per module |
| `heatmap_all_genes.png` | Full heatmap grouped by module |

## What success looks like

- You identify 6–12 distinct recovery temporal modules
- At least 2–3 modules are significantly enriched for specific miRNA targets
- miR-85 targets cluster in modules with profiles consistent with the paper's findings
- Module GO terms reveal biologically interpretable recovery programs

## Next steps

1. Check whether recovery modules overlap with age-dependent isoform switching genes ([How-To #1](01_isoform_shift_quantification.md))
2. Test whether module membership predicts poly(A)-tail behavior ([How-To #3](03_polya_translation_integration.md))
3. Compare recovery modules across heat-shock vs. oxidative stress vs. infection
