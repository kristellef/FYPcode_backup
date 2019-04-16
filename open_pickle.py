# import os
#
# array=[]
# path = '/Volumes/KIKS/UH-bitcoin-heur_2s/UH-bitcoin-heur_2/'
# for filename in os.listdir(path):
#     if path+filename=='/Volumes/KIKS/UH-bitcoin-heur_2s/UH-bitcoin-heur_2/.DS_Store':
#         continue
#     for files in os.listdir(path + filename):
#         array.append(files.split('.')[0])
# print(array)

import numpy as np

data=np.load('/Users/macbook/desktop/FYP/tx.npy')
for a in data:
    print a
