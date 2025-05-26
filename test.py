import pandas as pd
from analysis import calculate_return, plot_price

# โหลดข้อมูล
df = pd.read_csv('data/stock_data.csv')  # ปรับ path ตามจริง
df.columns = ['Date', 'Price', 'Close', 'High', 'Low', 'Volume']
df['Date'] = pd.to_datetime(df['Date'])
df[['Price', 'Close', 'High', 'Low', 'Volume']] = df[['Price', 'Close', 'High', 'Low', 'Volume']].apply(pd.to_numeric)

# วิเคราะห์ข้อมูล
df = calculate_return(df)

# แสดงกราฟ
plot_price(df)
