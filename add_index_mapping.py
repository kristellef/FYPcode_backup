import csv

heuristic0 = csv.reader(open('/Users/macbook/Desktop/map_addresses-1_500000.csv', 'rt'), delimiter=',')
writer = csv.writer(open('/Users/macbook/Desktop/mapping0.csv','wt'))
counter = 0
for row in writer:
    counter+=1
    row.append(counter)
    writer.writerow(row)

print('done')

