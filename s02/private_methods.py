import ccxt

exchange = ccxt.coinex({
    'apiKey': 'F72BE5EC6BE843619EC67E859FF9BCD5',
    'secret': 'BB8A1F66DFE22ECBFB8EFF9C077AED6D3D44960219445CD1',
})

# balance = exchange.fetch_balance()
# print(f"Balance {balance['free']['USDT']}")

symbol = "BTC/USDT"
amount = 0.001
price = 6000

order = exchange.create_limit_buy_order(symbol, amount, price)
print(f"سفارش خرید شما ثبت شد. کد سفارش {order['id']}")

order_id = order['id']
exchange.cancel_order(order_id, symbol)
print("سفارش با موفقیت لغو شد.")