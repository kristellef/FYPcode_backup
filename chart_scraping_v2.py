import lxml.html as lh
import re
import math
import csv
import time
import requests
from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.walletexplorer.com/wallet/BlackBankMarket'

page = urllib.request.urlopen(url)
soup = BeautifulSoup(page,'html.parser')

num = soup.find("small").text
pageNumber = int(re.sub('[^\d\.]', '', num))
numberPages = math.ceil(pageNumber / 100)

addresses=[]

for i in range(1,numberPages+1):
    url2 = "https://www.walletexplorer.com/wallet/BlackBankMarket?" + "page=" + str(i) +"&format=csv"
    print(url2)
    addresses.append(url2)

i = len(addresses)
for address in addresses:
    urllib.request.urlretrieve(address, '/Users/macbook/Desktop/FYP/files/BlackBankMarket-transactions/file' + str(i) + '.csv')
    i = i-1
    if i%50==0:
        print(i)