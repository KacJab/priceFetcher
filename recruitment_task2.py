import requests
import pandas as pd
import numpy as np


url = "https://www.okx.com/api/v5/market/candles"

symbol = "BTC-USDT"

params = {
    "instId" : symbol,
    'bar': "15m",
    'limit' : '100'
}

response = requests.get(url, params=params)


if response.status_code == 200:
    data = response.json()
    close_prices = []

    # close_prices.append(data["data"][10][4])

    for close_price in data["data"]:
        # print(close_price[4])
        close_pr = close_price[4]
        close_prices.append(close_pr)

    print("Close Prices:")
    for i, close_price in enumerate(close_prices):
        print(f"Bar {i + 1}: {close_price}")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")


def ma(Data, period, onwhat, where):
    for i in range(len(Data)):
        try:
            Data[i, where] = (Data[i - period:i + 1, onwhat].mean())

        except IndexError:
            pass
    return Data




