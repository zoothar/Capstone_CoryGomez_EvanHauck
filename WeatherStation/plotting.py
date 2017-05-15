import plotly.graph_objs as go
import pandas as pd
import plotly.offline as offline
#from plotly.grid_objs import Column, Grid
import plotly.figure_factory as ff
import django
django.setup()
from WeatherStation.models import Record
from pytz import timezone
import pytz
from django.db.models import Max, Min, StdDev, Avg
from datetime import datetime
from datetime import timedelta

pst = timezone('US/Pacific')

#function to be called in order to plot desired column, then return string to be embeded on webpage
def plotGraph( column_num, startDate, endDate):
    file_str = ''
    #empty lists that are required to be filled in order for the Plotly API to read the data correctly.
    x = []
    y = []



    #filling each list with the desired data
    if column_num == '0':
        for i in Record.objects.only("timeStamp", "battAvg").filter(timeStamp__range=(startDate, endDate)):
            x.append(i.timeStamp)
            y.append(i.battAvg)

        #prepping and then executing the Plotly API in order generate the graphs,offline used to allow for embedding the graphs
        df = pd.DataFrame({'x': x, 'y': y})
        df.head()

        data = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='Battery Voltages')]
        file_str =offline.plot({
            'data': data,
            'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='Voltage', type='log'))
        }, output_type='div')
    elif column_num == '1':
        # filling each list with the desired data
        for i in Record.objects.only("timeStamp", "pTempCAvg").filter(timeStamp__range=(startDate, endDate)):
            x.append(i.timeStamp)
            y.append(i.pTempCAvg)

        df = pd.DataFrame({'x': x, 'y': y})
        df.head()

        # prepping and then executing the Plotly API in order generate the graphs,offline used to allow for embedding the graphs
        data = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='P_Temp')]
        file_str =offline.plot({
            'data': data,
            'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='Temperature (C)', type='log'))
        }, output_type='div')
    elif column_num == '2':
        # filling each list with the desired data
        for i in Record.objects.only("timeStamp", "airTCAvg").filter(timeStamp__range=(startDate, endDate)):
            x.append(i.timeStamp)
            y.append(i.airTCAvg)

        df = pd.DataFrame({'x': x, 'y': y})
        df.head()

        # prepping and then executing the Plotly API in order generate the graphs,offline used to allow for embedding the graphs
        data = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='Air_Temp')]
        file_str =offline.plot({
            'data': data,
            'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='Temperature (C)', type='log'))
        }, output_type='div')
    elif column_num == '3':
        # filling each list with the desired data
        for i in Record.objects.only("timeStamp", "rH").filter(timeStamp__range=(startDate, endDate)):
            x.append(i.timeStamp)
            y.append(i.rH)

        df = pd.DataFrame({'x': x, 'y': y})
        df.head()

        # prepping and then executing the Plotly API in order generate the graphs,offline used to allow for embedding the graphs
        data = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='Relative Humidity')]
        file_str =offline.plot({
            'data': data,
            'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='Relative Humidity', type='log'))
        }, output_type='div')
    elif column_num == '4':
        # filling each list with the desired data
        for i in Record.objects.only("timeStamp", "slrkW").filter(timeStamp__range=(startDate, endDate)):
            x.append(i.timeStamp)
            y.append(i.slrkW)

        df = pd.DataFrame({'x': x, 'y': y})
        df.head()

        # prepping and then executing the Plotly API in order generate the graphs,offline used to allow for embedding the graphs
        data = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='slrkW')]
        file_str =offline.plot({
            'data': data,
            'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='slrkW', type='log'))
        }, output_type='div')
    elif column_num == '5':
        # filling each list with the desired data
        for i in Record.objects.only("timeStamp", "slrMJTot").filter(timeStamp__range=(startDate, endDate)):
            x.append(i.timeStamp)
            y.append(i.slrMJTot)

        df = pd.DataFrame({'x': x, 'y': y})
        df.head()

        # prepping and then executing the Plotly API in order generate the graphs,offline used to allow for embedding the graphs
        data = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='slrMJTot')]
        file_str =offline.plot({
            'data': data,
            'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='slrMJTot', type='log'))
        }, output_type='div')
    elif column_num == '6':
        # filling each list with the desired data
        for i in Record.objects.only("timeStamp", "wSMs").filter(timeStamp__range=(startDate, endDate)):
            x.append(i.timeStamp)
            y.append(i.wSMs)

        df = pd.DataFrame({'x': x, 'y': y})
        df.head()

        # prepping and then executing the Plotly API in order generate the graphs,offline used to allow for embedding the graphs
        data = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='Wind Speed')]
        file_str =offline.plot({
            'data': data,
            'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='Wind Speed (m/s)', type='log'))
        }, output_type='div')
    elif column_num == '7':
        # filling each list with the desired data
        for i in Record.objects.only("timeStamp", "windDir").filter(timeStamp__range=(startDate, endDate)):
            x.append(i.timeStamp)
            y.append(i.windDir)

        df = pd.DataFrame({'x': x, 'y': y})
        df.head()

        # prepping and then executing the Plotly API in order generate the graphs,offline used to allow for embedding the graphs
        data = [go.Scatter(x=df['x'], y=df['y'], mode='markers', name='direction')]
        file_str =offline.plot({
            'data': data,
            'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='Wind Direction (Degrees)', type='log'))
        }, output_type='div')
    elif column_num == '8':
        # filling each list with the desired data
        for i in Record.objects.only("timeStamp", "pARTotTot").filter(timeStamp__range=(startDate, endDate)):
            x.append(i.timeStamp)
            y.append(i.pARTotTot)

        df = pd.DataFrame({'x': x, 'y': y})
        df.head()

        # prepping and then executing the Plotly API in order generate the graphs,offline used to allow for embedding the graphs
        data = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='pARTotTot')]
        file_str =offline.plot({
            'data': data,
            'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='pARTotTot', type='log'))
        }, output_type='div')
    elif column_num == '9':
        # filling each list with the desired data
        for i in Record.objects.only("timeStamp", "bPMmHg").filter(timeStamp__range=(startDate, endDate)):
            x.append(i.timeStamp)
            y.append(i.bPMmHg)

        df = pd.DataFrame({'x': x, 'y': y})
        df.head()

        # prepping and then executing the Plotly API in order generate the graphs,offline used to allow for embedding the graphs
        data = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='Pressure')]
        file_str =offline.plot({
            'data': data,
            'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='Barometric pressure (mmHg)', type='log'))
        }, output_type='div')
    elif column_num == '10':
        # filling each list with the desired data
        for i in Record.objects.only("timeStamp", "rainMmTot").filter(timeStamp__range=(startDate, endDate)):
            x.append(i.timeStamp)
            y.append(i.rainMmTot)

        df = pd.DataFrame({'x': x, 'y': y})
        df.head()

        # prepping and then executing the Plotly API in order generate the graphs,offline used to allow for embedding the graphs
        data = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='Rainfall')]
        file_str =offline.plot({
            'data': data,
            'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='Rainfall (mm)', type='log'))
        }, output_type='div')
    elif column_num == '11':
        # filling each list with the desired data
        for i in Record.objects.only("timeStamp", "pARDen").filter(timeStamp__range=(startDate, endDate)):
            x.append(i.timeStamp)
            y.append(i.pARDen)

        df = pd.DataFrame({'x': x, 'y': y})
        df.head()

        # prepping and then executing the Plotly API in order generate the graphs,offline used to allow for embedding the graphs
        data = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='pARDen')]
        file_str=offline.plot({
            'data': data,
            'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='pARDen', type='log'))
        }, output_type='div')


    #returns string to be embeded
    return file_str

# using the Plotly API to display basic statistical data based on which data is being viewed
def plotTable(column_num, startDate, endDate):
    file_str = ''
    selct = 'battAvg'

    #determines which data is being used, selected the select statement for the query accordingly
    if column_num == '0':
        selct = 'battAvg'
    elif column_num == '1':
        selct = 'pTempCAvg'
    elif column_num == '2':
        selct = 'airTCAvg'
    elif column_num == '3':
        selct = 'rH'
    elif column_num == '4':
        selct = 'slrkW'
    elif column_num == '5':
        selct = 'slrMJTot'
    elif column_num == '6':
        selct = 'wSMs'
    elif column_num == '7':
        selct = 'windDir'
    elif column_num == '8':
        selct = 'pARTotTot'
    elif column_num == '9':
        selct = 'bPMmHg'
    elif column_num == '10':
        selct = 'rainMmTot'
    elif column_num == '11':
        selct = 'pARDen'

    # grabs the data from the database and aggregates it based on the data viewed (and pulls only the desired numernic values rather than the dictionary result
    dt = Record.objects.filter(timeStamp__range=(startDate, endDate))
    list = [['Max', 'Min', 'Standard Deviation', 'Average'],
            [dt.aggregate(val=Max(selct))['val'], dt.aggregate(val=Min(selct))['val'],
             dt.aggregate(val=StdDev(selct))['val'], dt.aggregate(val=Avg(selct))['val']]]

    #creates the table with the data
    table = ff.create_table(list)
    #plots the table offline to be embedded in the web page
    file_str = offline.plot(table, output_type='div')
    return file_str


# def plotRecent():
#     file_str = ''
#     dt = Record.objects.latest('timeStamp')
#     list = [['Time Stamp', 'Record Number', 'Battery Voltage', 'P Temp', 'Air Temp (C)', 'RH', 'slrkW', 'slr MJ Total',
#              'Wind Speed (m/s)', 'Wind Direction', 'pArtTot Total','Baro Pres. (mmHg)', 'Rainfall (mm)', 'pARDen'],
#             [dt.timeStamp, dt.recordNum, dt.battAvg, dt.pTempCAvg, dt.airTCAvg, dt.rH , dt.slrkW, dt.slrMJTot, dt.wSMs,
#             dt.windDir, dt.pARTotTot, dt.bPMmHg, dt.rainMmTot, dt.pARDen]]
#     table = ff.create_table(list)
#
#     file_str = offline.plot(table, output_type='div')
#
#     return file_str

#basic get function with parsing to get the time stamp data and adjust the time based on daylight savings (for user viewing in recent weather data)
def getTimeStamp():
    dt = Record.objects.latest('timeStamp')
    stamp = dt.timeStamp
    stampstr = str(dt.timeStamp)

    ct, tm = stampstr.split(" ")
    h, mn, s = tm.split(":")

    now = datetime.now(tz=pytz.utc)
    now = now.astimezone(pst)

    if int(h) < now.hour:
        stamp = stamp + timedelta(hours=1)
    return stamp.strftime("%A %B %d, %Y %I:%M%p")

#basic get function for recent air temp
def getAirTemp():
    dt = Record.objects.latest('timeStamp')
    return str(dt.airTCAvg)

#basic get function for recent wind speed
def getWindSpeed():
    dt = Record.objects.latest('timeStamp')
    return str(dt.wSMs)

#basic get function for recent wind direction, also adding compass values based on the data found
def getWindDirection():
    dt = Record.objects.latest('timeStamp')
    compass = '' #following if/elseif statements designate a direction on the compass rose corresponding to
                 # the value
    if dt.windDir == 0 or dt.windDir == 360:
        compass = 'N'
    elif dt.windDir > 0 and dt.windDir < 90:
        compass = 'NE'
    elif dt.windDir == 90:
        compass = 'E'
    elif dt.windDir > 90 and dt.windDir < 180:
        compass = 'SE'
    elif dt.windDir ==180:
        compass = 'S'
    elif dt.windDir > 180 and dt.windDir < 270:
        compass = 'SW'
    elif dt.windDir == 270:
        compass = 'W'
    elif dt.windDir > 270 and dt.windDir < 360:
        compass = 'NW'
    return str(dt.windDir) + " " + compass

#basic get function for recent battery voltage
def getBattVolt():
    dt = Record.objects.latest('timeStamp')
    return str(dt.battAvg)

#basic get function for recent barometric pressure
def getBaroPres():
    dt = Record.objects.latest('timeStamp')
    return str(dt.bPMmHg)

#basic get function for recent relative humidity
def getRelativeHum():
    dt = Record.objects.latest('timeStamp')
    return str(dt.rH)

#basic get function for recent rainfall
def getRainFall():
    dt = Record.objects.latest('timeStamp')
    return str(dt.rainMmTot)