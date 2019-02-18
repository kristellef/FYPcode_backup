import csv
from collections import Counter
from operator import itemgetter
from itertools import groupby
import pandas

reader = csv.reader(open('/Users/macbook/Desktop/FYP/files/darknet_userID.csv','rt'),delimiter=',')

list=[]
dictionary={}
for row in reader:
    entry = (row[4],row[3])
    list.append(entry)

PandoraOpenMarket =[]
BabylonMarket=[]
BlackBankMarket=[]
EvolutionMarket=[]
SilkRoad2Market=[]
MiddleEarthMarketplace=[]
NucleusMarket=[]
BlueSkyMarketplace=[]
GreenRoadMarket=[]
AbraxasMarket=[]
SilkRoadMarketplace=[]
SheepMarketplace=[]
AlphaBayMarket=[]
CannabisRoadMarket=[]

for i in list:
    if i[1] == 'PandoraOpenMarket':
        PandoraOpenMarket.append(int(i[0]))
    if i[1] == 'BabylonMarket':
        BabylonMarket.append(int(i[0]))
    if i[1] == 'BlackBankMarket':
        BlackBankMarket.append(int(i[0]))
    if i[1] == 'EvolutionMarket':
        EvolutionMarket.append(int(i[0]))
    if i[1] == 'SilkRoad2Market':
        SilkRoad2Market.append(int(i[0]))
    if i[1] == 'MiddleEarthMarketplace':
        MiddleEarthMarketplace.append(int(i[0]))
    if i[1] == 'NucleusMarket':
        NucleusMarket.append(int(i[0]))
    if i[1] == 'BlueSkyMarketplace':
        BlueSkyMarketplace.append(int(i[0]))
    if i[1] == 'GreenRoadMarket':
        GreenRoadMarket.append(int(i[0]))
    if i[1] == 'AbraxasMarket':
        AbraxasMarket.append(int(i[0]))
    if i[1] == ' SilkRoadMarketplace':
        SilkRoadMarketplace.append(int(i[0]))
    if i[1] == 'SheepMarketplace':
        SheepMarketplace.append(int(i[0]))
    if i[1] == 'AlphaBayMarket':
        AlphaBayMarket.append(int(i[0]))
    if i[1] == 'CannabisRoadMarket':
        CannabisRoadMarket.append(int(i[0]))

print(Counter(PandoraOpenMarket))
print(Counter(BabylonMarket))
print(Counter(BlackBankMarket))
print(Counter(EvolutionMarket))
print(Counter(SilkRoad2Market))
print(Counter(MiddleEarthMarketplace))
print(Counter(NucleusMarket))
print(Counter(BlueSkyMarketplace))
print(Counter(GreenRoadMarket))
print(Counter(AbraxasMarket))
print(Counter(SilkRoadMarketplace))
print(Counter(SheepMarketplace))
print(Counter(AlphaBayMarket))
print(Counter(CannabisRoadMarket))
