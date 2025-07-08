import matplotlib.pyplot as plt
import seaborn as sns

def plot_category_spending(df):
    category_totals = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    plt.figure(figsize=(10,5))
    sns.barplot(x=category_totals.index, y=category_totals.values)
    plt.xticks(rotation=45, ha='right')
    plt.title("Total Spending by Category")
    plt.ylabel("Amount")
    plt.tight_layout()
    plt.show()

def plot_monthly_trend(df):
    df['Month'] = df['Date'].dt.to_period('M').astype(str)
    monthly = df.groupby('Month')['Amount'].sum().reset_index()
    plt.figure(figsize=(10,5))
    sns.lineplot(x='Month', y='Amount', data=monthly, marker='o')
    plt.xticks(rotation=45)
    plt.title("Monthly Spending Trend")
    plt.tight_layout()
    plt.show()
