import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])

    df['Category'] = df['Category'].str.strip().str.lower()
    df['Transaction Type'] = df['Transaction Type'].str.strip().str.lower()
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    df = df.dropna(subset=['Amount'])

    df = df.drop_duplicates()

    if 'Month' in df.columns:
        df = df.drop(columns=['Month'])

    return df

