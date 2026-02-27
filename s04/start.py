import pandas_ta as ta
import pandas as pd
import ccxt

exchange = ccxt.coinex()
bars = exchange.fetch_ohlcv("BTC/USDT", timeframe="1h", limit=100)
df = pd.DataFrame(bars, columns=['ts', 'open', 'high', 'low', 'close', 'volume'])

df['RSA'] = ta.rsi(df['close'], length=14)

df['SMA_20'] = ta.sma(df['close'], length=20)
df['EMA_50'] = ta.ema(df['close'], length=50)

bbands = ta.bbands(df['close'], length=20, std=2)
df = pd.concat([df, bbands], axis=1)

df = df.dropna()

df.to_csv("data.csv", index=True)
print(df.tail())