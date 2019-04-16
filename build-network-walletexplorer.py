# import csv
# import networkx as nx
# from collections import Counter
# import matplotlib.pyplot as plt
# # from graph_tool.all import *
#
# CannabisRoadMarket = csv.reader(open('/Users/macbook/Desktop/FYP/files/CannabisRoadMarket-transactions/CannabisRoadMarket_transactions.csv','rt'),delimiter=',')
# GreenRoad = csv.reader(open('/Users/macbook/Desktop/FYP/files/GreenRoadMarket-transactions/GreenRoadMarket-transactions.csv','rt'),delimiter=',')
# Babylon = csv.reader(open('/Users/macbook/Desktop/FYP/files/BabylonMarket-transactions/Babylon_transactions.csv','rt'),delimiter=',')
#
#
# cannabisRoad_in=[]
# cannabisRoad_out=[]
#
# greenRoad_in=[]
# greenRoad_out=[]
#
# babylon_in=[]
# babylon_out=[]
#
# for line in CannabisRoadMarket:
#     if len(line) == 7 and line[0] != 'date':
#         if line[2] != '':
#             cannabisRoad_in.append(line[1])
#         else:
#             if line[4] != '(fee)':
#                 cannabisRoad_out.append(line[4])
#
# for line in GreenRoad:
#     if len(line) == 7 and line[0] != 'date':
#         if line[2] != '':
#             greenRoad_in.append(line[1])
#         else:
#             if line[4] != '(fee)':
#                 greenRoad_out.append(line[4])
#
# for line in Babylon:
#     if len(line) == 7 and line[0] != 'date':
#         if line[2] != '':
#             babylon_in.append(line[1])
#         else:
#             if line[4] != '(fee)':
#                 babylon_out.append(line[4])
#
# vertex_temp = cannabisRoad_out + cannabisRoad_in + greenRoad_in + greenRoad_out + babylon_in + babylon_out + ['CannabisRoadMarket','GreenRoadMarket','BabylonMarket']
# # vertex_temp = greenRoad_in + greenRoad_out + babylon_in + babylon_out + ['GreenRoadMarket','BabylonMarket']
#
# dictionary_count=dict(Counter(vertex_temp))
# vertex=list(dictionary_count.keys())
#
#
# G=nx.Graph()
# G.add_nodes_from(vertex)
#
# edges=[]
#
# for elem in cannabisRoad_in:
#     edges.append((elem, 'CannabisRoadMarket'))
#
# for elem in cannabisRoad_out:
#     edges.append(('CannabisRoadMarket', elem))
#
# for elem in greenRoad_in:
#     edges.append((elem,'GreenRoadMarket'))
#
# for elem in greenRoad_out:
#     edges.append(('GreenRoadMarket',elem))
#
# for elem in babylon_in:
#     edges.append((elem, 'BabylonMarket'))
#
# for elem in babylon_out:
#     edges.append(('BabylonMarket', elem))
#
# # i=0
# # for elem in greenRoad_in+greenRoad_out:
# #     if elem in babylon_in+babylon_out:
# #         i+=1
#
# for edge in edges:
#     G.add_edge(*edge)
#
# print(G.nodes())
# print('edges added')
# nx.draw(G, node_size=2, width=0.2)
# plt.savefig("/Users/macbook/Desktop/FYP/charts/network-2.png")

import csv

CannabisRoad = csv.reader(open('/Users/macbook/Desktop/FYP/files/CannabisRoadMarket-transactions/CannabisRoadMarket_transactions.csv','rt'),delimiter=',')
GreenRoad = csv.reader(open('/Users/macbook/Desktop/FYP/files/GreenRoadMarket-transactions/GreenRoadMarket-transactions.csv','rt'),delimiter=',')
Babylon = csv.reader(open('/Users/macbook/Desktop/FYP/files/BabylonMarket-transactions/Babylon_transactions.csv','rt'),delimiter=',')
BlackBank = csv.reader(open('/Users/macbook/Desktop/FYP/files/BlackBankMarket-transactions/BlackBankMarket-transactions.csv','rt'),delimiter=',')
AlphaBay = csv.reader(open('/Users/macbook/Desktop/FYP/files/AlphaBayMarket-transactions/AlphaBay_transactions.csv','rt'),delimiter=',')
Abraxas = csv.reader(open('/Users/macbook/Desktop/FYP/files/AbraxasMarket-transactions/AbraxasMarket-transactions.csv','rt'),delimiter=',')
BlueSky = csv.reader(open('/Users/macbook/Desktop/FYP/files/BlueSkyMarketplace-transactions/BlueSkyMarketplace-transactions.csv','rt'),delimiter=',')
MiddleEarth = csv.reader(open('/Users/macbook/Desktop/FYP/files/MiddleEarthMarketplace-transactions/MiddleEarthMarketplace-transactions.csv','rt'),delimiter=',')
Nucleus = csv.reader(open('/Users/macbook/Desktop/FYP/files/NucleusMarket-transactions/NucleusMarket-transactions.csv','rt'),delimiter=',')
Pandora = csv.reader(open('/Users/macbook/Desktop/FYP/files/PandoraOpenMarket-transactions/PandoraOpenMarket-transactions.csv','rt'),delimiter=',')
Sheep = csv.reader(open('/Users/macbook/Desktop/FYP/files/SheepMarketplace-transactions/SheepMarketplace-transactions.csv','rt'),delimiter=',')
SilkRoad2 = csv.reader(open('/Users/macbook/Desktop/FYP/files/SilkRoad2Market-transactions/SilkRoad2Market-transactions.csv','rt'),delimiter=',')

def print_line(csv_file):
    for line in csv_file:
        print(line)
        break

array=[Abraxas,BlueSky,MiddleEarth,Nucleus,Pandora,Sheep,SilkRoad2]

for param in array:
    print_line(param)