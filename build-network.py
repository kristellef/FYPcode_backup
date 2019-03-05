import csv
import networkx as nx
import matplotlib.pyplot as plt
from graph_tool.all import *
from collections import Counter

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

cannabis_in=[]
cannabis_out=[]

greenRoad_in=[]
greenRoad_out=[]

babylon_in=[]
babylon_out=[]

blackbank_in=[]
blackbank_out=[]

alphabay_in=[]
alphabay_out=[]

abraxas_in=[]
abraxas_out =[]

bluesky_in=[]
bluesky_out =[]

evolution_in=[]
evolution_out=[]

middle_in=[]
middle_out=[]

nucleus_in=[]
nucleus_out=[]

pandora_in=[]
pandora_out=[]

sheep_in=[]
sheep_out=[]

silk2_in=[]
silk2_out=[]

silk_in=[]
silk_out=[]

def add_tx_to_array (csv_file, array_in,array_out):
    for line in csv_file:
        if len(line) == 7 and line[0] != 'date':
            if line[2] != '':
                array_in.append(line[1])
            else:
                if line[4] != '(fee)':
                    array_out.append(line[4])

# for line in CannabisRoad:
#     if len(line) == 7 and line[0] != 'date':
#         if line[2] != '':
#             cannabis_in.append(line[1])
#         else:
#             if line[4] != '(fee)':
#                 cannabis_out.append(line[4])

array = [(AlphaBay,alphabay_in,alphabay_out),(BlackBank,blackbank_in, blackbank_out), (CannabisRoad,cannabis_out, cannabis_in), (GreenRoad,greenRoad_in,greenRoad_out), (Babylon,babylon_in,babylon_out),
(Abraxas,abraxas_in,abraxas_out),(Nucleus,nucleus_in,nucleus_out),(Sheep,sheep_in,sheep_out),(Evolution,evolution_in,evolution_out),(MiddleEarth,middle_in,middle_out),(Pandora,pandora_in,pandora_out),
(BlueSky,bluesky_in,bluesky_out),(SilkRoad2,silk2_in,silk2_out),(SilkRoad,silk_in,silk_out)]

for param in array:
    add_tx_to_array(param[0],param[1],param[2])

vertex_temp = alphabay_in + alphabay_out + blackbank_in + blackbank_out + cannabis_out + cannabis_in + greenRoad_in + greenRoad_out + babylon_in + babylon_out + nucleus_in + nucleus_out + pandora_in + pandora_out + bluesky_in + bluesky_out + sheep_out + sheep_in + evolution_in + evolution_out + silk_in + silk_out + silk2_in + silk2_out + middle_in + middle_out + abraxas_in + abraxas_out

dictionary_count=dict(Counter(vertex_temp))
# remove wallets from dict to avoid having duplicate vertex
if 'CannabisRoadMarket (001e9eea95a6f803)' in vertex_temp:
    del dictionary_count['CannabisRoadMarket (001e9eea95a6f803)']
if 'GreenRoadMarket (00adc4a2b0fbd07c)' in vertex_temp:
    del dictionary_count['GreenRoadMarket (00adc4a2b0fbd07c)']
if 'BlackBankMarket (0001210e68c46db4)' in vertex_temp:
    del dictionary_count['BlackBankMarket (0001210e68c46db4)']
if 'AlphaBayMarket (000078c74c35206a)' in vertex_temp:
    del dictionary_count['AlphaBayMarket (000078c74c35206a)']
if 'BabylonMarket (0025ef6357663859)' in vertex_temp:
    del dictionary_count['BabylonMarket (0025ef6357663859)']
if 'AbraxasMarket (000052c2391e8192)' in vertex_temp:
    del dictionary_count['AbraxasMarket (000052c2391e8192)']
if 'BlueSkyMarketplace (00015294e4ef907e)' in vertex_temp:
    del dictionary_count['BlueSkyMarketplace (00015294e4ef907e)']
if 'MiddleEarthMarketplace (000041317dfea6fd)' in vertex_temp:
    del dictionary_count['MiddleEarthMarketplace (000041317dfea6fd)']
if 'PandoraOpenMarket (0000d9a5c977c03b)' in vertex_temp:
    del dictionary_count['PandoraOpenMarket (0000d9a5c977c03b)']
if 'SheepMarketplace (0000a3a375c51032)' in vertex_temp:
    del dictionary_count['SheepMarketplace (0000a3a375c51032)']
if 'SilkRoad2Market (00000bfdb5d7ed34)' in vertex_temp:
    del dictionary_count['SilkRoad2Market (00000bfdb5d7ed34)']
if 'NucleusMarket (0001a5d354cf4f44)' in vertex_temp:
    del dictionary_count['NucleusMarket (0001a5d354cf4f44)']
if 'EvolutionMarket (000000388b7abc5c)' in vertex_temp:
    del dictionary_count['EvolutionMarket (000000388b7abc5c)']
if 'SilkRoadMarketplace (000006f003f6a22c)' in vertex_temp:
    del dictionary_count['SilkRoadMarketplace (000006f003f6a22c)']

vertex=list(dictionary_count.keys())
label=list(dictionary_count.keys())
print(len(vertex))

g = Graph()
v=[g.add_vertex() for i in range(0,len(vertex))]

v_cannabis = g.add_vertex()
v_greenroad = g.add_vertex()
v_babylon = g.add_vertex()
v_blackmarket=g.add_vertex()
v_alphabay=g.add_vertex()
v_abraxas = g.add_vertex()
v_nucleus = g.add_vertex()
v_evolution = g.add_vertex()
v_bluesky = g.add_vertex()
v_silkroad = g.add_vertex()
v_silkroad2 = g.add_vertex()
v_pandora = g.add_vertex()
v_middle = g.add_vertex()
v_sheep = g.add_vertex()

print('number of vertex: ' + str(len(v)))

v_prop = g.new_vertex_property("string")
for i in range(0,len(v)):
    v_prop[v[i]]= label[i]

v_prop[v_cannabis]= 'CannabisRoadMarket (001e9eea95a6f803)'
v_prop[v_greenroad]= 'GreenRoadMarket (00adc4a2b0fbd07c)'
v_prop[v_babylon]= 'BabylonMarket (0025ef6357663859)'
v_prop[v_blackmarket]= 'BlackBankMarket (0001210e68c46db4)'
v_prop[v_alphabay]='AlphaBayMarket (000078c74c35206a)'
v_prop[v_abraxas]='AbraxasMarket (000052c2391e8192)'
v_prop[v_nucleus]='NucleusMarket (0001a5d354cf4f44)'
v_prop[v_evolution]='EvolutionMarket (000000388b7abc5c)'
v_prop[v_bluesky]='BlueSkyMarketplace (00015294e4ef907e)'
v_prop[v_silkroad]='SilkRoadMarketplace (000006f003f6a22c)'
v_prop[v_silkroad2]='SilkRoad2Market (00000bfdb5d7ed34)'
v_prop[v_pandora]='PandoraOpenMarket (0000d9a5c977c03b)'
v_prop[v_middle]='MiddleEarthMarketplace (000041317dfea6fd)'
v_prop[v_sheep]='SheepMarketplace (0000a3a375c51032)'

print('vertex added')

edges=[]

# TODO: check if edges from one wallet to another are included / wallet vertex added twice?

for edge in v:
    # inflow
    if v_prop[edge] in greenRoad_in:
        g.add_edge(edge,v_greenroad)
    if v_prop[edge] in babylon_in:
        g.add_edge(edge,v_babylon)
    if v_prop[edge] in cannabis_in:
        g.add_edge(edge,v_cannabis)
    if v_prop[edge] in blackbank_in:
        g.add_edge(edge,v_blackmarket)
    if v_prop[edge] in alphabay_in:
        g.add_edge(edge,v_alphabay)
    if v_prop[edge] in abraxas_in:
        g.add_edge(edge,v_abraxas)
    if v_prop[edge] in nucleus_in:
        g.add_edge(edge,v_nucleus)
    if v_prop[edge] in evolution_in:
        g.add_edge(edge,v_evolution)
    if v_prop[edge] in pandora_in:
        g.add_edge(edge,v_pandora)
    if v_prop[edge] in sheep_in:
        g.add_edge(edge,v_sheep)
    if v_prop[edge] in silk_in:
        g.add_edge(edge,v_silkroad)
    if v_prop[edge] in silk2_in:
        g.add_edge(edge,v_silkroad2)
    if v_prop[edge] in bluesky_in:
        g.add_edge(edge,v_bluesky)
    if v_prop[edge] in middle_in:
        g.add_edge(edge,v_middle)
    # outlfow
    if v_prop[edge] in greenRoad_out:
        g.add_edge(v_greenroad,edge)
    if v_prop[edge] in babylon_out:
        g.add_edge(v_babylon,edge)
    if v_prop[edge] in cannabis_out:
        g.add_edge(v_cannabis,edge)
    if v_prop[edge] in blackbank_out:
        g.add_edge(v_blackmarket,edge)
    if v_prop[edge] in alphabay_out:
        g.add_edge(v_alphabay,edge)
    if v_prop[edge] in abraxas_out:
        g.add_edge(v_abraxas,edge)
    if v_prop[edge] in evolution_out:
        g.add_edge(v_evolution,edge)
    if v_prop[edge] in pandora_out:
        g.add_edge(v_pandora,edge)
    if v_prop[edge] in middle_out:
        g.add_edge(v_middle,edge)
    if v_prop[edge] in silk_out:
        g.add_edge(v_silkroad,edge)
    if v_prop[edge] in silk2_out:
        g.add_edge(v_silkroad2,edge)
    if v_prop[edge] in bluesky_out:
        g.add_edge(v_bluesky,edge)
    if v_prop[edge] in sheep_out:
        g.add_edge(v_sheep,edge)
    if v_prop[edge] in nucleus_out:
        g.add_edge(v_nucleus,edge)

# if 'CannabisRoadMarket (001e9eea95a6f803)' in greenRoad_in:
#     g.add_edge(v_cannabis,v_greenroad)
# if 'CannabisRoadMarket (001e9eea95a6f803)' in greenRoad_out:
#     g.add_edge(v_greenroad,v_cannabis)
# if 'BabylonMarket (0025ef6357663859)' in greenRoad_in:
#     g.add_edge(v_babylon,v_greenroad)
# if 'BabylonMarket (0025ef6357663859)' in greenRoad_out:
#     g.add_edge(v_greenroad,v_babylon)
# if 'BlackBankMarket (0001210e68c46db4)' in greenRoad_in:
#     g.add_edge(v_blackmarket,v_greenroad)
# if 'BlackBankMarket (0001210e68c46db4)' in greenRoad_out:
#     g.add_edge(v_greenroad,v_blackmarket)
# if 'AlphaBayMarket (000078c74c35206a)' in greenRoad_in:
#     g.add_edge(v_alphabay,v_greenroad)
# if 'AlphaBayMarket (000078c74c35206a)' in greenRoad_out:
#     g.add_edge(v_greenroad,v_alphabay)

def check_wallet_edges(wallet_in,wallet_out,vertex):
    if 'GreenRoadMarket (00adc4a2b0fbd07c)' in wallet_in:
        g.add_edge(v_greenroad,vertex)
        print(v_prop[v_greenroad],v_prop[vertex])
    if 'GreenRoadMarket (00adc4a2b0fbd07c)' in wallet_out:
        g.add_edge(vertex,v_greenroad)
        print(v_prop[vertex],v_prop[v_greenroad])
    if 'CannabisRoadMarket (001e9eea95a6f803)' in wallet_in:
        g.add_edge(v_cannabis,vertex)
        print(v_prop[v_cannabis],v_prop[vertex])
    if 'CannabisRoadMarket (001e9eea95a6f803)' in wallet_out:
        g.add_edge(vertex,v_cannabis)
        print(v_prop[vertex],v_prop[v_cannabis])
    if 'BabylonMarket (0025ef6357663859)' in wallet_in:
        g.add_edge(v_babylon,vertex)
        print(v_prop[v_babylon],v_prop[vertex])
    if 'BabylonMarket (0025ef6357663859)' in wallet_out:
        g.add_edge(vertex,v_babylon)
        print(v_prop[vertex],v_prop[v_babylon])
    if 'BlackBankMarket (0001210e68c46db4)' in wallet_in:
        g.add_edge(v_blackmarket,vertex)
        print(v_prop[v_blackmarket],v_prop[vertex])
    if 'BlackBankMarket (0001210e68c46db4)' in wallet_out:
        g.add_edge(vertex,v_blackmarket)
        print(v_prop[vertex],v_prop[v_blackmarket])
    if 'AlphaBayMarket (000078c74c35206a)' in wallet_in:
        g.add_edge(v_alphabay,vertex)
        print(v_prop[v_alphabay],v_prop[vertex])
    if 'AlphaBayMarket (000078c74c35206a)' in wallet_out:
        g.add_edge(vertex,v_alphabay)
        print(v_prop[vertex],v_prop[v_alphabay])
    if 'AbraxasMarket (000052c2391e8192)' in wallet_in:
        g.add_edge(v_abraxas,vertex)
        print(v_prop[v_abraxas],v_prop[vertex])
    if 'AbraxasMarket (000052c2391e8192)' in wallet_out:
        g.add_edge(vertex,v_abraxas)
        print(v_prop[vertex],v_prop[v_abraxas])
    if 'BlueSkyMarketplace (00015294e4ef907e)' in wallet_in:
        g.add_edge(v_bluesky,vertex)
        print(v_prop[v_bluesky],v_prop[vertex])
    if 'BlueSkyMarketplace (00015294e4ef907e)' in wallet_out:
        g.add_edge(vertex,v_bluesky)
        print(v_prop[vertex],v_prop[v_bluesky])
    if 'MiddleEarthMarketplace (000041317dfea6fd)' in wallet_in:
        g.add_edge(v_middle,vertex)
        print(v_prop[v_middle],v_prop[vertex])
    if 'MiddleEarthMarketplace (000041317dfea6fd)' in wallet_out:
        g.add_edge(vertex,v_middle)
        print(v_prop[vertex],v_prop[v_middle])
    if 'PandoraOpenMarket (0000d9a5c977c03b)' in wallet_in:
        g.add_edge(v_pandora,vertex)
        print(v_prop[v_pandora],v_prop[vertex])
    if 'PandoraOpenMarket (0000d9a5c977c03b)' in wallet_out:
        g.add_edge(vertex,v_pandora)
        print(v_prop[vertex],v_prop[v_pandora])
    if 'SheepMarketplace (0000a3a375c51032)' in wallet_in:
        g.add_edge(v_sheep,vertex)
        print(v_prop[v_sheep],v_prop[vertex])
    if 'SheepMarketplace (0000a3a375c51032)' in wallet_out:
        g.add_edge(vertex,v_sheep)
        print(v_prop[vertex],v_prop[v_sheep])
    if 'SilkRoad2Market (00000bfdb5d7ed34)' in wallet_in:
        g.add_edge(v_silkroad2,vertex)
        print(v_prop[v_silkroad2],v_prop[vertex])
    if 'SilkRoad2Market (00000bfdb5d7ed34)' in wallet_out:
        g.add_edge(vertex,v_silkroad2)
        print(v_prop[vertex],v_prop[v_silkroad2])
    if 'NucleusMarket (0001a5d354cf4f44)' in wallet_in:
        g.add_edge(v_nucleus,vertex)
        print(v_prop[v_nucleus],v_prop[vertex])
    if 'NucleusMarket (0001a5d354cf4f44)' in wallet_out:
        g.add_edge(vertex,v_nucleus)
        print(v_prop[vertex],v_prop[v_nucleus])
    if 'EvolutionMarket (000000388b7abc5c)' in wallet_in:
        g.add_edge(v_evolution,vertex)
        print(v_prop[v_evolution],v_prop[vertex])
    if 'EvolutionMarket (000000388b7abc5c)' in wallet_out:
        g.add_edge(vertex,v_evolution)
        print(v_prop[vertex],v_prop[v_evolution])
    if 'SilkRoadMarketplace (000006f003f6a22c)' in wallet_in:
        g.add_edge(v_silkroad,vertex)
        print(v_prop[v_silkroad],v_prop[vertex])
    if 'SilkRoadMarketplace (000006f003f6a22c)' in wallet_out:
        g.add_edge(vertex,v_silkroad)
        print(v_prop[vertex],v_prop[v_silkroad])

array = [(greenRoad_in,greenRoad_out,v_greenroad),(cannabis_in,cannabis_out,v_cannabis),(babylon_in,babylon_out,v_babylon),(blackbank_in,blackbank_out,v_blackmarket),(alphabay_in,alphabay_out,v_alphabay),
(abraxas_in,abraxas_out,v_abraxas),(nucleus_in,nucleus_out,v_nucleus),(sheep_in,sheep_out,v_sheep),(evolution_in,evolution_out,v_evolution),(middle_in,middle_out,v_middle),(pandora_in,pandora_out,v_pandora),
(bluesky_in,bluesky_out,v_bluesky),(silk2_in,silk2_out,v_silkroad2),(silk_in,silk_out,v_silkroad)]
for param in array:
    check_wallet_edges(param[0],param[1],param[2])
    print ('ok')

print('edges added')

graph_draw(g, vertex_font_size=10, fit_view=1, output_size=(6000, 6000), output="/Users/macbook/Desktop/FYP/charts/network-14-darknet.png")
# vertex_text=v_prop, to add labels
print('graph drawn')
