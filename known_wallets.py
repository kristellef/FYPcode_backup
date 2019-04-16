import csv
import networkx as nx
import matplotlib.pyplot as plt
from graph_tool.all import *
from collections import Counter
import re

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
            if line[2] != '' and len(line[2])>16 and 'E' not in line[2]:
                array_in.append(line[1])
            else:
                if line[4] != '(fee)' and len(line[4])>16 and 'E' not in line[3]:
                    array_out.append(line[4])

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
f = open('/Users/macbook/Desktop/list_known_wallets.txt','w')
for i in vertex:
    f.write(i +"\n")
f.close()
