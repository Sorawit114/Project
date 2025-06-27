import pandas as pd
import yfinance as yf
import talib
from pattern_list import all_patterns as patterns  # Dictionary ของฟังก์ชันแพทเทิร์น

# โหลดข้อมูลหุ้น AAPL
df = yf.download('AAPL', start='2022-01-01', end='2023-12-31')

# ถ้ามี MultiIndex (เช่น 'AAPL', 'Open') ให้ลดระดับ
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.droplevel(1)

# ใช้เฉพาะคอลัมน์ที่ต้องใช้
df = df[['Open', 'High', 'Low', 'Close']].dropna()

# เพิ่มคอลัมน์แสดงสีแท่งเทียน (Red = แท่งลง, Green = แท่งขึ้น)
df['CandleColor'] = ['Red' if close < open_ else 'Green'
                     for open_, close in zip(df['Open'], df['Close'])]

# เตรียม DataFrame สำหรับเก็บ label ของแต่ละแพทเทิร์น
labels_df = pd.DataFrame(index=df.index)

# ตรวจจับ pattern ด้วย TA-Lib
for name, func in patterns.items():
    result = func(df['Open'].values,
                  df['High'].values,
                  df['Low'].values,
                  df['Close'].values)

    labels_df[name] = [f"{name}_Bullish" if v > 0 else
                       f"{name}_Bearish" if v < 0 else ""
                       for v in result]

# รวมแพทเทิร์นที่ตรวจพบลงใน list
pattern_events = [
    {
        'Date': date.strftime('%Y-%m-%d'),
        'Pattern': val,
        'CandleColor': df.loc[date, 'CandleColor']
    }
    for date, row in labels_df.iterrows()
    for val in row.values if val
]

# สร้าง DataFrame และบันทึกไฟล์
pattern_events_df = pd.DataFrame(pattern_events)
pattern_events_df.to_csv('pattern_detected_events.csv', index=False)

print(f"บันทึกไฟล์ pattern_detected_events.csv จำนวน {len(pattern_events_df)} แถวเรียบร้อยแล้ว")
