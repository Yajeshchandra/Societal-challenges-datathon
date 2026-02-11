# Diabetes Prediction from NHANES Questionnaire Data

**Course:** 42.17 — Societal Challenges Datathon · RWTH Aachen

---

## Overview

This project predicts **Type 2 Diabetes** using only self-reported questionnaire data from the [NHANES](https://www.cdc.gov/nchs/nhanes/index.htm) (National Health and Nutrition Examination Survey) — **no lab tests, no clinical measurements, no demographics**.

The goal is to demonstrate that a machine-learning model can identify diabetes risk from lifestyle, medical history, and functional indicators alone, making screening possible in low-resource settings where blood work is unavailable.

### Key Results

| Metric           | Value  |
|------------------|--------|
| ROC-AUC          | 0.921  |
| Recall (Diabetes)| 0.870  |
| F1 Score         | 0.543  |
| Balanced Accuracy| 0.859  |

- **Model:** CatBoost gradient boosting classifier
- **Features:** 46 variables across 15 NHANES questionnaire modules
- **Imbalance handling:** 4:1 undersampling + class weights
- **Threshold:** tuned for recall ≥ 87% (prioritising catching diabetic cases)
- **5-Fold CV AUC:** 0.934 ± 0.005

---

## How to Run

### 1. Setup

Install the [uv python package manager](https://docs.astral.sh/uv/#installation), then:

```bash
uv sync
```

### 2. Launch

**Jupyter Lab:**
```bash
uv run jupyter lab
```

**VS Code:**
Open any `.ipynb` and select the `.venv` kernel.

### 3. Run the Solution

Open **`main.ipynb`** and run all cells top to bottom. The notebook loads raw XPT files, cleans/derives features, trains the model, tunes the threshold, and produces all evaluation plots.

---

## File Structure

```
├── main.ipynb                  # Main solution — full pipeline & results
├── EDA_plots.ipynb             # EDA for feature selection process
│
├── EDA_missingness.ipynb       # EDA studying missingness patterns
├── EDA_correlation.ipynb       # EDA for initial modelling exploration
├── exploring.ipynb             # Feature selection & model selection process
│                                 (main.ipynb is the refined version of this)
│
├── data/
│   ├── raw/                    # NHANES .XPT files (source data)
│   ├── CSV/                    # Converted CSVs
│   └── extra/
│       ├── variables.csv       # Variable name mapping & descriptions
│       └── NHANES_DATA_CODEBOOK.md
│
├── main_focus/                 # Subset CSVs for key modules
├── lectures/                   # Course lecture notebooks
│
├── pyproject.toml              # Dependencies (managed by uv)
├── uv.lock                     # Locked dependency versions
└── README.md
```

### Main Files

| File | Purpose |
|------|---------|
| **`main.ipynb`** | End-to-end solution: data loading → cleaning → feature engineering → CatBoost training → threshold tuning → 5-fold CV → evaluation plots |
| **`EDA_plots.ipynb`** | Exploratory visualisations justifying feature selection across all 15 NHANES modules |

### Supporting Notebooks

| File | Purpose |
|------|---------|
| `EDA_missingness.ipynb` | Analysis of missing-value patterns and imputation strategy |
| `EDA_correlation.ipynb` | Correlation analysis and initial modelling experiments |
| `exploring.ipynb` | Iterative feature selection and model comparison (CatBoost vs XGBoost vs LightGBM). `main.ipynb` is the cleaned, final version of this work |

---

## Approach

1. **Data:** 15 NHANES questionnaire modules (audiometry, blood pressure history, functioning, medical conditions, mental health, smoking, weight history, prescriptions, etc.)
2. **Target:** Binary diabetes classification (prediabetes cases excluded)
3. **Cleaning:** Sentinel value removal (999/777 patterns), mode/median imputation (≤30% missing), masking indicators (30–50%), drop (>50%)
4. **Feature Engineering:** BMI (imperial), weight change, comorbidity count, oral health composite, functional score
5. **Model:** CatBoost with `nan_mode="Min"`, early stopping on AUC, recall-optimised threshold via precision-recall curve
