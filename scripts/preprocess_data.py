import pandas as pd
import os

input_path = 'data/raw/stock_data.csv'
output_path = 'data/processed/processed_data.csv'
os.makedirs(os.path.dirname(output_path), exist_ok=True)

df = pd.read_csv(input_path)
df['Date'] = pd.to_datetime(df['Date'], utc=True)
df['Date'] = df['Date'].map(pd.Timestamp.toordinal)
df = df.dropna()
df.to_csv(output_path, index=False)
print("Data processed and saved to 'data/processed/processed_data.csv'")