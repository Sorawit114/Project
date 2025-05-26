import pandas as pd
import os

def calculate_indicators(df):
    # ตรวจสอบว่าคอลัมน์ Close และ Volume มีอยู่จริงไหม
    if 'Close' not in df.columns or 'Volume' not in df.columns:
        raise ValueError("❌ ไม่พบคอลัมน์ Close หรือ Volume")

    # แปลงคอลัมน์ที่ต้องใช้ให้เป็น float
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')
    df['Volume'] = pd.to_numeric(df['Volume'], errors='coerce')

    # ลบข้อมูลที่ไม่สามารถแปลงได้ (NaN)
    df = df.dropna(subset=['Close', 'Volume'])

    # Indicators
    df['MA5'] = df['Close'].rolling(window=5).mean()
    df['MA10'] = df['Close'].rolling(window=10).mean()
    df['MA20'] = df['Close'].rolling(window=20).mean()

    delta = df['Close'].diff()
    gain = delta.where(delta > 0, 0).rolling(window=14).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))

    ema12 = df['Close'].ewm(span=12, adjust=False).mean()
    ema26 = df['Close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = ema12 - ema26
    df['MACD_signal'] = df['MACD'].ewm(span=9, adjust=False).mean()
    df['MACD_hist'] = df['MACD'] - df['MACD_signal']

    df['Daily_Return'] = df['Close'].pct_change()
    df['Volume_Change_Pct'] = df['Volume'].pct_change()

    return df

def process_all_csv(data_dir="data"):
    for file in os.listdir(data_dir):
        if file.endswith(".csv"):
            path = os.path.join(data_dir, file)
            try:
                df = pd.read_csv(path)
                df = calculate_indicators(df)
                df = df.dropna()
                df.to_csv(path, index=False)
                print(f"✅ เพิ่ม indicators และบันทึก: {file} ({df.shape[0]} แถว)")
            except Exception as e:
                print(f"⚠️ เกิดข้อผิดพลาดในไฟล์ {file}: {e}")

if __name__ == "__main__":
    process_all_csv()
