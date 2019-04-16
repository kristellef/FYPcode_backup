import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import csv
import random
from collections import Counter
import collections

# plotly.tools.set_credentials_file(username='kristelle', api_key='CvmqbRb7CXD5VgwhRzQV')
# py.sign_in("kristelle", "CvmqbRb7CXD5VgwhRzQV")

# plotly.tools.set_credentials_file(username='kristelle97', api_key='Tg0PO9kW82dNkT3mkLqj')
# py.sign_in("kristelle97", "Tg0PO9kW82dNkT3mkLqj")

plotly.tools.set_credentials_file(username='kristelle', api_key='B6M6G5J07Lc1HiBHcpVt')
py.sign_in("kristelle", "B6M6G5J07Lc1HiBHcpVt")


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
    dict_in={}
    dict_out={}
    for line in reader:
        if len(line) == 7 and line[0] != 'date':
            if line[2] != '':
                if line[1] not in dict_in:
                    dict_in[line[1]]=0.0
                dict_in[line[1]]+=float(line[2])
            else:
                if line[4] != '(fee)' and line[3]!='':
                    if line[4] not in dict_out:
                        dict_out[line[4]]=0.0
                    dict_out[line[4]]+=float(line[3])

    filtered_dict_in = {k:v for k,v in dict_in.items() if len(k)>16}
    filtered_dict_out = {k:v for k,v in dict_out.items() if len(k)>16}

    sorted_in = collections.OrderedDict(sorted(filtered_dict_in.items(), key=lambda kv: kv[1],reverse=True))
    sorted_out = collections.OrderedDict(sorted(filtered_dict_out.items(), key=lambda kv: kv[1], reverse=True))


    def random_color(n):
        color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
                 for i in range(n)]
        return color

    labels_in=[]
    # keys_in=list(filtered_dict_in.keys())
    # values_in=list(filtered_dict_in.values())
    keys_in = list(sorted_in.keys())[:5]
    values_in=list(sorted_in.values())[:5]
    # for i in range(0,len(filtered_dict_in)):
    #     labels_in.append(keys_in[i] + ' ' +str(values_in[i]) + 'BTC')
    for i in range(0,len(list(sorted_in.keys())[:5])):
        labels_in.append(keys_in[i] + ' ' +str(values_in[i]) + 'BTC')

    # labels_out = []
    # keys_out = list(filtered_dict_out.keys())
    # values_out = list(filtered_dict_out.values())
    # for i in range(0, len(filtered_dict_out)):
    #     labels_out.append(keys_out[i] + ' ' + str(values_out[i]) + 'BTC')
    labels_out = []
    keys_out = list(sorted_out.keys())[:5]
    values_out = list(sorted_out.values())[:5]
    for i in range(0,len(list(sorted_out.keys())[:5])):
        labels_out.append(keys_out[i] + ' ' + str(values_out[i]) + 'BTC')

    # labels_in=list(filtered_dict_in.keys())
    labels_in.append(name)

    # labels_out=list(filtered_dict_out.keys())
    labels_out.append(name)

    print(values_in)
    print(labels_in)

    # values_in = list(filtered_dict_in.values())
    # values_out = list(filtered_dict_out.values())

    # data = dict(
    #     type='sankey',
    #     node = dict(
    #       pad = 15,
    #       thickness = 20,
    #       line = dict(
    #         color = "black",
    #         width = 0.5
    #       ),
    #       label = labels_in,
    #       color = random_color(len(filtered_dict_in)-1)
    #     ),
    #     link = dict(
    #       source = [i for i in range(0,len(labels_in)-1)],
    #       target = [len(labels_in)-1]*(len(labels_in)-1),
    #       value = values_in
    #   ))
    #
    # layout =  dict(
    #     title = 'Flow of ingoing transactions from known wallets to ' +name,
    #     font = dict(
    #       size = 10
    #     )
    # )

    data = dict(
            type='sankey',
            node = dict(
              pad = 15,
              thickness = 20,
              line = dict(
                color = "black",
                width = 0.5
              ),
              label = labels_out,
              color = random_color(len(filtered_dict_out)-1)
            ),
            link = dict(
              source = [len(labels_out)-1]*(len(labels_out)-1),
              target = [i for i in range(0,len(labels_out)-1)],
              value = values_out
          )
    )

    layout =  dict(
        title = 'Flow of outgoing transactions from' + name+' to known wallets',
        font = dict(
            size = 10
        )
     )

    fig = dict(data=[data], layout=layout)
    py.plot(fig, validate=False,filename=name+'-outgoing')



param = [(GreenRoad,'GreenRoadMarket'),(AlphaBay,'AlphaBayMarket'),(SilkRoad2,'SilkRoad2Marketplace'),(SilkRoad,'SilkRoadMarketplace'),
         (Babylon,'BabylonMarket'),(Nucleus,'NucleusMarket'),(MiddleEarth,'MiddleEarthMarketplace'),(Sheep,'SheepMarketplace'),
         (Evolution,'EvolutionMarket'),(CannabisRoad,'CannabisRoadMarket'),(BlackBank,'BlackBankMarket'),(Abraxas,'AbraxasMarket'),
         (BlueSky,'BlueSkyMarketplace'),(Pandora,'PandoraOpenMarket')]

for i in param:
    draw_sanksey(i[0],i[1])
