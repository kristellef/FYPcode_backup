import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import csv
import pandas as pd
from operator import itemgetter

# create chart of received transactions and sent transactions

plotly.tools.set_credentials_file(username='kristelle', api_key='CvmqbRb7CXD5VgwhRzQV')
py.sign_in("kristelle", "CvmqbRb7CXD5VgwhRzQV")

plot = csv.reader(open('/Users/macbook/Desktop/FYP/files/chart_data.csv', 'rt'), delimiter=',')

# positive array
x1 = []
y1 = []
# negative array
x2 = []
y2 = []

list1=[]
list2=[]

next(plot)
for row in plot:
    temp=[]
    value = float(row[1])
    if value > 0:
        temp.extend((pd.to_datetime(row[0]),value))
        list1.append(temp)
    else:
        temp.extend((pd.to_datetime(row[0]), value))
        list2.append(temp)
x1 = [item[0] for item in sorted(list1, key=itemgetter(0))]
x2 = [item[0] for item in sorted(list2, key=itemgetter(0))]

y1 = [item[1] for item in sorted(list1, key=itemgetter(0))]
y2 = [item[1] for item in sorted(list2, key=itemgetter(0))]

layout = go.Layout(
    title='Bitcoins received and sent by addresses in Abraxas Market from December 2014 to March 2017',
    xaxis=dict(
    ),
    yaxis=dict(
        title='Amount (in BTC)',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
        )
)
# Create traces
trace0 = go.Scatter(
    x = x2,
    y = y2,
    mode = 'lines',
    name = 'Sent',
    line=dict(
        color='rgb(17, 157, 255)',
    ),
)

trace1 = go.Scatter(
    x = x1,
    y = y1,
    mode = 'lines',
    name = 'Received',
    line=dict(
        color='rgb(255, 115, 17)',
    ),
)

data = [trace0, trace1]

fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='transactions-abraxas')

