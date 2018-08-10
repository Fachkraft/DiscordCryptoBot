import requests

link = 'https://api.cryptowat.ch/markets/kraken/btceur/price'
fullText = requests.get(link)

print fullText.text
