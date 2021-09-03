import datetime
import requests
import json


timedata = datetime.datetime.now()
time = timedata.strftime("%Y-%m-%d %H:%M:%S")
print(time)


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


DogeAddress = "DQ3ooovQ2jzcVWrDrk1nEEVUB6jr71puCR"

balence = requests.get("https://dogechain.info/api/v1/address/balance/"+DogeAddress)
price = requests.get("https://chain.so/api/v2/get_price/DOGE/USD")

pricedata = price.json()
balencedata = balence.json()


currentPrice = pricedata['data']['prices'][0]['price']
currentBalence = float(balencedata['balance'])

cashAmount = float(currentBalence) * float(currentPrice)

currentBalence = round(currentBalence, 4)
#currentPrice = round(currentPrice, 4)
cashAmount = round(cashAmount, 4)

print("Current Price:", currentPrice)
print("Current Balence:", currentBalence)
print("USD: $",cashAmount)

