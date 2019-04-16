import numpy as np
import csv

userID = np.load('/Users/macbook/Desktop/FYP/files/darknet_minimise_1to2 V2.npy')
addresses = csv.reader(open('/Users/macbook/Desktop/FYP/files/mapping-darknet.csv','rt'),delimiter = ',')
writer_heur2 = csv.writer(open('/Users/macbook/Desktop/FYP/files/darknet_userID.csv','wt'))

userID_heur1 = np.load('/Users/macbook/Desktop/FYP/files/minimise_user-1_500000-heur1.npy')
darknet = csv.reader(open('/Users/macbook/Desktop/FYP/files/darknet_userID.csv', 'rt'), delimiter=',')
writer_heur1 = csv.writer(open('/Users/macbook/Desktop/FYP/files/darknet_userID-V2.csv','wt'))

i=0
user = 0

array=[]
for user in userID:
    array.append(int(user))

for address in addresses:
    user = array[i]
    address.append(user)
    writer_heur2.writerow(address)
    i += 1
    if i % 1000 ==0:
        print(i)
    # print(address)

for row in darknet:
    # address id is row[1]
    user_id = userID_heur1[int(row[1])]
    row.append(user_id)
    writer_heur1.writerow(row)
    if i % 1000 == 0:
        print(i)
    i += 1