import pandas as pd

df = pd.read_csv('data/AAPL.csv', skiprows=1)

print(df.columns)  # ดูคอลัมน์ที่ได้

# แก้ชื่อคอลัมน์ให้ตรงกับจำนวนจริง
df.columns = ['Date', 'Price', 'Close', 'High', 'Low', 'Volume']

df['Date'] = pd.to_datetime(df['Date'])

for col in ['Price', 'Close', 'High', 'Low', 'Volume']:
    df[col] = pd.to_numeric(df[col])

print(df.dtypes)
print(df.head())
