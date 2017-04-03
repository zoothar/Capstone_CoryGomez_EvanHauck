import plotly.graph_objs as go
from plotly.graph_objs import Scatter
import pandas as pd
import plotly.offline as offline
import sqlite3
import datetime
import django
django.setup()
from WeatherStation.models import Record
from pytz import timezone
from datetime import datetime

pst = timezone('UTC')

slct = 1
sdate = pst.localize(datetime(2016, 3, 2))
edate = pst.localize(datetime(2017, 2, 3))
sdate2 = pst.localize(datetime(2016, 4, 4))

if slct == 0:
    x = []
    y = []
    for i in Record.objects.filter(timeStamp__range=(sdate, edate)):
        x.append(i.timeStamp)
        y.append(i.battAvg)

    df = pd.DataFrame({'x': x, 'y': y})
    df.head()

    data = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='Battery Voltages')]
    offline.plot({
        'data': data,
        'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='Voltage', type='log'))
    }, output_type='div')

elif slct == 1:
    x = []
    y = []
    for i in Record.objects.filter(timeStamp__range=(sdate2, edate)):
        x.append(i.timeStamp)
        y.append(i.pTempCAvg)

    df = pd.DataFrame({'x': x, 'y': y})
    df.head()

    data = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='pTempCAvg')]
    offline.plot({
        'data': data,
        'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='Temperature', type='log'))
    }, )
