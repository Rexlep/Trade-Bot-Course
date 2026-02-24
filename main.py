import ccxt
import pandas as pd
import pytz

exchange = ccxt.coinex()

symbol = "BTC/USDT"
timeframe = "1h"

bars = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=100)

df = pd.DataFrame(bars, columns=["timestamp", "open", "high", "low", "close", "volume"])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit="ms", utc=True)

tehran_tz = pytz.timezone("Asia/Tehran")

df['timestamp'] = df['timestamp'].dt.tz_convert(tehran_tz)
df['timestamp'] = df['timestamp'].dt.strftime("%Y-%m-%d %H:%M:%S")

df.dropna(inplace=True)

df.set_index("timestamp", inplace=True)
print(df.head())