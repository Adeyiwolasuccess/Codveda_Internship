# Codveda Data Science Internship

A portfolio of data science projects completed during the Codveda Technologies Data Science Internship, covering web scraping, exploratory analysis, regression, classification, clustering, time series forecasting and NLP.

## Overview

The internship is split into three levels of increasing difficulty. Each task is a self-contained notebook or script with its own findings, so you can open any folder and follow the analysis from raw data to conclusions.

## Projects at a Glance

| Level | Task | Technique | Headline result |
|---|---|---|---|
| 1 | [Web scraping](./Level_1/web_scraping) | requests, BeautifulSoup | 1,000 books and 100 quotes exported to CSV and JSON |
| 1 | [House price EDA](./Level_1/house_prices_eda_analysis.ipynb) | Summary stats, correlation | RM and LSTAT are the strongest price drivers |
| 2 | [House price regression](./Level_2/House_Price_Analysis.ipynb) | Linear, tree, forest | Random Forest: test R² 0.891, CV R² 0.871 |
| 2 | [Customer churn](./Level_2/churn_Analysis.ipynb) | SQL, clustering, classification | Random Forest: CV F1 0.883, ROC AUC 0.990 |
| 3 | [Time series forecasting](./Level_3/Time_Series_Analysis_final.ipynb) | Holt-Winters, SARIMA | SARIMA(2,1,0)(0,1,1,12) beats both baselines on the hold-out window |
| 3 | [Sentiment classification](./Level_3/nlp_sentiment_classification.ipynb) | TF-IDF, Logistic Regression, Naive Bayes | 84 to 86% accuracy, macro F1 about 0.65 |

## Repository Structure

```text
Codveda_Internship/
├── Level_1/
│   ├── web_scraping/            # books and quotes scrapers (+ own README)
│   ├── house_Prediction_DataSet.csv
│   └── house_prices_eda_analysis.ipynb
├── Level_2/
│   ├── House_Price_Analysis.ipynb
│   ├── churn_Analysis.ipynb
│   ├── boston.txt / boston_housing.csv
│   ├── churn.db                 # SQLite database used for SQL queries
│   ├── results_table.csv
│   └── images/
└── Level_3/
    ├── Time_Series_Analysis_final.ipynb
    ├── nlp_sentiment_classification.ipynb
    ├── Sentiment_dataset.csv
    ├── data/RSAFSNA_snapshot.csv
    └── images/
```

## Level 1

### Web Scraping Toolkit

Two scripts collect structured data and export it to CSV and JSON, with a shape, preview and missing-value check after each run.
- `scraper.py` crawls the full book catalogue (title, price, rating, availability, link).
- `dynamic_scraper.py` extracts quotes embedded in JavaScript data objects.

See the [scraping README](./Level_1/web_scraping/README.md) for details and run instructions.

### House Price Exploratory Data Analysis

Exploration of the Boston Housing data (506 rows, 14 numeric columns, no missing values) using pandas, matplotlib and seaborn.

Key findings:
- **Skew:** CRIM (skew 5.2), ZN and B are heavily skewed. A log transform on CRIM would help in modelling.
- **Target cap:** MEDV is capped at 50, affecting about 19 houses, so top-end values are understated.
- **Strongest relationships with price:** RM (r = 0.70) and LSTAT (r = −0.74). LSTAT is curved, and its Spearman correlation (−0.85) is stronger than its Pearson value.
- **Multicollinearity:** RAD and TAX correlate at 0.91, and INDUS, NOX, AGE, DIS, TAX and RAD form one correlated cluster.
- **Outliers:** CRIM has the most. They are flagged rather than removed.

## Level 2

### Boston House Price Prediction

Rebuilds the raw two-line-per-record file into a clean table, then compares four models on an 80/20 split and shuffled 5-fold cross-validation.

| Model | RMSE | R² (test) | CV R² mean |
|---|---|---|---|
| Baseline (mean) | 8.66 | −0.023 | −0.011 |
| Linear Regression | 4.77 | 0.689 | 0.712 |
| Decision Tree | 3.00 | 0.878 | 0.729 |
| **Random Forest** | **2.83** | **0.891** | **0.871** |

Random Forest is both the most accurate and the most stable (CV std 0.031, against 0.131 for the Decision Tree).

### Credit Card Customer Churn

Analysis of 10,127 BankChurners customers (about 16% churned), combining SQL, clustering and classification.
- **SQL (SQLite):** card tier is a weak churn signal, while churned customers have about 33% lower transaction amounts and 35% fewer transactions than retained ones.
- **Data leakage:** two pre-computed Naive Bayes columns in the source file were dropped because they are predictions of the target.
- **Clustering:** K-Means with PCA to explore customer segments.
- **Models:** Logistic Regression, Decision Tree, Random Forest and KNN, evaluated with a stratified split and 5-fold CV.
- **Imbalance handling:** class weighting and threshold tuning improved Logistic Regression recall at a cost in precision.
- **Result:** Random Forest reached CV F1 0.883 and ROC AUC 0.990. A stratified dummy baseline scored F1 0.164 and ROC AUC 0.501.
- **Leakage check:** removing the two strongest features (`Total_Trans_Amt`, `Total_Trans_Ct`) dropped ROC AUC to 0.918, a real but moderate fall, so they are strong predictors rather than leaks.

## Level 3

### Time Series Forecasting: US Retail Sales

Monthly US retail sales (FRED series RSAFSNA, not seasonally adjusted, 1992 to 2026). The notebook covers decomposition, stationarity tests (ADF), moving averages, Holt-Winters, ACF/PACF, SARIMA, and a 12-month forecast.
- The series is non-stationary until log transformed and differenced.
- SARIMA(2,1,0)(0,1,1,12), chosen by AIC, has the lowest error on the 24-month hold-out, ahead of Holt-Winters and a seasonal naive baseline.
- A rolling-origin test across eight 12-month windows shows SARIMA and Holt-Winters are comparable, and both beat the baseline.

### NLP: Social Media Sentiment Classification

Classifies 727 short posts into Positive, Negative and Neutral after mapping 191 emotion labels to three polarity groups.
- Preprocessing: emoji to text, hashtag splitting, URL removal, negation-aware stopword handling, lemmatisation, TF-IDF.
- Both Logistic Regression and Complement Naive Bayes reach 84 to 86% accuracy and a macro F1 of about 0.65, against a majority baseline of 67% accuracy and 0.27 macro F1.
- Positive and Negative are learned well (F1 0.86 to 0.91). Neutral is weak (F1 0.14 to 0.21) because it has only 40 examples and mixed content.

See the [Level 3 README](./Level_3/README.md) for the NLP pipeline details.

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/Adeyiwolasuccess/Codveda_Internship.git
cd Codveda_Internship
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv

# macOS / Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Download the NLTK resources used by the sentiment notebook:

```python
import nltk
nltk.download("stopwords")
nltk.download("wordnet")
```

5. Launch Jupyter and open any notebook:

```bash
jupyter notebook
```

Notes:
- Run each notebook from its own folder, because data files are loaded with relative paths.
- `churn_Analysis.ipynb` downloads its dataset from Kaggle through `kagglehub`.
- `Time_Series_Analysis_final.ipynb` downloads live data from FRED, so newer months may change the numbers slightly. A snapshot is saved in `Level_3/data/`.
- Set `DATA_PATH` in the first code cell of the sentiment notebook if your CSV is elsewhere.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core language |
| pandas, NumPy | Data manipulation |
| matplotlib, seaborn | Visualisation |
| scikit-learn | Models, clustering, metrics, cross-validation |
| statsmodels | Decomposition, ADF test, Holt-Winters, SARIMA |
| NLTK, emoji | Text preprocessing |
| SQLite | SQL analysis of the churn data |
| requests, BeautifulSoup4 | Web scraping |
| Jupyter Notebook | Interactive analysis |

## Author

**Success Adeyiwola**
- LinkedIn: [successadeyiwola](https://linkedin.com/in/successadeyiwola)
- X: [jathom48](https://x.com/jathom48)

## Badges

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
