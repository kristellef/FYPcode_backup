import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import requests
import lxml.html as lh
import re
import math
import itertools

def getTotalNumber(url):
    array = []
    r = requests.get(url)
    doc = lh.fromstring(r.content)
    small_elements = doc.xpath('//small')
    for line in small_elements:
        array.append(line.text_content())
    total_number = int(re.sub('[^\d\.]', '', array[0]))
    return total_number

def getPage(url):
    array=[]
    result=[]
    r = requests.get(url)
    doc = lh.fromstring(r.content)
    small_elements = doc.xpath('//small')
    for line in small_elements:
        array.append(line.text_content())
    total_number = int(re.sub('[^\d\.]', '', array[0]))
    page_number = math.ceil(total_number / 100)
    for i in range(1,page_number+1):
        new_url = url + '?page=' + str(i)
        result.append(query(new_url))
    for item in result:
        item.pop(0)
    return list(itertools.chain.from_iterable(result))

def query(url):
    r = requests.get(url)
    doc = lh.fromstring(r.content)
    tr_elements = doc.xpath('//tr')
    amount=[]
    for line in tr_elements:
        value = re.sub('[^\d\.]', '', line[1].text_content())
        amount.append(value)
    return amount

# print(getPage('https://www.walletexplorer.com/wallet/BabylonMarket/addresses'))

plotly.tools.set_credentials_file(username='kristelle', api_key='CvmqbRb7CXD5VgwhRzQV')
py.sign_in("kristelle", "CvmqbRb7CXD5VgwhRzQV")

x1 = getPage('https://www.walletexplorer.com/wallet/SilkRoadMarketplace/addresses')
total_number = getTotalNumber('https://www.walletexplorer.com/wallet/SilkRoadMarketplace/addresses')
percentage = ((x1.count('0.')) / (float(total_number)))*100.0

layout = go.Layout(
    title='Balance of addresses in the SilkRoadMarketplace',
    xaxis=dict(
        title='Balance amount'
    ),
    yaxis=dict(
            title='Number of addresses'
        ),
    annotations=[
            dict(
                x=2,
                y=3000,
                xref='x',
                yref='y',
                text="percentage of balance equal to 0=" + str(percentage),
                showarrow=False,
            )
        ]
)

data = [go.Histogram(x=x1)]

fig = go.Figure(data=data,layout=layout)
plot_url = py.plot(fig, filename='histogram-balance-SilkRoadMarketplace')


x1 = getPage('https://www.walletexplorer.com/wallet/SilkRoad2Market/addresses')
total_number = getTotalNumber('https://www.walletexplorer.com/wallet/SilkRoad2Market/addresses')
percentage = ((x1.count('0.')) / (float(total_number)))*100.0

layout = go.Layout(
    title='Balance of addresses in the SilkRoad2Market',
    xaxis=dict(
        title='Balance amount'
    ),
    yaxis=dict(
            title='Number of addresses'
        ),
    annotations=[
            dict(
                x=2,
                y=3000,
                xref='x',
                yref='y',
                text="percentage of balance equal to 0=" + str(percentage),
                showarrow=False,
            )
        ]
)

data = [go.Histogram(x=x1)]


fig = go.Figure(data=data,layout=layout)
plot_url = py.plot(fig, filename='histogram-balance-SilkRoad2Market')