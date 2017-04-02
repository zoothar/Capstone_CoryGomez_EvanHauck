import plotly.graph_objs as go
from plotly.graph_objs import Scatter
import pandas as pd
import plotly.offline as offline
import sqlite3
import datetime

#function to be called in order to plot desired column, then return string to be embeded on webpage
def plotGraph(column_num, startDate, endDate):

    #commented out evan's personal settings and replaced with mine, evan if you want yours to work you have to uncomment your code and comment out mine...
    #Evan's
    conn = sqlite3.connect('/home/evan/Documents/Capstone_randomFiles/CapstoneProject/Capstone_CoryGomez_EvanHauck/db.ESRM_Sierra')
    #Cory's Desktop
    #conn = sqlite3.connect('/home/batman/Documents/CSUCI/Capstone/Capstone_CoryGomez_EvanHauck/db.ESRM_Sierra')
    #Cory's Laptop
    #conn = sqlite3.connect('/home/batman/Documents/Project/Capstone_CoryGomez_EvanHauck/db.ESRM_Sierra')

    # adds time to date
    sDate = startDate + ' 00:00:00'
    eDate = endDate + ' 23:59:59'

    # functions as a switch statement to generate the string to be embeded in the webpage
    if column_num == 0:
        qr = pd.read_sql_query("SELECT timeStamp, battAvg FROM WeatherStation_record WHERE timeStamp BETWEEN '" +
                           sDate + "' AND '" + eDate + "'", conn)
        file_str = offline.plot({
                        'data': [Scatter(x=qr['timeStamp'],y=qr['battAvg'],mode='lines',name='Battery Voltages', )],
                        'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='Voltage', type='log'))
                   }, output_type='div')
    elif column_num == 1:
        qr = pd.read_sql_query("SELECT timeStamp, pTempCAvg FROM WeatherStation_record WHERE timeStamp BETWEEN '" +
                               sDate + "' AND '" + eDate + "'", conn)
        file_str = offline.plot({
                        'data': [Scatter(x=qr['timeStamp'], y=qr['pTempCAvg'], mode='lines', name='Temperature', )],
                        'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='Temperature', type='log'))
                    }, output_type='div')
    elif column_num == 2:
        qr = pd.read_sql_query("SELECT timeStamp, airTCAvg FROM WeatherStation_record WHERE timeStamp BETWEEN '" +
                               sDate + "' AND '" + eDate + "'", conn)
        file_str = offline.plot({
                        'data': [Scatter(x=qr['timeStamp'], y=qr['airTCAvg'], mode='lines', name='Temperature', )],
                        'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='Temperature', type='log'))
                    }, output_type='div')
    elif column_num == 3:
        qr = pd.read_sql_query("SELECT timeStamp, rH FROM WeatherStation_record WHERE timeStamp BETWEEN '" +
                               sDate + "' AND '" + eDate + "'", conn)
        file_str = offline.plot({
                        'data': [Scatter(x=qr['timeStamp'], y=qr['rH'], mode='lines', name='rH', )],
                        'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='rH', type='log'))
                    }, output_type='div')
    elif column_num == 4:
        qr = pd.read_sql_query("SELECT timeStamp, slrkW FROM WeatherStation_record WHERE timeStamp BETWEEN '" +
                               sDate + "' AND '" + eDate + "'", conn)
        file_str = offline.plot({
                        'data': [Scatter(x=qr['timeStamp'], y=qr['slrkW'], mode='lines', name='slrkW', )],
                        'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='slrkW', type='log'))
                    }, output_type='div')
    elif column_num == 5:
        qr = pd.read_sql_query("SELECT timeStamp, slrMJTot FROM WeatherStation_record WHERE timeStamp BETWEEN '" +
                               sDate + "' AND '" + eDate + "'", conn)
        file_str = offline.plot({
                        'data': [Scatter(x=qr['timeStamp'], y=qr['slrMJTot'], mode='lines', name='slrMJTot', )],
                        'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='slrMJTot', type='log'))
                    }, output_type='div')
    elif column_num == 6:
        qr = pd.read_sql_query("SELECT timeStamp, wSMs FROM WeatherStation_record WHERE timeStamp BETWEEN '" +
                               sDate + "' AND '" + eDate + "'", conn)
        file_str = offline.plot({
                        'data': [Scatter(x=qr['timeStamp'], y=qr['wSMs'], mode='lines', name='wSMs', )],
                        'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='wSMs', type='log'))
                    }, output_type='div')
    elif column_num == 7:
        qr = pd.read_sql_query("SELECT timeStamp, windDir FROM WeatherStation_record WHERE timeStamp BETWEEN '" +
                               sDate + "' AND '" + eDate + "'", conn)
        file_str = offline.plot({
                        'data': [Scatter(x=qr['timeStamp'], y=qr['windDir'], mode='markers', name='windDir', )],
                        'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='Wind Direction (degrees)', type='log'))
                    }, output_type='div')
    elif column_num == 8:
        qr = pd.read_sql_query("SELECT timeStamp, pARTotTot FROM WeatherStation_record WHERE timeStamp BETWEEN '" +
                               sDate + "' AND '" + eDate + "'", conn)
        file_str = offline.plot({
                        'data': [Scatter(x=qr['timeStamp'], y=qr['pARTotTot'], mode='lines', name='pARTotTot', )],
                        'layout': go.Layout(xaxis=go.XAxis(title='Date'),yaxis=go.YAxis(title='pARTotTot', type='log'))
                    }, output_type='div')
    elif column_num == 9:
        qr = pd.read_sql_query("SELECT timeStamp, bPMmHg FROM WeatherStation_record WHERE timeStamp BETWEEN '" +
                               sDate + "' AND '" + eDate + "'", conn)
        file_str = offline.plot({
                        'data': [Scatter(x=qr['timeStamp'], y=qr['bPMmHg'], mode='lines', name='Pressure', )],
                        'layout': go.Layout(xaxis=go.XAxis(title='Date'),yaxis=go.YAxis(title='Barometric Pressure (mmHg)', type='log'))
        }, output_type='div')
    elif column_num == 10:
        qr = pd.read_sql_query("SELECT timeStamp, rainMmTot FROM WeatherStation_record WHERE timeStamp BETWEEN '" +
                               sDate + "' AND '" + eDate + "'", conn)
        file_str = offline.plot({
                        'data': [Scatter(x=qr['timeStamp'], y=qr['rainMmTot'], mode='lines', name='Rainfall', )],
                        'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='Rainfall (mm)', type='log'))
                    }, output_type='div')
    elif column_num == 11:
        qr = pd.read_sql_query("SELECT timeStamp, pARDen FROM WeatherStation_record WHERE timeStamp BETWEEN '" +
                               sDate + "' AND '" + eDate + "'", conn)
        file_str = offline.plot({
                        'data': [Scatter(x=qr['timeStamp'], y=qr['pARDen'], mode='lines', name='pARDen', )],
                        'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='pARDen', type='log'))
                    }, output_type='div')

    f = open("/home/evan/Documents/test_string_file.txt","w")
    #f = open("/home/batman/Documents/test_string_file.txt","w")

    #TODO: delete after testing
    print(f)
    f.write(file_str)

    #returns string to be embeded
    return file_str


#for downloading csv file between two dates with all columns
def queryToCSV(startDate, endDate):

    #adds time to date
    sDate = startDate + ' 00:00:00'
    eDate = endDate + ' 23:59:59'
    # Evan's
    conn = sqlite3.connect(
        '/home/evan/Documents/Capstone_randomFiles/CapstoneProject/Capstone_CoryGomez_EvanHauck/db.ESRM_Sierra')
    # Cory's Desktop
    # conn = sqlite3.connect('/home/batman/Documents/CSUCI/Capstone/Capstone_CoryGomez_EvanHauck/db.ESRM_Sierra')
    # Cory's Laptop
    # conn = sqlite3.connect('/home/batman/Documents/Project/Capstone_CoryGomez_EvanHauck/db.ESRM_Sierra')

    #query database
    qr = pd.read_sql_query("SELECT * FROM WeatherStation_record WHERE timeStamp BETWEEN '" +
                           sDate + "' AND '" + eDate + "'", conn)
    qr.to_csv('WeatherStation_query_' + datetime.datetime.now().strftime('%Y_%m_%d__%H_%M') + '.csv')

def downloadDbToCSV():

    # Evan's
    conn = sqlite3.connect(
        '/home/evan/Documents/Capstone_randomFiles/CapstoneProject/Capstone_CoryGomez_EvanHauck/db.ESRM_Sierra')
    # Cory's Desktop
    # conn = sqlite3.connect('/home/batman/Documents/CSUCI/Capstone/Capstone_CoryGomez_EvanHauck/db.ESRM_Sierra')
    # Cory's Laptop
    # conn = sqlite3.connect('/home/batman/Documents/Project/Capstone_CoryGomez_EvanHauck/db.ESRM_Sierra')

    tbl = pd.read_sql_query("SELECT * FROM WeatherStation_record", conn)
    tbl.to_csv('WeatherStation_' + datetime.datetime.now().strftime('%Y_%m_%d') + '.csv')