import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import csv

plotly.tools.set_credentials_file(username='kristelle', api_key='CvmqbRb7CXD5VgwhRzQV')
py.sign_in("kristelle", "CvmqbRb7CXD5VgwhRzQV")

plot1 = csv.reader(open('/Users/macbook/Desktop/FYP/files/GreenRoadMarket-in-out.csv', 'rt'), delimiter=',')
plot2 = csv.reader(open('/Users/macbook/Desktop/FYP/files/BabylonMarket-in-out.csv', 'rt'), delimiter=',')
x1 = []
y1 = []
x2 = []
y2 = []

for line in plot1:
    if line[0] != 'Received' and line[1] != 'Sent':
        x1.append(line[0])
        # y1.append(line[1])
for line in plot2:
    if line[0] != 'Received' and line[1] != 'Sent':
        x2.append(line[0])
        # y2.append(line[1])
layout = go.Layout(
    title='Amount of Bitcoin received by each address in the Babylon Market and in Green Road Market',
    xaxis=dict(
        title='Received (in BTC)',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
            title='Number of addresses',
        )
)
# Create traces
trace0 = go.Scatter(
    x = x2,
    mode = 'markers',
    name = 'Babylon Market',
    marker=dict(
        color='rgb(17, 157, 255)',
        opacity=0.5,
        line=dict(
            color='rgb(17, 157, 255)',
        )
    ),
)

trace1 = go.Scatter(
    x = x1,
    mode = 'markers',
    name = 'Green Road Market',
    marker=dict(
        color='rgb(255, 115, 17)',
        opacity=0.5,
        line=dict(
            color='rgb(255, 115, 17)',
        )
    ),
)

data = [trace0, trace1]

fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='transactions-in-out')