import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

from Indicators import add_technical_indicators, add_trend_label

def train_model(df):
    features = ['MA5', 'MA10', 'MA20', 'RSI', 'MACD', 'MACD_signal', 'MACD_hist', 'Daily_Return', 'Volume_Change_Pct',
                'EMA12', 'EMA26', 'Momentum', 'Upper_BB', 'Lower_BB', 'Stoch_RSI']
    df = df.dropna(subset=features + ['Trend'])

    X = df[features]
    y = df['Trend']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = RandomForestClassifier(n_estimators=200, max_depth=10, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("Classification Report:\n", classification_report(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

    return model

if __name__ == "__main__":
    ticker = 'AAPL'
    df = pd.read_csv(f'data/{ticker}.csv')
    df = add_trend_label(df)
    df = add_technical_indicators(df)
    model = train_model(df)
