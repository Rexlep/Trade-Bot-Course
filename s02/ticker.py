import ccxt

exchange = ccxt.coinex()

markets = exchange.load_markets()

print(f"All markets  {len(markets)}")

symbols = exchange.symbols
print("5 first ticker")

print(symbols[:5])

symbol = "BTC/USDT"
ticker = exchange.fetch_ticker(symbol)

last_price = ticker['last']
high_price = ticker['high']
low_price = ticker['low']
bid = ticker['bid']
ask = ticker['ask']

print(f"State {symbol}")
print(f"Live price {last_price}$")
print(f"Highest price {high_price}")
print(f"Lowest price {low_price}")
print(f"Best price for sale {bid}")
print(f"Best price for buy {ask}")