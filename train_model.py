import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def load_data(filename):
    df = pd.read_csv(filename)
    df['Date'] = pd.to_datetime(df['Date'], utc=True)
    df['Date'] = df['Date'].map(pd.Timestamp.toordinal)
    df = df.dropna()
    return df

def train_model(df):
    X = df[['Date', 'Open', 'High', 'Low', 'Volume']]
    y = df['Close']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")

    return model

def save_model(model, filename):
    joblib.dump(model, filename)
    print(f"Model saved to {filename}")

if __name__ == "__main__":
    df = load_data('stock_data.csv')
    model = train_model(df)
    save_model(model, 'stock_predictor_model.pkl')
