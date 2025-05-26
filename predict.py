import pandas as pd
import joblib
from sklearn.metrics import mean_squared_error

def load_data(path):
    rows = []
    with open(path, 'r') as f:
        header = f.readline().strip().split(',')
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 7:
                # เติมค่า Open = 0.0 (หรือจะคำนวณจากค่าอื่นก็ได้)
                parts.insert(5, '0.0')
            if len(parts) == 8:
                rows.append(parts)

    df = pd.DataFrame(rows, columns=header)
    print("Fixed data shape:", df.shape)
    
    for col in ['Price', 'Close', 'High', 'Low', 'Open', 'Volume']:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Price', 'Close', 'High', 'Low', 'Volume'])
    
    print("Shape after dropna:", df.shape)
    
    if df.empty:
        raise ValueError("Dataframe is empty after cleaning. Please check the input file.")

    return df

def prepare_features(df):
    X = df[['Price', 'High', 'Low', 'Volume']]
    y = df['Close']
    return X, y

def predict_and_evaluate(model_path, data_path):
    model = joblib.load(model_path)
    df = load_data(data_path)
    X, y_true = prepare_features(df)
    y_pred = model.predict(X)
    mse = mean_squared_error(y_true, y_pred)
    print(f"Prediction MSE: {mse:.4f}")
    for i in range(5):
        print(f"True: {y_true.iloc[i]:.2f}, Predicted: {y_pred[i]:.2f}")

if __name__ == '__main__':
    model_path = 'model.joblib'
    data_path = 'data/stock_data.csv'
    predict_and_evaluate(model_path, data_path)
