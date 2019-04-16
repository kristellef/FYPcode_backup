import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import csv

plotly.tools.set_credentials_file(username='kristelle', api_key='CvmqbRb7CXD5VgwhRzQV')
py.sign_in("kristelle", "CvmqbRb7CXD5VgwhRzQV")

plot1 = csv.reader(open('/Users/macbook/Desktop/FYP/files/Abraxas-transactions.csv', 'rt'), delimiter=',')
x1 = []

firstline=True
for line in plot1:
    if firstline:
        firstline=False
        continue
    if float(line[1])>0:
        x1.append(line[1])


layout = go.Layout(
    title='Number of ingoing transactions in the Abraxas Market',
    xaxis=dict(
        title = 'Amount of Bitcoins received'
    ),
    yaxis=dict(
            title = 'Number of transactions'
        ),
)

data = [go.Histogram(x=x1)]


fig = go.Figure(data=data,layout=layout)
plot_url = py.plot(fig, filename='histogram-Abraxas')