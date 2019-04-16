from lib.db import DB
from lib.DisjointSet import DisjointSet
from pprint import pprint
from lib.BitcoinBlockCrawler import BitcoinBlockCrawler
import json, csv
from migrations.createTables import createTables
import psycopg2

# Load configuration file and connect to database
with open('config.json') as json_file:
    config = json.load(json_file)

db = DB(config['DB'])
createTables(db)

# queries1 = []
# addresses = []
#
# queries1 = """SELECT * FROM darknet_addresses;"""
# addresses = db.execute([queries1])
#
# queries2 = []
# # query2 = """UPDATE addresses SET id = (SELECT id FROM address_matching where address={0});"""
# query2 = """SELECT id FROM address_mapping where address='{0}';"""
# for row in addresses:
#     print(query2.format(row[0]))
#     queries2.append(query2.format(row[0]))
#     print(db.execute(queries2))
# db.execute(queries2, False)



# queries=[]
# query="""INSERT INTO address_mapping (address, id) VALUES ('{0}',{1});"""

# csv_file = csv.reader(open('/Users/macbook/Desktop/map_addresses-1_500000.csv', 'rt'), delimiter=',')
# index=0
# total = 176930000

# for row in csv_file:
#     # try:
#     #     id = int(row[1])
#     # except ValueError:
#     #     print('Please enter an integer')
#     #     continue
#     # queries.append(query.format(row[0], id))
#     if row[0] == '18aCigCGAuhfT7TyPyGTpzjWJpHdnQ7GML':
#         print(row)
#         break
#
#     index+=1
#     if index % 1000000 == 0:
#         # db.execute(queries,False)
#         # queries = []
#         print('Passed ',index,'/',total)
#
# print('done')
#

darknet_csv= csv.writer(open('/Users/macbook/Desktop/darknet.csv', 'wt'))
conn = psycopg2.connect(database="fyp",
    user="macbook", password="'", host="127.0.0.1", port="5432")
cur = conn.cursor()
cur.execute('SELECT * from darknet_addresses')
rows = cur.fetchall()
for row in rows:
    darknet_csv.writerow(row)
row_count = sum(1 for row in (open('/Users/macbook/Desktop/darknet.csv', 'rt')))
print (row_count)