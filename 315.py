import numpy as np

data1=np.load('/Users/macbook/Desktop/FYP/files/minimise_user-1_500000-heur1.npy')
data2=np.load('/Users/macbook/Desktop/FYP/files/minimise_user-1_500000-heur2s.npy')

print(len(data1))

counter=0
for i in data2:
    if i==315:
        counter+=1

print(counter)


'''
there are 6864734 users from heur1 (out of 346516753) that are mapped to user 315 in heur2

'''
