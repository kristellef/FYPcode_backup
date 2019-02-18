import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import csv
import random
from collections import Counter

plotly.tools.set_credentials_file(username='kristelle', api_key='CvmqbRb7CXD5VgwhRzQV')
py.sign_in("kristelle", "CvmqbRb7CXD5VgwhRzQV")

reader = csv.reader(open('/Users/macbook/Desktop/FYP/files/AlphaBayMarket-transactions/AlphaBay_transactions.csv','rt'),delimiter=',')

mydict_in=[]
mydict_out=[]

for line in reader:
    if len(line)==7 and line[0]!='date':
        mydict_in.append(line[1])
        mydict_out.append(line[4])

dict_in = Counter(mydict_in)
dict_out = Counter(mydict_out)

# del dictionary_out['(fee)']
# del dictionary_out['']
# del dictionary['']

dictionary_out={}
dictionary={}

for k, v in dict_out.items():
    if len(k) > 16:
        dictionary_out[k]=v

for k, v in dict_in.items():
    if len(k) <= 16:
        dictionary[k] = v

# dictionary = {key:val for key, val in dictionary.items() if val !=1}
# dictionary_out = {key:val for key, val in dictionary_out.items() if val !=1}

keys = list(dictionary.keys())
values = list(dictionary.values())

keys_out = list(dictionary_out.keys())
values_out = list(dictionary_out.values())

keys.append('AlphaBayMarket')
keys_out.append('AlphaBayMarket')

# labels=[]
# for el in keys:
#     if len(el)>16:
#         labels.append(el)
#     else:
#         labels.append('')
#
# labels[len(labels)-1]='AlphaBayMarket'
#
# labels_out=[]
# for el in keys_out:
#     if len(el)>16:
#         labels_out.append(el)
#     else:
#         labels_out.append('')
#
# labels_out[len(labels_out)-1]='AlphaBayMarket'

def random_color(n):
    color = ["#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)])
             for i in range(n)]
    return color

data = dict(
    type='sankey',
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(
        color = "black",
        width = 0.5
      ),
      label = keys,
      color = random_color(len(keys))
    ),
    link = dict(
      source = list(range(0, len(keys)-1)),
      target = [len(keys)-1]*(len(keys)-1),
      value = values
  ))

layout =  dict(
    title = "Flow of ingoing transactions from AlphaBayMarket to known wallets",
    font = dict(
      size = 10
    )
)

fig = dict(data=[data], layout=layout)
py.plot(fig, validate=False,filename='AlphaBayMarket-ingoing')
