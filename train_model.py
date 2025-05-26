import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression

def load_data(path):
    df = pd.read_csv(path)
    # สมมติคอลัมน์จริงในไฟล์มี 7 ตัว เช่น
    # Date, Price, Close, High, Low, Volume, Ticker
    df.columns = ['Date', 'Price', 'Close', 'High', 'Low', 'Volume', 'Ticker']
    df['Date'] = pd.to_datetime(df['Date'])
    for col in ['Price', 'Close', 'High', 'Low', 'Volume']:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df = df.dropna()
    return df

def prepare_features(df):
    X = df[['Price', 'High', 'Low', 'Volume']]
    y = df['Close']
    return X, y

def train_and_save_model(data_path, model_path):
    df = load_data(data_path)
    X, y = prepare_features(df)
    model = LinearRegression()
    model.fit(X, y)
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == '__main__':
    data_path = 'data/stock_data.csv'  # เปลี่ยนเป็นไฟล์ข้อมูลของคุณ
    model_path = 'model.joblib'
    train_and_save_model(data_path, model_path)
