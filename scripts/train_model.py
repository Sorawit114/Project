import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import os

input_path = 'data/processed/processed_data.csv'
df = pd.read_csv(input_path)
X = df[['Date', 'Open', 'High', 'Low', 'Volume']]
y = df['Close']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

mse = mean_squared_error(y_test, model.predict(X_test))
print(f"Mean Squared Error: {mse}")

os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/stock_predictor.pkl')
print("Model saved to models/stock_predictor.pkl")