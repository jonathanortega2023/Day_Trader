import pandas as pd
import yfinance as yf

qtum_df = yf.download('QTUM')
print(qtum_df.head())

ticker = yf.Ticker('QTUM')
tsla_df = ticker.history(period = 'max')
tsla_df['Close'].plot(title = 'QTUM\'s stock price')