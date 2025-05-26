import streamlit as st
from datetime import datetime
import joblib
from recommend import recommend_action

st.title("📈 Stock Price Predictor")

model = joblib.load('models/stock_predictor.pkl')

date = st.date_input("Date", datetime(2023, 1, 1))
open_price = st.number_input("Open Price", value=150.0)
high_price = st.number_input("High Price", value=155.0)
low_price = st.number_input("Low Price", value=148.0)
volume = st.number_input("Volume", value=1000000)

if st.button("Predict"):
    ordinal = date.toordinal()
    features = [[ordinal, open_price, high_price, low_price, volume]]
    predicted_price = model.predict(features)[0]
    action = recommend_action(open_price, predicted_price)
    st.success(f"Predicted Close Price: ${predicted_price:.2f}")
    st.info(f"Recommendation: {action}")