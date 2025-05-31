import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from tensorflow.keras.models import load_model
from scripts.fetch_data import fetch_sp500_data
from datetime import datetime
import os

# Paths
DATA_PATH = "data/raw/stock_data.csv"
MODEL_PATH = "models/stock_lstm_model.h5"
SCALER_PATH = "models/stock_scaler.pkl"

st.title("S&P 500 Trend Prediction App")

# Section: Load or Fetch Data
if st.button("📥 Load latest S&P 500 data"):
    fetch_sp500_data(save_path=DATA_PATH)
    st.success("Data fetched and saved!")

# Show raw data
if os.path.exists(DATA_PATH):
    df = pd.read_csv(DATA_PATH)
    st.subheader("📊 Recent Data")
    st.dataframe(df.tail(100))

# Predict future price
if st.button("📈 Predict next price"):
    if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
        model = load_model(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)

        # Prepare data
        close_prices = df[['Close']].values
        last_60 = close_prices[-60:]
        scaled = scaler.transform(last_60)
        X_pred = np.reshape(scaled, (1, 60, 1))

        # Predict
        predicted_scaled = model.predict(X_pred)
        predicted_price = scaler.inverse_transform(predicted_scaled)
        st.metric("📌 Predicted Next Closing Price", f"{predicted_price[0][0]:.2f} USD")

        # Plot
        st.subheader("📉 Price Trend")
        fig, ax = plt.subplots()
        ax.plot(df['Date'].tail(60), close_prices[-60:], label='Actual')
        ax.scatter(df['Date'].iloc[-1], predicted_price, color='red', label='Predicted')
        ax.legend()
        st.pyplot(fig)
    else:
        st.error("Model or scaler not found. Please train the model first.")
