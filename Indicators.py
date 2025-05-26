import pandas as pd
import matplotlib.pyplot as plt

def add_trend_label(df):
    df = df.copy()
    df['Next_Close'] = df['Close'].shift(-1)
    df['Trend'] = (df['Next_Close'] > df['Close']).astype(int)
    df = df.dropna(subset=['Trend'])
    return df

def add_technical_indicators(df):
    df = df.copy()
    df['MA5'] = df['Close'].rolling(window=5).mean()
    df['MA10'] = df['Close'].rolling(window=10).mean()
    df['MA20'] = df['Close'].rolling(window=20).mean()
    # MACD
    df['EMA12'] = df['Close'].ewm(span=12, adjust=False).mean()
    df['EMA26'] = df['Close'].ewm(span=26, adjust=False).mean()
    df['MACD'] = df['EMA12'] - df['EMA26']
    df['MACD_signal'] = df['MACD'].ewm(span=9, adjust=False).mean()
    df['MACD_hist'] = df['MACD'] - df['MACD_signal']
    df['Daily_Return'] = df['Close'].pct_change()
    df['Volume_Change_Pct'] = df['Volume'].pct_change()
    df['Momentum'] = df['Close'] - df['Close'].shift(10)
    df['20_STD'] = df['Close'].rolling(window=20).std()
    df['Upper_BB'] = df['MA20'] + (df['20_STD'] * 2)
    df['Lower_BB'] = df['MA20'] - (df['20_STD'] * 2)
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    RS = gain / loss
    df['RSI'] = 100 - (100 / (1 + RS))
    min_rsi = df['RSI'].rolling(window=14).min()
    max_rsi = df['RSI'].rolling(window=14).max()
    df['Stoch_RSI'] = (df['RSI'] - min_rsi) / (max_rsi - min_rsi)
    return df.dropna()

def plot_stock(df, ticker):
    plt.figure(figsize=(14,7))
    plt.plot(df.index, df['Close'], label='Close Price', color='blue')
    plt.plot(df.index, df['MA5'], label='MA5', color='orange')
    plt.plot(df.index, df['MA10'], label='MA10', color='green')
    plt.title(f'{ticker} Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()
