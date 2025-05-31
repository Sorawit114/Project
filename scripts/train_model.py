import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import joblib
import os

# Load and preprocess data
def load_data(csv_path, sequence_length=60):
    df = pd.read_csv(csv_path)
    df = df[['Date', 'Close']]
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(df[['Close']])

    X, y = [], []
    for i in range(sequence_length, len(scaled_data)):
        X.append(scaled_data[i-sequence_length:i, 0])
        y.append(scaled_data[i, 0])

    X, y = np.array(X), np.array(y)
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))
    return X, y, scaler

# Build LSTM model
def build_model(input_shape):
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=input_shape))
    model.add(LSTM(units=50))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Train and save model
def train_and_save(csv_path, model_path, scaler_path):
    X, y, scaler = load_data(csv_path)
    model = build_model((X.shape[1], 1))
    model.fit(X, y, epochs=10, batch_size=32)

    model.save(model_path)
    joblib.dump(scaler, scaler_path)
    print(f"Model saved to {model_path}, Scaler saved to {scaler_path}")

if __name__ == "__main__":
    raw_csv = "../data/raw/stock_data.csv"
    model_out = "../models/stock_lstm_model.h5"
    scaler_out = "../models/stock_scaler.pkl"
    os.makedirs("../models", exist_ok=True)
    train_and_save(raw_csv, model_out, scaler_out)
