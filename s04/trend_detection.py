import pandas_ta as ta
import pandas as pd
import ccxt

exchange = ccxt.coinex()
bars = exchange.fetch_ohlcv("BTC/USDT", timeframe="1h", limit=300)
df = pd.DataFrame(bars, columns=['ts', 'open', 'high', 'low', 'close', 'volume'])

df["EMA_50"] = ta.ema(df['close'], length=50)
df['EMA_200'] = ta.ema(df['close'], length=200)


def detect_trend(row):
    if row['close'] > row['EMA_200'] and row["EMA_50"] > row['EMA_200']:
        return "Strong Uptrend"
    elif row['close'] < row['EMA_200'] and row['EMA_50'] < row['EMA_200']:
        return "Strong Downtrend"
    else:
        return "Neutral"


df['Trend'] = df.apply(detect_trend, axis=1)

last_status = df.iloc[-1]
print(f"آخرین قیمت {last_status['close']}")
print(f"آخرین روند بازار :{last_status['Trend']}")