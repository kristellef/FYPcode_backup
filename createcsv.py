import json, csv, os

mapping_csv = csv.reader(open('/Users/macbook/Desktop/mapping0.csv', 'rt'), delimiter=',')

count = 0
data = []
for row in mapping_csv:
    count +=1

    if count%50000==0:
        print(count,'/346.516.753')

    if len(row) <=3:
        path = "/Users/macbook/Desktop/csvs/"+str(row[0][0:3])+".csv"
        if os.path.isfile(path) :
            writer = csv.writer(open(path,'a'))
            writer.writerow(row)
        else:
            temp_csp = csv.writer(open(path,'w+'))
            temp_csp.writerow(row)
    if len(row)>3:
        id = row[len(row)-2]
        counter = row[len(row)-1]
        for i in range(0,len(row)-2):
            path = "/Users/macbook/Desktop/csvs/" + str(row[i][0:3]) + ".csv"
            data = [row[i], id, counter]
            if os.path.isfile(path):
                writer = csv.writer(open(path,'a'))
                writer.writerow(data)
            else:
                temp_csp = csv.writer(open(path,'w+'))
                temp_csp.writerow(data)
print('done')
