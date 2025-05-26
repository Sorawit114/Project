import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error, r2_score

model = joblib.load('models/stock_predictor.pkl')
df = pd.read_csv('data/processed/processed_data.csv')
X = df[['Date', 'Open', 'High', 'Low', 'Volume']]
y = df['Close']

predictions = model.predict(X)
mae = mean_absolute_error(y, predictions)
r2 = r2_score(y, predictions)
print(f"Mean Absolute Error: {mae:.2f}")
print(f"R2 Score: {r2:.2f}")