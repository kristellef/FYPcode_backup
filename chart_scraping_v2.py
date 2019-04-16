import lxml.html as lh
import re
import math
import csv
import time
import requests
from bs4 import BeautifulSoup
import urllib.request
import os

def scrap_wallet(url, folder, ip):
    # url = 'https://www.walletexplorer.com/wallet/SheepMarketplace'

    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page,'html.parser')

    num = soup.find("small").text
    pageNumber = int(re.sub('[^\d\.]', '', num))
    numberPages = math.ceil(pageNumber / 100)

    addresses=[]
    numbers=[]

    files = list(os.listdir(folder[:(len(folder)-4)]))
    for i in files:
        if re.sub("[^0-9]", "", i) != '':
            numbers.append(int(re.sub("[^0-9]", "", i)))

    print(len(numbers))

    for i in range(1,numberPages+1):
        # url2 = "https://www.walletexplorer.com/wallet/SheepMarketplace?" + "page=" + str(i) +"&format=csv"
        if i not in numbers:
            url2 = url + "?" + "page=" + str(i) + "&format=csv"
            print(url2)
            addresses.append(url2)
        else:
            print("i already downloaded")

    i = len(addresses)

    for address in addresses:
        proxy = urllib.request.ProxyHandler(ip)
        # construct a new opener using your proxy settings
        opener = urllib.request.build_opener(proxy)
        # install the openen on the module-level
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(address,folder + str(i) + '.csv')
        i = i-1
        if i%50==0:
            print(i)

scrap_wallet('https://www.walletexplorer.com/wallet/SilkRoadMarketplace','/Users/macbook/Desktop/FYP/files/SilkRoadMarketplace-transactions/file', {'http': 'http://179.191.245.58'})
scrap_wallet('https://www.walletexplorer.com/wallet/EvolutionMarket','/Users/macbook/Desktop/FYP/files/EvolutionMarket-transactions/file', {'http': 'http://187.111.113.253'})