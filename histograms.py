import csv
from collections import Counter
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import plotly.figure_factory as ff
import plotly.io as pio
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import csv
from collections import Counter
import operator
import datetime as dt
import numpy as np


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

# rcParams['font.family'] = 'sans-serif'
# rcParams['font.sans-serif'] = ['Computer Modern']
# plt.rcParams.update({'font.size': 12})

font = {'family' : 'Computer Modern',
        'weight' : 'bold',
        'size'   : 6}
plt.rc('font', **font)

def timeline(csv_file):
    temp = []
    for line in csv_file:
        if len(line) == 7 and line[0] != 'date':
            if line[2] != '':
                temp.append(line[0])
            else:
                if line[4] != '(fee)':
                    temp.append(line[0])
    input_list=[]
    for i in temp:
        temp=i.split()
        input_list.append(temp[0])
    start=input_list[0]
    end=input_list[len(input_list)-1]
    row = [start,end]
    return row

def draw_timeline():
    greenRoad=timeline(GreenRoad)
    alphaBay=timeline(AlphaBay)
    silkRoad2=timeline(SilkRoad2)
    silkRoad=timeline(SilkRoad)
    babylon=timeline(Babylon)
    nucleus=timeline(Nucleus)
    middleEarth=timeline(MiddleEarth)
    sheep=timeline(Sheep)
    evolution=timeline(Evolution)
    cannabisRoad=timeline(CannabisRoad)
    blackBank=timeline(BlackBank)
    abraxas=timeline(Abraxas)
    blueSky=timeline(BlueSky)
    pandora=timeline(Pandora)
    df = [dict(Task="GreenRoad", Start=greenRoad[0], Finish=greenRoad[1],Resource='GreenRoad'),
      dict(Task="AlphaBay", Start=alphaBay[0], Finish=alphaBay[1],Resource='AlphaBay'),
      dict(Task="SilkRoad2Marketplace", Start=silkRoad2[0], Finish=silkRoad2[1],Resource='SilkRoad2Marketplace'),
      dict(Task="SilkRoadMarketplace", Start=silkRoad[0], Finish=silkRoad[1],Resource='SilkRoadMarketplace'),
      dict(Task="BabylonMarket", Start=babylon[0], Finish=babylon[1],Resource='BabylonMarket'),
      dict(Task="NucleusMarket", Start=nucleus[0], Finish=nucleus[1],Resource='NucleusMarket'),
      dict(Task="MiddleEarthMarketplace", Start=middleEarth[0], Finish=middleEarth[1],Resource='MiddleEarthMarketplace'),
      dict(Task="SheepMarketplace", Start=sheep[0], Finish=sheep[1],Resource='SheepMarketplace'),
      dict(Task="EvolutionMarket", Start=evolution[0], Finish=evolution[1],Resource='EvolutionMarket'),
      dict(Task="CannabisRoadMarket", Start=cannabisRoad[0], Finish=cannabisRoad[1],Resource='CannabisRoadMarket'),
      dict(Task="BlackBankMarket", Start=blackBank[0], Finish=blackBank[1],Resource='BlackBankMarket'),
      dict(Task="AbraxasMarket", Start=abraxas[0], Finish=abraxas[1],Resource='AbraxasMarket'),
      dict(Task="BlueSkyMarketplace", Start=blueSky[0], Finish=blueSky[1],Resource='BlueSkyMarketplace'),
      dict(Task="PandoraOpenMarket", Start=pandora[0], Finish=pandora[1],Resource='PandoraOpenMarket'),
      ]
    df = sorted(df, key=lambda i: i['Start'])
    colors = ['#4286f4', '#41f450', '#ebf224','#ff00c3','#f90431','#ef9607','#bf00f9','#00ffdd','#183818','#e1a0f7','#706666','#84840d','#b30059','#227722']
    fig = ff.create_gantt(df,colors=colors,title='Timeline of activity of each Darknets',index_col='Resource', reverse_colors=True, show_colorbar=True)
    py.plot(fig, filename='gantt-simple-gantt-chart', world_readable=True)

def frequency_tx_wallet(csv_file,name):
    print('begin '+name)
    temp_in=[]
    temp_out=[]
    for line in csv_file:
        if len(line) == 7 and line[0] != 'date':
            if line[2] != '':
                temp_in.append(line[1])
            else:
                if line[4] != '(fee)':
                    temp_out.append(line[4])
    dict_in = Counter(temp_in)
    dict_out = Counter(temp_out)

    x1 = list(dict_in.values())
    x2 = list(dict_out.values())
    print('values added')
    # f = open('/Users/macbook/Desktop/histogram_results.txt', 'a')
    # f.write("FREQUENCY OF INGOING TRANSACTIONS BY WALLETS IN THE" + name + "\n")
    # f.write(str(Counter(x1)) + '\n')
    # f.write("FREQUENCY OF OUTGOING TRANSACTIONS BY WALLETS IN THE " + name + "\n")
    # f.write(str(Counter(x2)) + '\n')
    # f.close()

    axes = plt.gca()
    axes.set_ylim([min(Counter(x1).values()),max(Counter(x1).values())])

    plt.hist(x1,bins=[i for i in range(0,max(set((x1))))])
    plt.title('Frequency of ingoing transactions by wallets in the ' + name,)
    plt.xlabel('Number of transactions')
    plt.ylabel('Frequency')
    plt.savefig('/Users/macbook/Desktop/FYP/charts/histograms/freq_tx_wallet/ingoing/freq_tx_wallet-'+name+'.png')
    plt.clf()
    print("saved "+name)

    axes = plt.gca()
    axes.set_ylim([min(x2),max(x2)])

    plt.hist(x2,bins=[i for i in range(0,max(set(x2)))])
    plt.title('Frequency of outgoing transactions by wallets in the ' + name,)
    plt.xlabel('Number of transactions')
    plt.ylabel('Frequency')
    plt.savefig('/Users/macbook/Desktop/FYP/charts/histograms/freq_tx_wallet/outgoing/freq_tx_wallet-'+name+'.png')
    plt.clf()
    print("saved "+name)

def frequency_tx_day(csv_file, name):
    temp_in = []
    temp_out = []
    for line in csv_file:
        if len(line) == 7 and line[0] != 'date':
            if line[2] != '':
                temp_in.append(line[0])
            else:
                if line[4] != '(fee)':
                    temp_out.append(line[0])
    input_list=[]
    for i in temp_in:
        temp=i.split()
        input_list.append(temp[0])
    output_list = []
    for i in temp_out:
        temp = i.split()
        output_list.append(temp[0])
    dict_in = Counter(input_list)
    dict_out = Counter(output_list)

    x1 = list(dict_in.values())
    x2 = list(dict_out.values())

    axes = plt.gca()
    axes.set_ylim([min(Counter(x1).values()),max(Counter(x1).values())])

    plt.hist(x1,bins=[i for i in range(0,len(set((x1))))])
    plt.title('Frequency of ingoing transactions by day in the ' + name,)
    plt.xlabel('Number of transactions')
    plt.ylabel('Frequency')
    plt.savefig('/Users/macbook/Desktop/FYP/charts/histograms/freq_tx_day/ingoing/freq_tx_day-'+name+'.png')
    plt.clf()
    print("saved "+name)

    axes = plt.gca()
    axes.set_ylim([min(Counter(x2).values()),max(Counter(x2).values())])

    plt.hist(x2,bins=[i for i in range(0,len(set(x2)))])
    plt.title('Frequency of outgoing transactions by day in the ' + name,)
    plt.xlabel('Number of transactions')
    plt.ylabel('Frequency')
    plt.savefig('/Users/macbook/Desktop/FYP/charts/histograms/freq_tx_day/outgoing/freq_tx_day-'+name+'.png')
    plt.clf()
    print("saved "+name)
# for i in param:
#     frequency_tx_day(i[0],i[1])

def amount_by_tx(csv_file,name):
    temp_in = []
    temp_out = []
    for line in csv_file:
        if len(line) == 7 and line[0] != 'date':
            if line[2] != '':
                temp_in.append(float(line[2]))
            else:
                if line[4] != '(fee)':
                    temp_out.append(float(line[3]))
    temp_in.sort()
    temp_out.sort()

    bin_list={}
    def splitz(list_param):
        min_val=0
        sub_list = []
        for i in list_param:
            if min_val<=i<min_val+0.01:
                sub_list.append(i)
            else:
                bin_list[min_val,min_val+0.01]=len(sub_list)
                min_val+=0.01
                sub_list = []
        return (sorted(bin_list.items(), key=operator.itemgetter(1)))

    x1 = temp_in
    x2 = temp_out

    # axes = plt.gca()
    # axes.set_ylim([min(Counter(x1).values()),max(Counter(x1).values())])

    # [i for i in np.arange(0, max(set(x1)), 0.1*2)]

    plt.hist(x1, bins =[0,0.01,0.02,0.03,0.1,0.5,1,2,3,4,5,10,15,20,30,40,50]+[i for i in np.arange(60, max(set(x1)), 10)])
    plt.title('Frequency of volume of received amount by ingoing transactions in the '+name)
    plt.xlabel('Amount in BTC')
    plt.ylabel('Frequency')
    plt.savefig('/Users/macbook/Desktop/FYP/charts/histograms/volumes-by-tx/ingoing/volume_tx_day-'+name+'.png')
    plt.clf()
    print("saved "+name)

    # axes = plt.gca()
    # axes.set_ylim([min(Counter(x2).values()),max(Counter(x2).values())])

    plt.hist(x2,bins =[0,0.01,0.02,0.03,0.1,0.5,1,2,3,4,5,10,15,20,30,40,50]+[i for i in np.arange(60, max(set(x1)), 10)])
    plt.title('Frequency of volume of sent amount by outgoing transactions in the '+name)
    plt.xlabel('Amount in BTC')
    plt.ylabel('Frequency')
    plt.savefig('/Users/macbook/Desktop/FYP/charts/histograms/volumes-by-tx/outgoing/volume_tx_day-'+name+'.png')
    plt.clf()
    print("saved "+name)

def amount_by_day(csv_file,name):
    temp_in = {}
    temp_out = {}
    for line in csv_file:
        if len(line) == 7 and line[0] != 'date':
            date=line[0].split()[0]
            if line[2] != '':
                if date not in temp_in.keys():
                    temp_in[date]=[]
                temp_in[date].append(float(line[2]))
            else:
                if line[4] != '(fee)' and line[3]!='':
                    if date not in temp_out.keys():
                        temp_out[date]=[]
                    temp_out[date].append(float(line[3]))
    for i in temp_in.keys():
        sum_list = sum(temp_in[i])
        temp_in[i]=sum_list
    for i in temp_out.keys():
        sum_list = sum(temp_out[i])
        temp_out[i]=sum_list

    temp_in=list(temp_in.values())
    temp_out=list(temp_out.values())

    temp_in.sort()
    temp_out.sort()

    bin_list={}
    def splitz(list_param):
        min_val=0
        sub_list = []
        for i in list_param:
            if min_val<=i<min_val+1:
                sub_list.append(i)
            else:
                bin_list[min_val,min_val+1]=len(sub_list)
                min_val+=1
                sub_list = []
        return (sorted(bin_list.items(), key=operator.itemgetter(1)))

    # f = open('/Users/macbook/Desktop/amount_in_day_results.txt', 'a')
    # f.write("AMOUNT OF INGOING BTC IN THE " + name + "\n")
    # f.write(str(splitz(temp_in))+ '\n')
    # f.write("AMOUNT OF OUTGOING BTC IN THE " + name + "\n")
    # f.write(str(splitz(temp_out)) + '\n')
    # f.close()

    x1 = temp_in
    # axes = plt.gca()
    # axes.set_ylim([0,])
    # plt.hist(x1,bins =[0,0.01,0.02,0.03,0.1,0.5,1,2,3,4,5,10,15,20,30,40,50]+[i for i in np.arange(60, max(set(x1)), 10)])
    # plt.title('Frequency of volume of ingoing transactions by day in the '+name)
    # plt.xlabel('Amount in BTC')
    # plt.ylabel('Frequency')
    # plt.savefig('/Users/macbook/Desktop/FYP/charts/histograms/volumes-by-day/ingoing/volume_tx_day-'+name+'.png')
    # plt.clf()
    # print("saved "+name)

    x2 = temp_out
    # axes = plt.gca()
    # axes.set_ylim([min(Counter(x2).values()),max(Counter(x2).values())])
    # plt.hist(x2,bins =[0,0.01,0.02,0.03,0.1,0.5,1,2,3,4,5,10,15,20,30,40,50]+[i for i in np.arange(60, max(set(x1)), 10)])
    # plt.title('Frequency of volume of outgoing transactions by day in the '+name)
    # plt.xlabel('Amount in BTC')
    # plt.ylabel('Frequency')
    # plt.savefig('/Users/macbook/Desktop/FYP/charts/histograms/volumes-by-day/outgoing/volume_tx_day-'+name+'.png')
    # plt.clf()
    # print("saved "+name)

    data = [go.Histogram(x=x1)]

    layout = go.Layout(
        title='Frequency of volume of ingoin transactions by day in the '+name,
        xaxis=dict(
            title='Amount in BTC'
        ),
        yaxis=dict(
            title='Frequency'
        ),
    )
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='styled histogram')
    pio.write_image(fig, '/Users/macbook/Desktop/FYP/charts/histograms/volumes-by-day/ingoing/volume_tx_day-'+name+'.png')

    data = [go.Histogram(x=x2)]

    layout = go.Layout(
        title='Frequency of volume of outgoing transactions by day in the '+name,
        xaxis=dict(
            title='Amount in BTC'
        ),
        yaxis=dict(
            title='Frequency'
        ),
    )
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='styled histogram')
    pio.write_image(fig, '/Users/macbook/Desktop/FYP/charts/histograms/volumes-by-day/outgoing/volume_tx_day-'+name+'.png')


param = [(GreenRoad,'GreenRoadMarket'),(AlphaBay,'AlphaBayMarket'),(SilkRoad2,'SilkRoad2Marketplace'),(SilkRoad,'SilkRoadMarketplace'),
         (Babylon,'BabylonMarket'),(Nucleus,'NucleusMarket'),(MiddleEarth,'MiddleEarthMarketplace'),(Sheep,'SheepMarketplace'),
         (Evolution,'EvolutionMarket'),(CannabisRoad,'CannabisRoadMarket'),(BlackBank,'BlackBankMarket'),(Abraxas,'AbraxasMarket'),
         (BlueSky,'BlueSkyMarketplace'),(Pandora,'PandoraOpenMarket')]

# for i in param:
    # frequency_tx_wallet(i[0],i[1])
    # frequency_tx_day(i[0],i[1])
    # frequency_tx_wallet(i[0],i[1])
    # amount_by_day(i[0],i[1])
draw_timeline()