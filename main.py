
import os
import pandas as pd
import numpy as np

data_customers = pd.read_csv("data/raw/customers.csv")
data_transactions = pd.read_csv("data/raw/transactions.csv")

print(data_customers.columns)
print(data_transactions.columns)
