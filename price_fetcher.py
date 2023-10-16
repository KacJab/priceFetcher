import ccxt
import time


def fetch_prices(symbol, exchange_names):

    exchanges = {}

    for exchange_name in exchange_names:
        try:
            exchange = getattr(ccxt, exchange_name.lower())()
            exchanges[exchange_name] = exchange
        except Exception as e:
            print(f'Error initializing {exchange_name}: {str(e)}')

    while True:
        try:
            for exchange_name, exchange in exchanges.items():
                ticker = exchange.fetch_ticker(symbol)
                last_price = ticker.get('last')

                if last_price:
                    print(f'{exchange_name} {symbol} Price: {last_price}')
                else:
                    print(f'Error fetching {exchange_name} price data.')

            time.sleep(0.2)

        except Exception as e:
            print(f'Error fetching prices: {str(e)}')

if __name__ == "__main__":
    symbol = 'ADA/BTC'

    exchange_names = ['Poloniex', 'OKX', 'binance']    #you can add another exchanges here

    fetch_prices(symbol, exchange_names)
