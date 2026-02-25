import ccxt
import pandas as pd
import pytz

exchange = ccxt.coinex()

symbol = "BTC/USDT"
timeframe = "1m"

bars = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=100)

df = pd.DataFrame(bars, columns=["timestamp", "open", "high", "low", "close", "volume"])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit="ms", utc=True)

tehran_tz = pytz.timezone("Asia/Tehran")

df['timestamp'] = df['timestamp'].dt.tz_convert(tehran_tz)
df['timestamp'] = df['timestamp'].dt.strftime("%Y-%m-%d %H:%M:%S")

df["pct_change"] = df['close'].pct_change() * 100

df['volatility'] = df['close'].rolling(window=20).std()

df['cumulative_return'] = (1 + df['pct_change'] / 100).cumprod() - 1
df['cumulative_return'] *= 100

df["body_size"] = abs(df['close'] - df['open'])

df['is_bullish'] = df['close'] > df['open']

df.set_index("timestamp", inplace=True)
df.to_csv("data.csv")