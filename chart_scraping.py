import requests
import lxml.html as lh
import re
import math
import csv
import time
from random import randint

from bs4 import BeautifulSoup
import requests


addresses = []
reader = csv.reader(open('/Users/macbook/Desktop/FYP/files/mapping-darknet.csv', 'rt'), delimiter=',')
writer = csv.writer(open('/Users/macbook/Desktop/FYP/files/chart_data.csv', 'a+'))
header = ['received', 'sent','balance']
writer.writerow(header)
received = ''
sent = ''
balance = ''
array =[]

for row in reader:
    if (row[3] == 'AbraxasMarket'):
        addresses.append(row[0])
while(len(addresses) > 0):
    for i in range(0,100):
        url = 'https://live.blockcypher.com/btc/address/' + addresses[i] + '/'
        r = requests.get(url)
        # html = r.read().decode("utf-8")
        if 'Checking your browser before accessing blockcypher.com' in r:
            print('ok')
            break
        doc = lh.fromstring(r.content)
        # find the rows of the table and store
        li_elements = doc.xpath('//li')
        for line in li_elements:
            array.append(line.text_content())
        for s in array:
            if 'Received' in s:
                received = re.sub('[^\d\.]', '', s)
            if 'Sent' in s:
                sent = re.sub('[^\d\.]', '', s)
            if 'Balance' in s:
                balance = re.sub('[^\d\.]', '', s)
        row = [received, sent, balance]
        print(row)
        print(url)
        writer.writerow(row)
        # sleep(5)
    del (addresses[:100])
    print(len(addresses))







