import ccxt

exchange = ccxt.coinex({
    'apiKey': 'F72BE5EC6BE843619EC67E859FF9BCD5',
    'secret': 'BB8A1F66DFE22ECBFB8EFF9C077AED6D3D44960219445CD1',
    'options': {
        'createMarketBuyOrderRequiresPrice': False,
        'defaultType': 'spot',
    }
})


try:
    balance = exchange.fetch_balance()

    usdt_balance = balance['total'].get("USDT", 0)

    print("Connected successfully")
    print(f"Your usdt balance: {usdt_balance}")

    print("Your assets")

    for asset, amount in balance['total'].items():
        if amount > 0:
            print(f"{asset}: {amount}")

except Exception as e:
    print(f"Error: {e}")