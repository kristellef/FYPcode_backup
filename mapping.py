import json, csv, os

darknet = csv.reader(open('/Users/macbook/Desktop/darknet.csv', 'rt'), delimiter=',')
writer = csv.writer(open('/Users/macbook/Desktop/mapping_heur0.csv','a'))
count=0
for row in darknet:
    path = "/Users/macbook/Desktop/csvs/" + str(row[0][0:3]) + ".csv"
    mapping = csv.reader(open(path))
    count += 1
    if count % 5000 == 0:
        print(count, '/1.817.311')
    for row2 in mapping:
        if row[0] == row2[0]:
            writer.writerow(row2)
row_count = sum(1 for row in (open('/Users/macbook/Desktop/mapping_heur0.csv', 'rt')))
print(row_count)
