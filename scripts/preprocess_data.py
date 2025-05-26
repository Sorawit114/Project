import pandas as pd

def preprocess_data(input_filename, output_filename):
    df = pd.read_csv(input_filename)
    df['Date'] = pd.to_datetime(df['Date'], utc=True)
    df['Date'] = df['Date'].map(pd.Timestamp.toordinal)
    df = df.dropna()
    df.to_csv(output_filename, index=False)
    print(f"Data processed and saved to '{output_filename}'")

if __name__ == "__main__":
    preprocess_data('data/raw/stock_data.csv', 'data/processed/processed_data.csv')
