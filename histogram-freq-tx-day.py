import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import csv
import collections
from operator import itemgetter

plotly.tools.set_credentials_file(username='kristelle', api_key='CvmqbRb7CXD5VgwhRzQV')
py.sign_in("kristelle", "CvmqbRb7CXD5VgwhRzQV")

plot1 = csv.reader(open('/Users/macbook/Desktop/FYP/files/Abraxas-transactions.csv', 'rt'), delimiter=',')
x1 = []
frequency = collections.Counter()

firstline=True
for line in plot1:
    if firstline:
        firstline=False
        continue
    frequency[line[0][:10]] += 1
frequency_list=(sorted(frequency.most_common(),key=itemgetter(0)))

x1 = [item[0] for item in frequency_list]

y1 = [item[1] for item in frequency_list]

average = sum(y1)/len(y1)

print(average)

layout = go.Layout(
    title='Frequency of transactions (ingoing/outgoing) by day in the Abraxas Market',
    xaxis=dict(
    ),
    yaxis=dict(
            title='Number of transactions'
        ),
)

data = [go.Histogram(x=x1)]


fig = go.Figure(data=data,layout=layout)
plot_url = py.plot(fig, filename='histogram-freq-day-AbraxasMarket')

