import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import csv
import collections
import random
from collections import Counter
from operator import itemgetter
import statistics
import datetime
from functools import reduce

plotly.tools.set_credentials_file(username='kristelle', api_key='CvmqbRb7CXD5VgwhRzQV')
py.sign_in("kristelle", "CvmqbRb7CXD5VgwhRzQV")

reader = csv.reader(open('/Users/macbook/Desktop/FYP/files/AlphaBayMarket-transactions/AlphaBay_transactions.csv','rt'),delimiter=',')

dictionary=[]



transactions = []
for row in reader:
    if len(row) == 7 and row[0] != 'date' and row[2]!='':
        transactions.append(row)

# Sort transactions by date
transactions = sorted(transactions, key=lambda x: x[0])

index = 1
numberTransactions = len(transactions)

currentDate = transactions[0][0][:10]
currentTransactions = [transactions[0]]

while index < numberTransactions:
    transaction = transactions[index]
    temp=[]
    temp_date_arr=[]
    if transaction[0][:10] != currentDate:

        # Do something with transactions of current day before they disappear
        # Code below is example

        # print(currentDate,len(currentTransactions))
        for i in range(0,len(currentTransactions)):
            temp.append(float(currentTransactions[i][2]))
        for j in range(1,len(currentTransactions)):
            previous = datetime.datetime.strptime(currentTransactions[j-1][0], '%Y-%m-%d %H:%M:%S')
            next = datetime.datetime.strptime(currentTransactions[j][0], '%Y-%m-%d %H:%M:%S')
            temp_date = next - previous
            temp_date_arr.append(temp_date)
        if (len(currentTransactions)==1):
            temp_date_arr.append(0.0)

        median_date = statistics.median(temp_date_arr)
        median_amount = statistics.median(temp)

        # avg_date = reduce(lambda x, y: x + y, temp_date_arr) / len(temp_date_arr)
        # avg_amount=reduce(lambda x, y: x + y, temp) / len(temp)

        row = [str(median_date),median_amount, currentDate]
        dictionary.append(row)
        # dictionary[str(median_date)] = median_amount

        # Change current day and replace current transactions
        currentDate = transaction[0][:10]
        currentTransactions = [transaction]
    else:
        # Same day so we add to array and move on to next one
        currentTransactions.append(transaction)

    index += 1

dictionary.sort(key=itemgetter(2))
x=[]
y1=[]
y2=[]

for i in dictionary:
    x.append(datetime.datetime.strptime(i[2], '%Y-%m-%d'))
    time=[]
    total_time = 0
    time = (i[0].split(':'))
    if len(time)>1:
        total_time = float(time[0])*60+float(time[1])+(float(time[2])/60)
    y1.append(total_time)
    y2.append(i[1])

trace1 = go.Scatter(
    x=x,
    y=y2,
    name='Received Amount (in BTC)'
)
trace2 = go.Scatter(
    x=x,
    y=y1,
    name='Tx Interval (in minutes)',
    yaxis='y2'
)
data = [trace1, trace2]
layout = go.Layout(
    title='Inflow transaction pattern of AlphaBayMarket by day',
    yaxis=dict(
        title='Median of Received Amount (in BTC)'
    ),
    yaxis2=dict(
        title='Median of Tx Interval (in minutes)',
        titlefont=dict(
            color='rgb(148, 103, 189)'
        ),
        tickfont=dict(
            color='rgb(148, 103, 189)'
        ),
        overlaying='y',
        side='right'
    )
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='Median-tx-amount-AlphaBayMarket')

trace1 = go.Scatter(
    x = y2,
    y = y1, #time interval
    mode = 'markers',
)

data = [trace1]

layout = dict(title = 'Inflow transaction pattern of AlphaBayMarket by day',
              yaxis = dict(title='Median of Tx Interval (in minutes)'),
              xaxis = dict(title='Median of Received Amount (in BTC)')
             )

fig = dict(data=data, layout=layout)
py.plot(fig, filename='scatter-median-AlphaBayMarket')