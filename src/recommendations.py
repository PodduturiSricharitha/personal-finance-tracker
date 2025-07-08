def generate_recommendations(df):
    df = df.copy()
    df['Month'] = df['Date'].dt.to_period('M')

    recs = []

    # Top 1 category
    expenses = df[df["Transaction Type"] == "debit"]
    top_cat = expenses.groupby("Category")["Amount"].sum().idxmax()

    recs.append(f"Your highest spending category is **{top_cat.title()}**.")

    # Monthly spike detection
    monthly = df.groupby("Month")["Amount"].sum()
    this_month = monthly.iloc[-1]
    last_month = monthly.iloc[-2] if len(monthly) >= 2 else None
    if last_month and this_month > 1.25 * last_month:
        recs.append("Spending increased significantly this month compared to the last.")

    # Frequent anomaly warning
    if "Anomaly" in df.columns:
        unusual_count = (df['Anomaly'] == "Unusual").sum()
        if unusual_count > 3:
            recs.append(f"There are {unusual_count} unusual transactions to review.")

    return recs
