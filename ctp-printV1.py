#!/usr/bin/env python
# -*- coding: utf-8 -*-


import block
from optparse import OptionParser
import numpy as np
from collections import Counter
import os
import numpy as np
import csv

black_nodes=set()
# number of transactions with dirty bitcoins
count_tx_black=0
count_total_tx=0
data = np.load('/Users/macbook/Desktop/FYP/files/darknet_minimise_1to2 V2.npy')
for i in data:
    if i not in black_nodes:
        black_nodes.add(i)
# initial number of black nodes to be used later to compute the number of new dark nodes
inital_black_nodes = len(black_nodes)
x = np.array([])

# TODO: create a numpy file containing the comuptations: number of new black nodes/number of old black nodes; number of black nodes/number of clean nodes;
# number of tx with dirty bitcoin/number of tx with clean bitcoin; volume of tx (BTC) with dirty bitcoin/volume of tx with clean bitcoin
# Create a list of lists for each computations: [[black,clean],[black,clean]]

#########################################################################################
#########################################################################################

# included
new_black_array=[]
new_black_array_ratio=[]
black_clean_tx_array=[]
black_clean_volume_array=[]
number_nodes_clean_black_array=[]

writer = csv.writer(open('/Users/macbook/Desktop/FYP/files/UH-bitcoin-heur_2s.csv', 'a+'))

#########################################################################################
#########################################################################################

def parse_command_line():
    parser = OptionParser()


    parser.add_option("--curr", action='store', dest="currency", default="bitcoin",
                      help="which currency is being analysed")

    parser.add_option("--heur", action='store', dest="heuristic", default="1",
                      help="which heuristic is being analysed")

    parser.add_option("--filter-in", action='store_true', dest="filter_in",
                      help="filter if number of inputs is 1")

    parser.add_option("--filter-out", action='store_true', dest="filter_out",
                      help="filter if number of outputs is 1")

    parser.add_option("--pickled", dest="pickled", action="store_true")

    options, args = parser.parse_args()

    options.heuristic = "heur_%s"%options.heuristic
    return options, args

def print_red(options, blk_id):
    global count_tx_black
    global count_total_tx
    global black_nodes
    black_nodes_excluding_block = len(black_nodes)
    number_tx_in_block=0
    number_black_tx_in_block=0
    volume_tx_in_block=0
    volume_black_tx_in_block=0
    # contains all the nodes involved in transactions with black nodes within this block (inputs and outputs)
    all_black_nodes=[]
    # contains all the nodes involved in transactions within this block
    all_nodes=[]
    if not options.pickled:
        blk = block.load_id(None, int(blk_id), "/Volumes/KIKS/UH-bitcoin-heur_2s/UH-%s-%s"%(options.currency, options.heuristic))
    else:
        blk = block.load_id(options.currency, int(blk_id))
    for (pos, ( transaction_hash, transaction_fee, new_elements, transaction_input,transaction_output) ) in enumerate(blk.transactions):
        if len(transaction_input) == 1 and options.filter_in:
            continue
        if len(transaction_output) == 1 and options.filter_out:
            continue

        inputs=[]
        count_total_tx+=1
        number_tx_in_block +=1
        for i in transaction_input:
            inputs.append(i[0])
            volume_tx_in_block+=i[1]
            all_nodes.append(i[0])
            # if i[0] not in all_nodes:
            #     all_nodes.append(i[0])

        for j in transaction_output:
            all_nodes.append(j[0])

        if bool(set(inputs) & black_nodes):
            count_tx_black+=1
            number_black_tx_in_block+=1
            for i in transaction_input:
                volume_black_tx_in_block+=i[1]
                all_black_nodes.append(i[0])

            for i in transaction_output:
                all_black_nodes.append(i[0])
                black_nodes.add(i[0])

        # print ("TX:::  (%s) %s"%(blk_id, transaction_hash))
        #
        # print ("FULL: %s >> %s |%s "%( transaction_input, transaction_output, new_elements ))
        # try:
        #     (rh,rf,rs,rin,rout) = blk.short_transactions[pos]
        #     print ("REDU: %s >> %s |%s "%(  rin, rout, rs ))
        # except: pass
        #
        # print  (120*"-")
    all_black_nodes=list(set(all_black_nodes))
    all_nodes=list(set(all_nodes))
    new_black_nodes = len(black_nodes) - black_nodes_excluding_block
    # new black nodes, number of black nodes before entering the block
    new_black=[new_black_nodes,black_nodes_excluding_block]
    number_clean_tx_in_block=number_tx_in_block-number_black_tx_in_block
    # clean, black, total
    black_clean_tx=[number_clean_tx_in_block,number_black_tx_in_block,number_tx_in_block]
    volume_clean_tx_block=volume_tx_in_block - volume_black_tx_in_block
    # clean, black, total
    volume_black_clean=[volume_clean_tx_block,volume_black_tx_in_block,volume_tx_in_block]
    number_nodes_clean = len(all_nodes) - len(all_black_nodes)
    # clean, black, total
    number_nodes_clean_black = [number_nodes_clean,len(all_black_nodes),len(all_nodes)]

    row=[new_black,black_clean_tx,volume_black_clean,number_nodes_clean_black]
    
    writer.writerow(row)

opts, args = parse_command_line()

args=[]
path = '/Volumes/KIKS/UH-bitcoin-heur_2s/UH-bitcoin-heur_2/'
for filename in os.listdir(path):
    if path+filename=='/Volumes/KIKS/UH-bitcoin-heur_2s/UH-bitcoin-heur_2/.DS_Store':
        continue
    for files in os.listdir(path + filename):
        args.append(files.split('.')[0])

for a in args:
    if args.index(a)%1000==0:
        print(str(args.index(a)) + '/' + str(len(args)))
    print_red(opts, a)
