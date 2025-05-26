import matplotlib.pyplot as plt

def calculate_return(df):
    df['Return'] = df['Close'].pct_change()
    return df

def plot_price(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df['Close'], label='Close Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Stock Close Price Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()
