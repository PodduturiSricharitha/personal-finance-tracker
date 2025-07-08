# Personal Finance Tracker with Spending Insights

A Python-based system that analyzes personal spending, detects unusual transactions, and provides smart insights to help you manage money better.

---

## Features

- Visualize spending by category and month  
- Detect unusual (anomalous) transactions  
- Get intelligent recommendations based on your data  
- Clean and standardize messy transaction data  
## How to Run

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
2. **Run with your CSV file**
   ```bash
   python main.py data/transactions.csv
Make sure your CSV includes these columns:
Date, Description, Amount, Transaction Type, Category, Account Name

## Sample Output
  ```bash
  Loading and preprocessing data...
  Cleaned file saved as data/cleaned_transactions.csv
  Generating insights...
  Running anomaly detection...
  Recommendations:
   - Your highest spending category is **Credit Card Payment**.
   - There are 23 unusual transactions to review.
  ```
## Dataset Used
  https://www.kaggle.com/datasets/entrepreneurlife/personal-finance
