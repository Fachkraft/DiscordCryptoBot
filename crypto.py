import requests

link = 'https://api.cryptowat.ch/markets/kraken/btceur/price'
fullText = requests.get(link)
decryptedText = fullText.text

