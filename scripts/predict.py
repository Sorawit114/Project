import pandas as pd
import joblib
from datetime import datetime
from recommend import recommend_action

model = joblib.load('models/stock_predictor.pkl')

# Example input
date = '2023-01-01'
open_price = 150.0
high_price = 155.0
low_price = 148.0
volume = 1000000

ordinal = datetime.strptime(date, '%Y-%m-%d').toordinal()
features = [[ordinal, open_price, high_price, low_price, volume]]
predicted_price = model.predict(features)[0]
print(f"Predicted closing price for {date}: {predicted_price:.2f}")

action = recommend_action(open_price, predicted_price)
print("Recommended Action:", action)