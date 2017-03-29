import plotly.graph_objs as go
from plotly.graph_objs import Scatter
import pandas as pd
import plotly.offline as offline


import sqlite3

#commented out evan's personal settings and replaced with mine, evan if you want yours to work you have to uncomment your code and comment out mine...

#Evan's
conn = sqlite3.connect('/home/evan/Documents/Capstone_randomFiles/CapstoneProject/Capstone_CoryGomez_EvanHauck/db.ESRM_Sierra')

#Cory's Desktop
#conn = sqlite3.connect('/home/batman/Documents/CSUCI/Capstone/Capstone_CoryGomez_EvanHauck/db.ESRM_Sierra')

#Cory's Laptop
#conn = sqlite3.connect('/home/batman/Documents/Project/Capstone_CoryGomez_EvanHauck/db.ESRM_Sierra')

df = pd.read_sql_query('SELECT timeStamp, battAvg FROM WeatherStation_record WHERE recordNum < 15', conn)
#print(df.head()) #for testing connection

file_str = offline.plot({
                'data': [
                    Scatter(
                        x=df['timeStamp'],
                        y=df['battAvg'],
                        mode='lines',
                        name='Battery Voltages',)
                ],
                'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='Voltage', type='log'))
            }, output_type='div')
#file_loc = offline.plot({'data': [{'y': [4, 2, 3, 4]}],'layout': {'title': 'Test Plot','font': dict(size=16)}},image='png') #test example
f = open("/home/evan/Documents/test_string_file.txt","w")
#f = open("/home/batman/Documents/test_string_file.txt","w")

print(f)
f.write(file_str)