import csv
from collections import Counter

darknet = csv.reader(open('/Users/macbook/Desktop/FYP/files/darknet_userID-V2.csv', 'rt'), delimiter=',')

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

for row in darknet:
    if row[3]=='PandoraOpenMarket':
        PandoraOpenMarket.append(row[5])
    if row[3]=='BabylonMarket':
        BabylonMarket.append(row[5])
    if row[3]=='BlackBankMarket':
        BlackBankMarket.append(row[5])
    if row[3]=='EvolutionMarket':
        EvolutionMarket.append(row[5])
    if row[3]=='SilkRoad2Market':
        SilkRoad2Market.append(row[5])
    if row[3]=='MiddleEarthMarketplace':
        MiddleEarthMarketplace.append(row[5])
    if row[3]=='BlueSkyMarketplace':
        BlueSkyMarketplace.append(row[5])
    if row[3]=='GreenRoadMarket':
        GreenRoadMarket.append(row[5])
    if row[3]=='AbraxasMarket':
        AbraxasMarket.append(row[5])
    if row[3]==' SilkRoadMarketplace':
        SilkRoadMarketplace.append(row[5])
    if row[3]=='SheepMarketplace':
        SheepMarketplace.append(row[5])
    if row[3]=='AlphaBayMarket':
        AlphaBayMarket.append(row[5])
    if row[3]=='CannabisRoadMarket':
        CannabisRoadMarket.append(row[5])

print('PandoraOpenMarket')
print(Counter(PandoraOpenMarket))

print('------------------------------------------------------------------------------------------------------')

print('BabylonMarket')
print(Counter(BabylonMarket))

print('------------------------------------------------------------------------------------------------------')

print('BlackBankMarket')
print(Counter(BlackBankMarket))

print('------------------------------------------------------------------------------------------------------')

print('EvolutionMarket')
print(Counter(EvolutionMarket))

print('------------------------------------------------------------------------------------------------------')

print('SilkRoad2Market')
print(Counter(SilkRoad2Market))

print('------------------------------------------------------------------------------------------------------')

print('MiddleEarthMarketplace')
print(Counter(MiddleEarthMarketplace))

print('------------------------------------------------------------------------------------------------------')

print('BlueSkyMarketplace')
print(Counter(BlueSkyMarketplace))

print('------------------------------------------------------------------------------------------------------')

print('GreenRoadMarket')
print(Counter(GreenRoadMarket))

print('------------------------------------------------------------------------------------------------------')

print('AbraxasMarket')
print(Counter(AbraxasMarket))

print('------------------------------------------------------------------------------------------------------')

print('SilkRoadMarketplace')
print(Counter(SilkRoadMarketplace))

print('------------------------------------------------------------------------------------------------------')

print('SheepMarketplace')
print(Counter(SheepMarketplace))

print('------------------------------------------------------------------------------------------------------')

print('AlphaBayMarket')
print(Counter(AlphaBayMarket))

print('------------------------------------------------------------------------------------------------------')

print('CannabisRoadMarket')
print(Counter(CannabisRoadMarket))
