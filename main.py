import ccxt
import pandas as pd

exchange = ccxt.coinex()

symbol = "BTC/USDT"
timeframe = "1h"

bars = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=100)

df = pd.DataFrame(bars, columns=["timestamp", "open", "high", "low", "close", "volume"])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit="ms")

df.set_index("timestamp", inplace=True)
print(df.head())