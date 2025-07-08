from sklearn.ensemble import IsolationForest
import pandas as pd
import numpy as np

def detect_anomalies(df):
    model = IsolationForest(contamination=0.03, random_state=42)
    df = df.copy()
    df['Amount_Log'] = df['Amount'].apply(lambda x: np.log1p(x))
    model.fit(df[['Amount_Log']])
    df['Anomaly'] = model.predict(df[['Amount_Log']])
    df['Anomaly'] = df['Anomaly'].apply(lambda x: "Unusual" if x == -1 else "Normal")
    return df.drop(columns=['Amount_Log'])
