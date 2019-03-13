#!/usr/bin/env python
# -*- coding: utf-8 -*-


import block
from optparse import OptionParser
import numpy as np
from collections import Counter
import os
import numpy as np

black_nodes=[]
total_inputs=[]
# number of transactions with dirty bitcoins
count_tx_black=0
count_total_tx=0
data = np.load('/Users/macbook/Desktop/FYP/files/darknet_minimise_1to2 V2.npy')
for i in data:
    if i not in black_nodes:
        black_nodes.append(i)
# initial number of black nodes to be used later to compute the number of new dark nodes
inital_black_nodes = len(black_nodes)


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
        outputs=[]
        count_total_tx+=1
        number_tx_in_block +=1
        for i in transaction_input:
            inputs.append(i[0])
            total_inputs.append(i)
            volume_tx_in_block+=i[1]
            if i[0] not in all_nodes:
                all_nodes.append(i[0])

        for j in transaction_output:
            if j[0] not in all_nodes:
                all_nodes.append(j[0])

        if bool(set(inputs) & set(black_nodes)):
            count_tx_black+=1
            number_black_tx_in_block+=1
            for i in transaction_input:
                volume_black_tx_in_block+=i[1]
                all_black_nodes.append(i[0])
            for i in transaction_output:
                outputs.append(i[0])
            for i in outputs:
                if i not in all_black_nodes:
                    all_black_nodes.append(i)
                if i not in black_nodes:
                    black_nodes.append(i)
        print ("TX:::  (%s) %s"%(blk_id, transaction_hash))

        print ("FULL: %s >> %s |%s "%( transaction_input, transaction_output, new_elements ))
        try:
            (rh,rf,rs,rin,rout) = blk.short_transactions[pos]
            print ("REDU: %s >> %s |%s "%(  rin, rout, rs ))
        except: pass

        print  (120*"-")
    new_black_nodes = len(black_nodes) - black_nodes_excluding_block
    new_black_array.append(new_black_nodes)
    # new black nodes, number of black nodes before entering the block
    new_black=[new_black_nodes,black_nodes_excluding_block]
    new_black_array_ratio.append(new_black)
    number_clean_tx_in_block=number_tx_in_block-number_black_tx_in_block
    # clean, black, total
    black_clean_tx=[number_clean_tx_in_block,number_black_tx_in_block,number_tx_in_block]
    black_clean_tx_array.append(black_clean_tx)
    volume_clean_tx_block=volume_tx_in_block - volume_black_tx_in_block
    # clean, black, total
    volume_black_clean=[volume_clean_tx_block,volume_black_tx_in_block,volume_tx_in_block]
    black_clean_volume_array.append(volume_black_clean)
    number_nodes_clean = len(all_nodes) - len(all_black_nodes)
    # clean, black, total
    number_nodes_clean_black = [number_nodes_clean,len(all_black_nodes),len(all_nodes)]
    number_nodes_clean_black_array.append(number_nodes_clean_black)
    print(new_black)
    print(black_clean_tx)
    print(volume_black_clean)
    print(number_nodes_clean_black)
opts, args = parse_command_line()

# args=[]
# path = '/Volumes/KIKS/UH-bitcoin-heur_2s/UH-bitcoin-heur_2/'
# for filename in os.listdir(path):
#     if path+filename=='/Volumes/KIKS/UH-bitcoin-heur_2s/UH-bitcoin-heur_2/.DS_Store':
#         continue
#     for files in os.listdir(path + filename):
#         args.append(files.split('.')[0])

args=['890','879','930']

for a in args:
    print(a)
    print_red(opts, a)

np.save('/Users/macbook/desktop/FYP/new_black_nodes', np.array(new_black_array_ratio))
np.save('/Users/macbook/desktop/FYP/clean_black_tx', np.array(black_clean_tx_array))
np.save('/Users/macbook/desktop/FYP/clean_black_volume', np.array(black_clean_volume_array))
np.save('/Users/macbook/desktop/FYP/clean_black_nodes', np.array(number_nodes_clean_black_array))
