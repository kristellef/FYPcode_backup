import csv, time
from operator import itemgetter

# For a given index return all data in the file
def getFileData(index):
    path = "/Users/macbook/Desktop/csvs/{}.csv".format(index)
    filedata = {}

    with open(path) as f:
        for row in csv.reader(f):
            filedata[row[0]] = row

    return filedata

darknet = csv.reader(open('/Users/macbook/Desktop/darknet.csv', 'rt'), delimiter=',')
writer = csv.writer(open('/Users/macbook/Desktop/mapping-darknet.csv','a+'))

data = []

for row in darknet:
    data.append(row)

data = sorted(data, key=itemgetter(0))

currentIndex = data[0][0][0:3]
filedata = getFileData(currentIndex)
count = 0
start = time.time()

for row in data:
    # Change file if needed
    if row[0][0:3] != currentIndex:
        currentIndex = row[0][0:3]
        filedata = getFileData(currentIndex)

    # Find in file
    if not row[0] in filedata:
        # Skip if not in file
        print ('Address ',row[0], ' not in file.')
        continue

    # Write row in file
    writer.writerow([row[0],filedata[row[0]][1],filedata[row[0]][2],row[1]])
    count+=1

    if count % 1000 == 0:
        print(count, '/1.817.311 in ',(time.time()-start)/60,'min' )


print('done')