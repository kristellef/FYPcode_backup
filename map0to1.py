import numpy as np
import csv


mapping_csv = csv.reader(open('/Users/macbook/Desktop/FYP/files/mapping-darknet.csv', 'rt'), delimiter=',')
npyarray=[]
count=0
data = []
data = np.load('/Users/macbook/Desktop/FYP/files/minimise_user-1_500000-heur1.npy')

print(data.size)

for row in mapping_csv:
    # minimise using index of address in files map-addresses
    # index = int(row[2])

    # minimise using address ID
    index = int(row[1])
    npyarray.append(data[index])
    count += 1
    if count % 1000 == 0:
        print(count, '/1.817.311')

np.save('/Users/macbook/Desktop/FYP/files/dnklnd.npy', npyarray)

output = np.load('/Users/macbook/Desktop/FYP/files/darknet_minimise_0to1 V2.npy')
print(output.size)

print('done')


