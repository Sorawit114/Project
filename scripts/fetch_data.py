import yfinance as yf
import pandas as pd
from datetime import datetime
import os


def fetch_sp500_data(start_date="1900-01-01", end_date=None, save_path="../Project/data/raw/stock_data.csv"):
    if end_date is None:
        end_date = datetime.now().strftime('%Y-%m-%d')

    print(f"Fetching S&P 500 data from {start_date} to {end_date}...")
    ticker = "^GSPC"  # S&P 500 index symbol on Yahoo Finance

    data = yf.download(ticker, start=start_date, end=end_date)

    if data.empty:
        print("No data fetched. Please check the ticker or date range.")
        return

    # Ensure save directory exists
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    data.reset_index(inplace=True)
    data.to_csv(save_path, index=False)
    print(f"Data saved to {save_path}")


if __name__ == "__main__":
    fetch_sp500_data()
