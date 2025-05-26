import yfinance as yf
import pandas as pd
import os

from Indicators import add_technical_indicators, add_trend_label, plot_stock
from Train import train_model

def download_and_clean_data(symbols):
    os.makedirs("data", exist_ok=True)
    for symbol in symbols:
        try:
            print(f"📥 กำลังดึงข้อมูล: {symbol}")
            data = yf.download(symbol, period="5y", interval="1d")
            if data.empty:
                print(f"⚠️ ไม่พบข้อมูลสำหรับ {symbol}")
                continue
            file_path = f"data/{symbol.replace('.', '_')}.csv"
            data.to_csv(file_path)
            print(f"✅ บันทึกข้อมูลแล้ว: {file_path}\n")
        except Exception as e:
            print(f"❌ เกิดข้อผิดพลาดกับ {symbol}: {e}")

    # Clean missing data
    for filename in os.listdir("data"):
        if filename.endswith(".csv"):
            path = os.path.join("data", filename)
            df = pd.read_csv(path)
            df = df.dropna()  # หรือใช้ df.fillna(method="ffill")
            df.to_csv(path, index=False)
            print(f"🧹 ล้างข้อมูล: {filename} → คงเหลือ {df.shape[0]} แถว")

def process_and_train(ticker):
    df = pd.read_csv(f"data/{ticker.replace('.', '_')}.csv")
    print(df.head())  # ดูข้อมูลแถวแรก ๆ
    print(df.dtypes)  # ตรวจสอบชนิดข้อมูลแต่ละคอลัมน์

    # ถ้า Date ยังไม่ใช่ datetime ให้แปลงก่อน
    if not pd.api.types.is_datetime64_any_dtype(df['Date']):
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    df.set_index('Date', inplace=True)

    # ตรวจสอบ col 'Close' ว่าถูกต้องหรือไม่
    df['Close'] = pd.to_numeric(df['Close'], errors='coerce')  # แปลงเป็นตัวเลข ถ้าแปลงไม่ได้จะเป็น NaN

    print(df['Close'].unique())  # ตรวจสอบค่าที่มีใน Clos

    df.dropna(inplace=True)  # ลบแถวที่มี NaN

    df = add_technical_indicators(df)
    df = add_trend_label(df)

    model = train_model(df)
    return model


if __name__ == "__main__":
    # โหลดรายชื่อหุ้น
    with open("stock_list.txt", "r") as f:
        symbols = [line.strip() for line in f if line.strip()]

    # ดาวน์โหลดข้อมูลและล้างข้อมูลขาดหาย
    download_and_clean_data(symbols)

    # รัน pipeline สำหรับแต่ละหุ้น (ถ้าต้องการ)
    for ticker in symbols:
        print(f"\n🚀 เริ่มประมวลผลหุ้น: {ticker}")
        model = process_and_train(ticker)
