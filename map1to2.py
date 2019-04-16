import numpy as np

npyarray=[]
count=0
data = []
mapping0to1 = []
data = np.load('/Users/macbook/Desktop/FYP/files/minimise_user-1_500000-heur2s.npy')
data1 = np.load('/Users/macbook/Desktop/FYP/files/minimise_user-1_500000-heur1.npy')
mapping0to1 = np.load('/Users/macbook/Desktop/FYP/files/darknet_minimise_0to1 V2.npy')

for mapping in mapping0to1:
    npyarray.append(data[mapping])
    count += 1
    if count % 1000 == 0:
        print(count, '/1.817.311')

np.save('/Users/macbook/Desktop/FYP/files/darknet_minimise_1to2 V2.npy', npyarray)

output = np.load('/Users/macbook/Desktop/FYP/files/darknet_minimise_1to2 V2.npy')
print(output.size)

print('done')


print((np.unique(output)).size)
print(np.unique(output))
print(output.size)
print((np.unique(data1)).size)
