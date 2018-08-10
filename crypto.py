import requests

link = 'https://api.cryptowat.ch/markets/kraken/btceur/price'
fullText = requests.get(link)
decryptedText = fullText.text
decryptedText = decryptedText.replace('{','').replace('"','').replace('result','').replace(':','').replace('price','').replace('allowance','').replace(',','').replace('cost','').replace('}','').replace('remaining','')
decryptedText = decryptedText[:-15]
decryptedText = decryptedText + ' Euro'


