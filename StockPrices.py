import requests


# Apple stock prices (every 5 minutes)
response_AAPL = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=AAPL&interval=5min&apikey=53HU7S3992V5RPQZ", verify = False)
data_AAPL = response_AAPL.json()

# Google stock prices (every 5 minutes)
response_GOOG = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=GOOG&interval=5min&apikey=53HU7S3992V5RPQZ", verify = False)
data_GOOG = response_GOOG.json()

# This is a dict:
print("KEYS: ", data_AAPL.keys())

# Metadata
print("META DATA:", data_AAPL['Meta Data'])

# Actual Prices
# This line will need to change if you use a different function from alphavantage
prices = data_AAPL['Time Series (5min)']
# let's take the first 5 items
prices_list = list(prices.items())[:5]

for p in prices_list:
    print(p)

dict_prices = {'2024-12-06 19:55:00', {'1. open': '242.3977', '2. high': '242.4100', '3. low': '242.3025', '4. close': '242.3550', '5. volume': '1447'},
    '2024-12-06 19:50:00', {'1. open': '242.3300', '2. high': '242.4100', '3. low': '242.3000', '4. close': '242.4000', '5. volume': '1554'},
    '2024-12-06 19:45:00', {'1. open': '242.3200', '2. high': '242.4100', '3. low': '242.3025', '4. close': '242.3400', '5. volume': '875'},
    '2024-12-06 19:40:00', {'1. open': '242.3200', '2. high': '242.4100', '3. low': '242.3200', '4. close': '242.3650', '5. volume': '1082'},
    '2024-12-06 19:35:00', {'1. open': '242.3201', '2. high': '242.4100', '3. low': '242.3200', '4. close': '242.4100', '5. volume': '1815'}}