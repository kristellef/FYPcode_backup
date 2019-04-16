import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import re

# reader = csv.reader(open('/Users/macbook/Desktop/FYP/files/UH-bitcoin-heur_2s.csv', 'rt'),delimiter=',')
data=np.load('/Users/macbook/Desktop/FYP/heur2s-V4400000.npy')

'''
  0 new_black_nodes, 1 black_nodes_excluding_block, 2 cumulative_black_nodes, 3 len(total_number_nodes), 4 black_node_length, 5 number_clean_tx_in_block,
  6 number_black_tx_in_block, 7 number_tx_in_block, 8 volume_clean_tx_block, 9 volume_black_tx_in_block, 10 volume_tx_in_block, 11 number_nodes_clean,
  12 len(all_black_nodes), 13 len(all_nodes), 14 volume_total, 15volume_black
'''

colors = (255,0,0)
font = {'family' : 'serif',
        'serif' : 'cmr10',
        'weight' : 'bold',
        'size'   : 12}
plt.rc('font', **font)

def volume_block():
    y=[]
    for i in data:
        if np.array_equal(i, data[0]):
            continue
        if float(i[8])==0:
            ratio=0
        else:
            ratio=float(i[9])/float(i[8])
        y.append(ratio)
    draw_graph(y,'Ratio of volume of dirty transactions to volume of clean transactions per block')

def volume_cumulative():
    y=[]
    for i in data:
        clean = float(i[14])-float(i[15])
        if np.array_equal(i, data[0]):
            continue
        if clean==0:
            ratio=0
        else:
            ratio=float(i[15])/clean
        y.append(ratio)
    draw_graph(y,'Ratio of cumulative volume of dirty transactions to cumulative volume of clean transactions')

def nodes_block():
    y=[]
    for i in data:
        if np.array_equal(i, data[0]):
            continue
        if float(i[11])==0:
            ratio=0
        else:
            ratio=float(i[12])/float(i[11])
        y.append(ratio)
    draw_graph(y,'Ratio of number of dark nodes to number of clean nodes per block')

def nodes_cumulative():
    y=[]
    for i in data:
        clean = float(i[3])-float(i[2])
        if np.array_equal(i, data[0]):
            continue
        if clean==0:
            ratio=0
        else:
            ratio=float(i[2])/clean
        y.append(ratio)
    draw_graph(y,'Ratio of cumulative number of dark nodes to cumulative number of clean nodes')

def nodes_cumulative2():
    y=[]
    for i in data:
        if np.array_equal(i, data[0]):
            continue
        if float(i[3])==0:
            ratio=0
        else:
            ratio=float(i[2])/float(i[3])
        y.append(ratio)
    draw_graph(y,'Ratio of cumulative number of dark nodes to cumulative total number of nodes')

def new_dark_nodes():
    y=[]
    for i in data:
        if np.array_equal(i, data[0]):
            continue
        if float(i[13])==0:
            ratio=i[0]
        else:
            ratio=float(i[0])/float(i[13])
        y.append(ratio)
    draw_graph(y,'Ratio of number of new dark nodes to number of nodes per block')


def new_dark_nodes2():
    y=[]
    temp=0
    previous=0
    for i in data:
        if np.array_equal(i, data[0]):
            continue
        if np.array_equal(i, data[0]):
            temp = i[3]
        else:
            temp = float(i[3])-float(previous)
        if float(temp)==0:
            ratio=0
        else:
            ratio=float(i[0])/float(temp)
        y.append(ratio)
        previous=i[3]
    draw_graph(y,'Ratio of number of new dark nodes to number of all new nodes per block')


def draw_graph(y,title):
    x=[]
    for i in range(0,400000):
        x.append(i)

    plt.scatter(x,y,s=1)
    plt.title(title)
    plt.xlabel('block number')
    plt.ylabel('ratio dirty:clean')

    print("showing")
    plt.show()
    plt.clf()
    # plt.savefig('/Users/macbook/Desktop/FYP/charts/paint_black/ratio_nodes_cumulative.png')

# volume_block()
# volume_cumulative()
# nodes_block()
# nodes_cumulative()
# nodes_cumulative2()
new_dark_nodes2()
