import pandas as pd
import yfinance as yf
import talib

# โหลดข้อมูลหุ้น
df = yf.download('AAPL', start='2022-01-01', end='2023-12-31')
df = df[['Open', 'High', 'Low', 'Close']]
df.dropna(inplace=True)

# เตรียม dictionary ของ pattern
patterns = {
    "Doji": talib.CDLDOJI,
    "Hammer": talib.CDLHAMMER,
    "ShootingStar": talib.CDLSHOOTINGSTAR,
    "BullishEngulfing": talib.CDLENGULFING,
    "BearishEngulfing": talib.CDLENGULFING
}

# สร้าง DataFrame เก็บผล pattern แต่ละแท่ง (0/1)
labels_df = pd.DataFrame(index=df.index)

for name, func in patterns.items():
    result = func(
        df['Open'].values.reshape(-1),
        df['High'].values.reshape(-1),
        df['Low'].values.reshape(-1),
        df['Close'].values.reshape(-1)
    )
    if name == "BearishEngulfing":
        labels_df[name] = (result < 0).astype(int)
    elif name == "BullishEngulfing":
        labels_df[name] = (result > 0).astype(int)
    else:
        labels_df[name] = (result != 0).astype(int)

# สร้าง list สำหรับเก็บข้อมูล pattern ที่เกิดขึ้นจริง
pattern_events = []

# วนเช็กแต่ละแท่งใน labels_df
for date, row in labels_df.iterrows():
    for pattern_name, val in row.items():
        if val == 1:
            pattern_events.append({
                'Date': date.strftime('%Y-%m-%d'),
                'Pattern': pattern_name
            })

# สร้าง DataFrame ของ event pattern ที่เกิด
pattern_events_df = pd.DataFrame(pattern_events)

# เซฟไฟล์ CSV
pattern_events_df.to_csv('pattern_detected_events.csv', index=False)

print(f"บันทึกไฟล์ pattern_detected_events.csv จำนวน {len(pattern_events_df)} แถวเรียบร้อยแล้ว")
