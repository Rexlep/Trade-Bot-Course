import pandas_ta as ta
import pandas as pd
import ccxt

exchange = ccxt.coinex()
bars = exchange.fetch_ohlcv("BTC/USDT", timeframe="1h", limit=100)
df = pd.DataFrame(bars, columns=['ts', 'open', 'high', 'low', 'close', 'volume'])

macd_df = ta.macd(df['close'], fast=12, slow=26, signal=9)

df = pd.concat([df, macd_df], axis=1)

print(df.columns)

print(df[['close', "MACD_12_26_9",  "MACDs_12_26_9", "MACDh_12_26_9"]].tail())