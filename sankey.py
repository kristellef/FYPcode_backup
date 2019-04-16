import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import csv
import random
from collections import Counter

# plotly.tools.set_credentials_file(username='kristelle', api_key='CvmqbRb7CXD5VgwhRzQV')
# py.sign_in("kristelle", "CvmqbRb7CXD5VgwhRzQV")

plotly.tools.set_credentials_file(username='kristelle97', api_key='Tg0PO9kW82dNkT3mkLqj')
py.sign_in("kristelle97", "Tg0PO9kW82dNkT3mkLqj")

CannabisRoad = csv.reader(open('/Users/macbook/Desktop/FYP/files/CannabisRoadMarket-transactions/CannabisRoadMarket_transactions.csv','rt'),delimiter=',')
GreenRoad = csv.reader(open('/Users/macbook/Desktop/FYP/files/GreenRoadMarket-transactions/GreenRoadMarket-transactions.csv','rt'),delimiter=',')
Babylon = csv.reader(open('/Users/macbook/Desktop/FYP/files/BabylonMarket-transactions/Babylon_transactions.csv','rt'),delimiter=',')
BlackBank = csv.reader(open('/Users/macbook/Desktop/FYP/files/BlackBankMarket-transactions/BlackBankMarket-transactions.csv','rt'),delimiter=',')
AlphaBay = csv.reader(open('/Users/macbook/Desktop/FYP/files/AlphaBayMarket-transactions/AlphaBay_transactions.csv','rt'),delimiter=',')
Abraxas = csv.reader(open('/Users/macbook/Desktop/FYP/files/AbraxasMarket-transactions/AbraxasMarket-transactions.csv','rt'),delimiter=',')
BlueSky = csv.reader(open('/Users/macbook/Desktop/FYP/files/BlueSkyMarketplace-transactions/BlueSkyMarketplace-transactions.csv','rt'),delimiter=',')
Evolution = csv.reader(open('/Users/macbook/Desktop/FYP/files/EvolutionMarket-transactions/Evolution-transactions.csv','rt'),delimiter=',')
MiddleEarth = csv.reader(open('/Users/macbook/Desktop/FYP/files/MiddleEarthMarketplace-transactions/MiddleEarthMarketplace-transactions.csv','rt'),delimiter=',')
Nucleus = csv.reader(open('/Users/macbook/Desktop/FYP/files/NucleusMarket-transactions/NucleusMarket-transactions.csv','rt'),delimiter=',')
Pandora = csv.reader(open('/Users/macbook/Desktop/FYP/files/PandoraOpenMarket-transactions/PandoraOpenMarket-transactions.csv','rt'),delimiter=',')
Sheep = csv.reader(open('/Users/macbook/Desktop/FYP/files/SheepMarketplace-transactions/SheepMarketplace-transactions.csv','rt'),delimiter=',')
SilkRoad2 = csv.reader(open('/Users/macbook/Desktop/FYP/files/SilkRoad2Market-transactions/SilkRoad2Market-transactions.csv','rt'),delimiter=',')
SilkRoad = csv.reader(open('/Users/macbook/Desktop/FYP/files/SilkRoadMarketplace-transactions/SilkRoadMarketplace-transactions.csv','rt'),delimiter=',')

def draw_sanksey(reader,name):
    mydict_in=[]
    mydict_out=[]

    for line in reader:
        if len(line)==7 and line[0]!='date':
            mydict_in.append(line[1])
            mydict_out.append(line[4])

    dict_in = Counter(mydict_in)
    dict_out = Counter(mydict_out)

    # del dictionary_out['(fee)']
    # del dictionary_out['']
    # del dictionary['']

    dictionary_out={}
    dictionary={}

    for k, v in dict_out.items():
        if len(k) > 16:
            dictionary_out[k]=v

    for k, v in dict_in.items():
        if len(k) < 16:
            dictionary[k] = v

    # dictionary = {key:val for key, val in dictionary.items() if val !=1}
    # dictionary_out = {key:val for key, val in dictionary_out.items() if val !=1}

    keys = list(dictionary.keys())
    values = list(dictionary.values())

    keys_out = list(dictionary_out.keys())
    values_out = list(dictionary_out.values())

    keys.append(name)
    keys_out.append(name)

    def random_color(n):
        color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                 for i in range(n)]
        return color

    data1 = dict(
        type='sankey',
        node = dict(
          pad = 15,
          thickness = 20,
          line = dict(
            color = "black",
            width = 0.5
          ),
          label = keys,
          color = random_color(len(keys))
        ),
        link = dict(
          source = list(range(0, len(keys)-1)),
          target = [len(keys)-1]*(len(keys)-1),
          value = values
      ))

    layout1 =  dict(
        title = 'Flow of ingoing transactions from known wallets to ' +name,
        font = dict(
          size = 10
        )
    )

    fig1 = dict(data=[data1], layout=layout1)
    py.plot(fig1, validate=False,filename=name+'-ingoing')

    data2 = dict(
        type='sankey',
        node=dict(
            pad=15,
            thickness=20,
            line=dict(
                color="black",
                width=0.5
            ),
            label=keys_out,
            color=random_color(len(keys_out))
        ),
        link=dict(
            source=[len(keys_out) - 1] * (len(keys_out) - 1),
            target=list(range(0, len(keys_out) - 1)),
            value=values_out
        ))

    layout2 = dict(
        title='Flow of outgoing transactions from '+name+' to known wallets',
        font=dict(
            size=10
        )
    )

    fig2 = dict(data=[data2], layout=layout2)
    py.plot(fig2, validate=False, filename=name + '-outgoing')

param = [(GreenRoad,'GreenRoadMarket'),(AlphaBay,'AlphaBayMarket'),(SilkRoad2,'SilkRoad2Marketplace'),(SilkRoad,'SilkRoadMarketplace'),
         (Babylon,'BabylonMarket'),(Nucleus,'NucleusMarket'),(MiddleEarth,'MiddleEarthMarketplace'),(Sheep,'SheepMarketplace'),
         (Evolution,'EvolutionMarket'),(CannabisRoad,'CannabisRoadMarket'),(BlackBank,'BlackBankMarket'),(Abraxas,'AbraxasMarket'),
         (BlueSky,'BlueSkyMarketplace'),(Pandora,'PandoraOpenMarket')]

for i in param:
    draw_sanksey(i[0],i[1])
