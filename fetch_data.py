import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start_date, end_date):
    stock = yf.Ticker(ticker)
    df = stock.history(start=start_date, end=end_date)
    df['Ticker'] = ticker
    df.reset_index(inplace=True)
    df = df[['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Ticker']]
    df.columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Ticker']
    return df

def save_to_csv(df, filename):
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    tickers = ['AAPL', 'GOOGL', 'AMZN', 'MSFT', 'TSLA']
    all_data = pd.DataFrame()

    for ticker in tickers:
        df = fetch_stock_data(ticker, '2020-01-01', '2023-01-01')
        all_data = pd.concat([all_data, df])

    save_to_csv(all_data, 'stock_data.csv')
    print("Data fetched and saved to 'stock_data.csv'")
