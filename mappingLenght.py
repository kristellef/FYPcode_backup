import csv

row_count = sum(1 for row in (open('/Users/macbook/Desktop/mapping-darknet copy.csv', 'rt')))
print(row_count)