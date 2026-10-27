# Boston House Price Analysis

This project helps analysts and developers predict median home values in Boston-area census tracts from historical housing data. It walks through cleaning a raw two-line-per-record dataset, training several regression models, and comparing their performance with clear metrics and charts.

## System Design

```mermaid
flowchart LR
  RawData["Raw Boston Data (boston.txt)"]
  Notebook["Data Preparation Notebook"]
  CleanData[("Clean Dataset (boston_housing.csv)")]
  Modeling["Model Training & Evaluation"]
  Outputs["Charts & Results"]

  RawData --> Notebook
  Notebook --> CleanData
  CleanData --> Modeling
  Modeling --> Outputs

  style RawData fill:#1e1b4b,stroke:#6366f1,stroke-width:2px,color:#fff
  style Notebook fill:#1e1b4b,stroke:#6366f1,stroke-width:2px,color:#fff
  style CleanData fill:#0f172a,stroke:#3b82f6,stroke-width:2px,color:#fff
  style Modeling fill:#2e1065,stroke:#8b5cf6,stroke-width:2px,color:#fff
  style Outputs fill:#2e1065,stroke:#8b5cf6,stroke-width:2px,color:#fff
```

## Features

- **Raw data reconstruction**: The notebook loads `./boston.txt` and rebuilds each record from its original two-line format into a clean 506 x 14 table, then saves it as `boston_housing.csv`.
- **Model training pipeline**: It trains a mean baseline, Linear Regression, Decision Tree, and Random Forest on an 80/20 train-test split with a fixed random seed.
- **Cross-validation comparison**: It evaluates every model with shuffled 5-fold cross-validation so the winner is not just the result of one lucky split.
- **Reproducible reporting**: It exports a results table and saves actual-vs-predicted and CV-comparison charts to the `images/` folder.

### Data preparation workflow

```mermaid
flowchart TD
  Start(["Open notebook"])
  Load["Load raw text file"]
  Rebuild["Rebuild split records"]
  Validate["Check shape and missing values"]
  Save["Save cleaned CSV"]

  Start --> Load --> Rebuild --> Validate --> Save

  style Start fill:#1e1b4b,stroke:#6366f1,stroke-width:2px,color:#fff
  style Load fill:#1e1b4b,stroke:#6366f1,stroke-width:2px,color:#fff
  style Rebuild fill:#2e1065,stroke:#8b5cf6,stroke-width:2px,color:#fff
  style Validate fill:#2e1065,stroke:#8b5cf6,stroke-width:2px,color:#fff
  style Save fill:#0f172a,stroke:#3b82f6,stroke-width:2px,color:#fff
```

### Model training and evaluation workflow

```mermaid
sequenceDiagram
  actor Analyst
  participant Notebook
  participant Data as "Training Data"
  participant Models as "Regression Models"
  participant Metrics as "Evaluation Metrics"

  Analyst->>Notebook: Run analysis cells
  Notebook->>Data: Load cleaned dataset
  Data->>Models: Train baseline, linear, tree, forest
  Models->>Metrics: Calculate MSE, RMSE, R2
  Metrics->>Notebook: Return comparison table
  Notebook->>Analyst: Show actual vs predicted plots
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Adeyiwolasuccess/Codveda_Internship.git
cd Codveda_Internship
```

2. Make sure Python 3.8 or newer is installed.
3. Install the required packages:

```bash
pip install pandas numpy scikit-learn matplotlib jupyter
```

## Usage

1. Start Jupyter Notebook:

```bash
jupyter notebook
```

2. Open `./House_Price_Analysis.ipynb` and run the cells from top to bottom.
3. The notebook will:
   - read `./boston.txt`
   - create `./boston_housing.csv`
   - train and compare four models
   - save `results_table.csv`
   - save charts to `images/actual_vs_predicted.png` and `images/cv_comparison.png`

After running the notebook, the final results table will look like this:

```text
                     MSE  RMSE  R2 (test)  CV R2 mean  CV R2 std
Baseline (mean)    75.05  8.66     -0.023      -0.011      0.007
Linear Regression  22.78  4.77      0.689       0.712      0.031
Decision Tree       8.98  3.00      0.878       0.729      0.131
Random Forest       8.01  2.83      0.891       0.871      0.031
```

The Random Forest comes out on top, with a typical prediction error of around $2,830 on median home values.

## Technologies Used

| Technology | Description |
|---|---|
| [Python](https://www.python.org/) | Core language for data processing and modeling |
| [pandas](https://pandas.pydata.org/) | Data loading, cleaning, and tabular analysis |
| [NumPy](https://numpy.org/) | Numerical operations and array handling |
| [scikit-learn](https://scikit-learn.org/) | Regression models, cross-validation, and metrics |
| [Matplotlib](https://matplotlib.org/) | Visualization of predictions and model comparisons |
| [Jupyter Notebook](https://jupyter.org/) | Interactive analysis environment |

## Contributing

Contributions are welcome. If you want to add a new model, improve the visualizations, or clean up the data pipeline, feel free to open an issue or pull request. Keep changes focused and include a short explanation of what you changed and why.

## Author

- LinkedIn: [Success Adeyiwola](https://linkedin.com/in/successadeyiwola)
- X: [jathom48](https://x.com/jathom48)

## Badges

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=matplotlib&logoColor=white)](https://matplotlib.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)

[![Readme was generated by Dokugen](https://img.shields.io/badge/Readme%20was%20generated%20by-Dokugen-brightgreen)](https://dokugen.samueltuoyo.com)