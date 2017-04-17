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
import plotly.figure_factory as ff
from django.db.models import Max, Min, StdDev, Avg

slct = 0
sdate = datetime(2016, 3, 2)
edate = datetime(2017, 2, 3)
sdate2 = datetime(2016, 4, 4)

column = str('battAvg')

#for median,
#count = dt.count()
#dt.values_list(term, flat=True).order_by(term)[int(round(count/2))]

if slct == 0:
    dt = Record.objects.filter(timeStamp__range=(sdate, edate))
    list = [['Max batt', 'Min batt', 'stdDev batt', 'batt avg'],
            [dt.aggregate(battmax=Max(column))['battmax'], dt.aggregate(battmax=Min('battAvg'))['battmax'],
             dt.aggregate(battmax=StdDev('battAvg'))['battmax'], dt.aggregate(battmax=Avg('battAvg'))['battmax']]]
    print(list[1][1])
    table = ff.create_table(list)

    file_str = offline.plot(table)

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
