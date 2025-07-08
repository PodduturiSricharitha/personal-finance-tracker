import sys
import os
from src.data_preprocessing import load_data, preprocess_data
from src.visualization import plot_category_spending, plot_monthly_trend
from src.anomaly_detection import detect_anomalies
from src.recommendations import generate_recommendations

if __name__ == "__main__":
    #file input
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = "data/transactions.csv"

    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        sys.exit(1)

    print("Loading and preprocessing data...")
    df = load_data(file_path)
    clean_df = preprocess_data(df)

    output_path = "data/cleaned_transactions.csv"
    clean_df.to_csv(output_path, index=False)
    print(f"Cleaned file saved as {output_path}")

    print("Generating insights...")
    plot_category_spending(clean_df)
    plot_monthly_trend(clean_df)

    print("Running anomaly detection...")
    df_with_anomalies = detect_anomalies(clean_df)

    print("Recommendations:")
    recs = generate_recommendations(df_with_anomalies)
    for r in recs:
        print(" -", r)
