from datetime import datetime
import json

""""Class to get a stock price"""
class Stock():
    def __init__(self):
        self.price = 0

    def GetStock(self):
        #url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&interval=5min&apikey=4H4XGZE8HAY85MW6"
        #resp = requests.get(url, verify=False)
        f = open("python_stock_daily.txt", "r")
        resp = (f.read())
        return json.loads(resp)
    
    def GetPrice(self):
        stock = Stock().GetStock()
        today = str(datetime.now().strftime("%Y-%m-%d"))
        try:
            price = stock["Time Series (Daily)"][today]["4. close"]            
            return(price)
        except KeyError:
            print("No data found for date {}".format(today))
            return 0