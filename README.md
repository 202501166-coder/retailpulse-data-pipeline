# RetailPulse: Transaction Performance & Customer Intelligence Pipeline

RetailPulse is a Python-based data engineering and analytics project focused on processing retail transaction data, validating data quality, and exploring customer behavior and business performance.

The project is currently under development. Its goal is to build a modular ETL (Extract, Transform, Load) pipeline using Python, NumPy, and pandas.

## Project Objectives

Retail transaction datasets can contain missing values, duplicate records, inconsistent formats, and transactions that cannot be linked to valid customer records. RetailPulse aims to address these challenges through data validation, cleaning, financial auditing, and customer analytics.

Planned capabilities include:

- Loading and validating customer and transaction CSV files.
- Cleaning duplicate records, inconsistent text values, missing values, and date formats.
- Performing transaction and revenue calculations using vectorized NumPy and pandas operations.
- Identifying potentially inconsistent transactions and unmatched customer records.
- Analyzing regional sales, purchasing patterns, and customer lifetime value.
- Generating cleaned datasets and summarized business reports.
- Comparing vectorized operations with iterative approaches to explore performance differences.
- Testing data transformations and validating analytical results.

These capabilities will be implemented and tested incrementally.

## Tech Stack

- **Python 3.10+** — Core programming language.
- **pandas** — Data loading, cleaning, merging, and aggregation.
- **NumPy** — Numerical computation and vectorized operations.
- **pathlib** — Cross-platform filesystem path handling.
- **time** — Planned execution-time measurements.
- **Git and GitHub** — Version control and project hosting.

## Planned Project Structure

```text
retailpulse-data-pipeline/
├── data/
│   ├── raw/
│   │   ├── customers.csv
│   │   └── transactions.csv
│   └── processed/
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── cleaner.py
│   ├── vectorized_metrics.py
│   └── analytics.py
├── tests/
│   ├── __init__.py
│   └── test_pipeline_logic.py
├── logs/
├── .gitignore
├── requirements.txt
├── README.md
└── main.py
```

This represents the intended architecture. Additional files and directories will be added as development progresses.

## Development Roadmap

### Phase 1: Data Ingestion and Validation
- [ ] Resolve data paths reliably using pathlib.
- [ ] Validate input directories and required CSV files.
- [ ] Load customer and transaction datasets using pandas.
- [ ] Handle missing files, completely empty files, and empty datasets.
- [ ] Report dataset shapes and column names.

### Phase 2: Data Cleaning
- [ ] Standardize text fields and category values.
- [ ] Parse dates consistently and identify invalid values.
- [ ] Detect and handle duplicate records.
- [ ] Investigate missing values and apply suitable imputation strategies.

### Phase 3: Transaction and Financial Auditing
- [ ] Implement vectorized transaction and revenue calculations.
- [ ] Validate calculations against available transaction fields.
- [ ] Identify suspicious or inconsistent records.
- [ ] Compare vectorized calculations with iterative implementations.

### Phase 4: Customer and Business Analytics
- [ ] Join customer and transaction datasets.
- [ ] Detect transactions with unmatched customer records.
- [ ] Aggregate sales and transaction metrics by relevant business dimensions.
- [ ] Explore customer purchasing patterns and lifetime-value metrics.

### Phase 5: Testing and Reporting
- [ ] Add tests for data loading, validation, and analytical logic.
- [ ] Verify expected data shapes, data types, and calculation results.
- [ ] Export cleaned datasets and analytical summaries.
- [ ] Add structured logging and an execution summary.

## Getting Started

### Prerequisites

- Python 3.10 or later
- pip
- Git (optional)

### 1. Clone the Repository

Replace the placeholder with your actual GitHub repository URL.

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd retailpulse-data-pipeline
```

Alternatively, download the repository and open the project folder in PyCharm.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

On Linux or macOS:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

Install the core libraries:

```bash
python -m pip install pandas numpy
```

Once `requirements.txt` is available, dependencies can also be installed using:

```bash
pip install -r requirements.txt
```

### 4. Prepare the Input Data

Place the following CSV files in the `data/raw/` directory:

- `customers.csv`
- `transactions.csv`

Use synthetic or appropriately anonymized datasets when sharing the project publicly. Do not upload confidential customer information.

### 5. Run the Pipeline

Once the main entry point and required modules are implemented, run:

```bash
python main.py
```

**Note:** The complete pipeline is still under development. Execution instructions will be verified as the implementation progresses.

## Engineering Principles

- **Defensive programming:** Validate inputs and handle expected errors explicitly.
- **Modularity:** Separate data ingestion, cleaning, computation, and analytics.
- **Vectorization:** Prefer suitable NumPy and pandas operations over unnecessary Python-level loops.
- **Data integrity:** Validate assumptions before performing financial calculations.
- **Reproducibility:** Make processing steps understandable and repeatable.
- **Testing:** Verify important transformations and calculations with representative test cases.

## Learning Goals

This project is intended to develop practical skills in:

- Python programming and modular design.
- NumPy arrays and vectorized computation.
- pandas data manipulation and relational operations.
- ETL pipeline design and data quality validation.
- Financial and customer analytics.
- Testing, debugging, and Git-based version control.

## Project Status

**Status: In Development**

The current focus is building a reliable data-loading module with path validation, CSV ingestion, and clear error handling. Data cleaning, financial auditing, customer analytics, automated testing, and reporting will be implemented incrementally.

## Author

Developed as a hands-on learning project to strengthen practical Python data analytics and data engineering skills.
