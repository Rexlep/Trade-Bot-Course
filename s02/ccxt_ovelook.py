import ccxt

# print("Numbers of exchanges", len(ccxt.exchanges), ':', ccxt.exchanges)

exchange = ccxt.coinex()

try:
    status = exchange.fetch_status()
    print(f"Coinex exchange status {status['status']}")
except Exception as e:
    print("Could not connect")

market = exchange.load_markets()
print(f"Numbers of crypto in exchange {len(market)}")