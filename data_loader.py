from pathlib import Path
import pandas as pd
import os
import numpy as np
def load_raw_data(data_dir: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    # check dir exist or not
    if not data_dir.exists():
        raise FileNotFoundError(f"Directory not found: {data_dir}")
    # check its directory or not
    if not data_dir.is_dir():
        raise NotADirectoryError(f"Not a directory: {data_dir}")

    customers_path = data_dir / "customers.csv"
    transactionpath = data_dir / "transactions.csv"
    if not os.path.isfile(customers_path):
        raise FileNotFoundError(f"File not found: {customers_path}")
    if not os.path.isfile(transactionpath):
        raise FileNotFoundError(f"File not found: {transactionpath}")
    data_customer = pd.read_csv(customers_path)
    data_transaction = pd.read_csv(transactionpath)
    return data_customer, data_transaction

datadir = Path("data/raw")
data_customers, data_transactions = load_raw_data(datadir)
if data_customers.empty:
    raise ValueError("No customer data found")
if data_transactions.empty:
    raise ValueError("No transaction data found")
print(data_customers.head())
print(data_transactions.head())
shape_transtaction = data_transactions.shape
print(f"Transactions loaded successfully. Shape: {shape_transtaction}")
print(f"Customers loaded successfully. Shape: {data_customers.shape}")
