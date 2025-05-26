import pandas as pd
import joblib
from datetime import datetime

def load_model(filename):
    model = joblib.load(filename)
    return model

def predict_price(model, date, open_price, high_price, low_price, volume):
    date_ordinal = datetime.strptime(date, '%Y-%m-%d').toordinal()
    features = [[date_ordinal, open_price, high_price, low_price, volume]]
    predicted_price = model.predict(features)
    return predicted_price[0]

if __name__ == "__main__":
    model = load_model('stock_predictor_model.pkl')

    date = '2023-01-01'
    open_price = 150.0
    high_price = 155.0
    low_price = 148.0
    volume = 1000000

    predicted_price = predict_price(model, date, open_price, high_price, low_price, volume)
    print(f"Predicted closing price for {date}: {predicted_price}")
