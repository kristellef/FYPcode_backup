import numpy as np
import csv

userID = np.load('/Users/macbook/Desktop/FYP/files/darknet_minimise_1to2 V2.npy')
addresses = csv.reader(open('/Users/macbook/Desktop/FYP/files/mapping-darknet.csv','rt'),delimiter = ',')
writer = csv.writer(open('/Users/macbook/Desktop/FYP/files/darknet_userID.csv','wt'))

i=0
user = 0

array=[]
for user in userID:
    array.append(int(user))

for address in addresses:
    user = array[i]
    address.append(user)
    writer.writerow(address)
    i += 1
    if i % 1000 ==0:
        print(i)
    # print(address)
