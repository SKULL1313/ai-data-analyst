import pandas as pd

def load_data():
    """Load transaction data from the CSV file."""
    return pd.read_csv("data/transactions.csv")


def calculate_total_revenue():
    """Calculate total revenue across all transactions."""
    df = load_data()
    total = df["revenue"].sum()
    return total


def revenue_by_product():
    """Calculate total revenue for each product."""
    df = load_data()
    
    summary = df.groupby("product")["revenue"].sum()
    
    return summary.sort_values(ascending=False)


def calculate_average_transaction():
    """Calculate the average revenue per transaction."""
    df = load_data()
    average = df["revenue"].mean()
    return average