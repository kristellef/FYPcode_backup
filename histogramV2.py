import csv
from collections import Counter
# import plotly.plotly as py
# import plotly.graph_objs as go
# import plotly
# import plotly.figure_factory as ff
# import plotly.io as pio
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import csv
from collections import Counter
import operator
import datetime as dt
import numpy as np
from pylab import rcParams

#
# plotly.tools.set_credentials_file(username='kiko97', api_key='Cit4WdYDyj9td7OuHEvU')
# py.sign_in("kiko97", "Cit4WdYDyj9td7OuHEvU")

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

rcParams['figure.figsize'] = 17, 12

def timeline(csv_file):
    temp = []
    for line in csv_file:
        if len(line) == 7 and line[0] != 'date' and '#Wallet' not in line[0]:
            if line[2] != '':
                temp.append(line[0])
            else:
                if line[4] != '(fee)'  and '#Wallet' not in line[0]:
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
    df = [dict(Task="GreenRoad", Start='2015-07-22', Finish='2015-10-30',Resource='GreenRoadMarket'),
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

def ratio_ingoing_outgoing():
    x1=[]
    y1=[]
    x2=[]
    y2=[]
    def count_in_out(csv_file,name):
        count_in=0
        count_out=0
        for line in csv_file:
            if len(line) == 7 and line[0] != 'date':
                if line[2] != '':
                    count_in+=1
                else:
                    if line[4] != '(fee)' and line[3]!='':
                        count_out+=1
        return [count_in,count_out,name]

    param = [(GreenRoad,'GreenRoadMarket'),(AlphaBay,'AlphaBayMarket'),(SilkRoad2,'SilkRoad2Marketplace'),(SilkRoad,'SilkRoadMarketplace'),
             (Babylon,'BabylonMarket'),(Nucleus,'NucleusMarket'),(MiddleEarth,'MiddleEarthMarketplace'),(Sheep,'SheepMarketplace'),
             (Evolution,'EvolutionMarket'),(CannabisRoad,'CannabisRoadMarket'),(BlackBank,'BlackBankMarket'),(Abraxas,'AbraxasMarket'),
             (BlueSky,'BlueSkyMarketplace'),(Pandora,'PandoraOpenMarket')]

    for i in param:
        result = count_in_out(i[0],i[1])
        x1.append(result[0])
        x2.append(result[1])
        y1.append(result[2])
        y2.append(result[2])

    trace1 = go.Bar(
        y=y1,
        x=x1,
        name='Ingoing',
        orientation = 'h',
        marker = dict(
            color = 'rgba(246, 78, 139, 0.6)',
            line = dict(
                color = 'rgba(246, 78, 139, 1.0)',
                width = 3)
        )
    )
    trace2 = go.Bar(
        y=y2,
        x=x2,
        name='Outgoing',
        orientation = 'h',
        marker = dict(
            color = 'rgba(58, 71, 80, 0.6)',
            line = dict(
                color = 'rgba(58, 71, 80, 1.0)',
                width = 3)
        )
    )

    data = [trace1, trace2]
    layout = go.Layout(
        barmode='stack'
    )

    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='ingoing-outgoing-darknet')

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

    # x1 = list(dict_in.values())
    # x2 = list(dict_out.values())

    x1 = Counter(list(dict_in.values()))
    x2 = Counter(list(dict_out.values()))

    print('values added')
    def group(lst, n):
        for i in range(0, len(lst), n):
            val = lst[i:i+n]
            if len(val) == n:
              yield tuple(val)

    def splitz(bins,list_param):
        dict_bin={}
        dict_count={}
        for bin in bins:
            dict_bin[bin]=[]
            dict_count[bin]=0
        for i in list_param:
            for bin in bins:
                if bin[0]<=round(i,2)<=bin[1]:
                    dict_bin[bin].append(round(i,2))
                    dict_count[bin]+=1
        return (sorted(dict_count.items(), key=operator.itemgetter(1), reverse=True))

    dict_count1=dict(splitz(list(group([round(i,2) for i in np.arange(0, (round(max(set(x1)), 2))+4, 2)], 2)),sorted(x1)))
    print('dict created')

    filtered_dict_in = {k:v for k,v in dict_count1.items() if v!=0}

    print('dict filtered')

    print(filtered_dict_in)
    x = [str(i) for i in filtered_dict_in.keys()]
    g = tuple(filtered_dict_in.values())
    x = tuple(x)
    x_pos = np.arange(len(x))
    plt.bar(x_pos, g, color='#7ed6df',align='edge', width=0.5)
    plt.xlabel('Amount in BTC')
    plt.ylabel('Frequency')
    plt.title('Frequency of ingoing transactions by bitcoin address in the '+name)
    plt.xticks(x_pos, x,rotation=90,fontsize=5)
    plt.savefig('/Users/macbook/Desktop/FYP/charts/histograms/fq_by_txV2/ingoing/fq_tx_wallet-'+name+'.png')
    plt.clf()
    print('saved')


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

    def group(lst, n):
        for i in range(0, len(lst), n):
            val = lst[i:i+n]
            if len(val) == n:
              yield tuple(val)

    def splitz(bins,list_param):
        dict_bin={}
        dict_count={}
        for bin in bins:
            dict_bin[bin]=[]
            dict_count[bin]=0
        for i in list_param:
            for bin in bins:
                if bin[0]<=round(i,2)<=bin[1]:
                    dict_bin[bin].append(round(i,2))
                    dict_count[bin]+=1
        return (sorted(dict_count.items(), key=operator.itemgetter(1), reverse=True))

    dict_count1=dict(splitz(list(group([round(i,2) for i in np.arange(0, (round(max(set(x1)), 2))+4, 2)], 2)),sorted(x2)))
    print('dict created')

    filtered_dict_in = {k:v for k,v in dict_count1.items() if v!=0}

    print('dict filtered')
    sum_values = sum(filtered_dict_in.values())
    print(name)
    for v in filtered_dict_in:
        percentage = round(float(filtered_dict_in[v])/float(sum_values)*100,2)
        print(str(percentage))



    print(filtered_dict_in)
    x = [str(i) for i in filtered_dict_in.keys()]
    g = tuple(filtered_dict_in.values())
    x = tuple(x)
    x_pos = np.arange(len(x))
    plt.bar(x_pos, g, color='#7ed6df',align='edge', width=0.5)
    plt.xlabel('Amount in BTC')
    plt.ylabel('Frequency')
    plt.title('Frequency of outgoing transactions by day in the '+name)
    plt.xticks(x_pos, x,rotation=90,fontsize=5)
    plt.savefig('/Users/macbook/Desktop/FYP/charts/histograms/fq_by_txV2/outgoing/fq_tx_day-'+name+'.png')
    plt.clf()
    print('saved')

def amount_by_tx(csv_file,name):
    temp_in = []
    temp_out = []
    for line in csv_file:
        if len(line) == 7 and line[0] != 'date':
            if line[2] != '':
                temp_in.append(float(line[2]))
            else:
                if line[4] != '(fee)' and line[3]!='':
                    temp_out.append(float(line[3]))
    temp_in.sort()
    temp_out.sort()

    bin_list={}

    def group(lst, n):
        for i in range(0, len(lst), n):
            val = lst[i:i+n]
            if len(val) == n:
              yield tuple(val)

    def splitz(bins,list_param):
        dict_bin={}
        dict_count={}
        for bin in bins:
            dict_bin[bin]=[]
            dict_count[bin]=0
        for i in list_param:
            for bin in bins:
                if bin[0]<=round(i,2)<=bin[1]:
                    dict_bin[bin].append(round(i,2))
                    dict_count[bin]+=1
        return (sorted(dict_count.items(), key=operator.itemgetter(1), reverse=True))
        #return dict_count

    x1 = temp_in
    x2 = temp_out

    dict_count1=dict(splitz(list(group([round(i,2) for i in np.arange(0, (round(max(set(x1)), 2))+0.6, 0.3)], 2)),sorted(x1)))
    print('dict created')

    filtered_dict_in = {k:v for k,v in dict_count1.items() if v!=0}

    print('dict filtered')

    print(filtered_dict_in)
    x = [str(i) for i in filtered_dict_in.keys()]
    g = tuple(filtered_dict_in.values())
    x = tuple(x)
    x_pos = np.arange(len(x))
    plt.bar(x_pos, g, color='#7ed6df',align='edge', width=2)
    plt.xlabel('Amount in BTC')
    plt.ylabel('Frequency')
    plt.title('Frequency of volume of received amount by ingoing transactions in the '+name)
    plt.xticks(x_pos, x,rotation=90,fontsize=1)
    plt.show()
    # plt.savefig('/Users/macbook/Desktop/FYP/charts/histograms/volume_by_txV2/ingoing/volume_tx_day-'+name+'.png')
    plt.clf()
    print('saved')


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

    x1 = temp_in
    x2 = temp_out

    def group(lst, n):
        for i in range(0, len(lst), n):
            val = lst[i:i+n]
            if len(val) == n:
              yield tuple(val)

    def splitz(bins,list_param):
        dict_bin={}
        dict_count={}
        for bin in bins:
            dict_bin[bin]=[]
            dict_count[bin]=0
        for i in list_param:
            for bin in bins:
                if bin[0]<=round(i,2)<=bin[1]:
                    dict_bin[bin].append(round(i,2))
                    dict_count[bin]+=1
        return (sorted(dict_count.items(), key=operator.itemgetter(1), reverse=True))
        #return dict_count

    # dict_count1=dict(splitz(list(group([round(i,2) for i in np.arange(0, (round(max(set(x2)), 2))+0.5, 0.25)], 2)),sorted(x2)))
    # dict_count1=dict(splitz(list(group([round(i,2) for i in np.arange(0, (round(max(set(x2)), 2))+0.2, 0.1)], 2)),sorted(x2)))
    dict_count1=dict(splitz(list(group([round(i,2) for i in np.arange(0, 3500, 50)], 2)),sorted(x1)))
    # print('dict created')

    # filtered_dict_in = {k:v for k,v in dict_count1.items() if v!=0}
    filtered_dict_in=dict_count1
    # print('dict filtered')

    sum_values = sum(filtered_dict_in.values())
    print(name)
    total=0
    for v in filtered_dict_in:
        percentage = round(float(filtered_dict_in[v])/float(sum_values)*100,2)
        print(str(v)+str(percentage))
        total += percentage
    # print(total)

    # sum_values = sum(filtered_dict_in.values())
    # print(name)
    # for v in filtered_dict_in:
    #     percentage = round(float(filtered_dict_in[v])/float(sum_values)*100,2)
    #     print(str(percentage))

    # print(filtered_dict_in)
    # x = [str(i) for i in filtered_dict_in.keys()]
    # g = tuple(filtered_dict_in.values())
    # x = tuple(x)
    # x_pos = np.arange(len(x))
    # plt.bar(x_pos, g, color='#7ed6df',align='edge', width=1)
    # plt.xlabel('Amount in BTC')
    # plt.ylabel('Frequency')
    # plt.title('Frequency of volume of received amount by outgoing transactions in the '+name)
    # plt.xticks(x_pos, x,rotation=90,fontsize=5)
    # plt.savefig('/Users/macbook/Desktop/FYP/charts/histograms/volume_by_dayV2/outgoing/volume_tx_day-'+name+'.png')
    # plt.clf()
    # print('saved')


param = [(GreenRoad,'GreenRoadMarket'),(AlphaBay,'AlphaBayMarket'),(SilkRoad2,'SilkRoad2Marketplace'),(SilkRoad,'SilkRoadMarketplace'),
         (Babylon,'BabylonMarket'),(Nucleus,'NucleusMarket'),(MiddleEarth,'MiddleEarthMarketplace'),(Sheep,'SheepMarketplace'),
         (Evolution,'EvolutionMarket'),(CannabisRoad,'CannabisRoadMarket'),(BlackBank,'BlackBankMarket'),(Abraxas,'AbraxasMarket'),
         (BlueSky,'BlueSkyMarketplace'),(Pandora,'PandoraOpenMarket')]

def group(lst, n):
    for i in range(0, len(lst), n):
        val = lst[i:i+n]
        if len(val) == n:
          yield tuple(val)

# bins=list(group([round(i,2) for i in np.arange(0, 5800, 50)], 2))
# for i in bins:
#     print(i)

# for i in param:
#      # frequency_tx_wallet(i[0],i[1])
#      # frequency_tx_day(i[0],i[1])
#      # amount_by_tx(i[0],i[1])
#      amount_by_day(i[0],i[1])

print(timeline(AlphaBay))
