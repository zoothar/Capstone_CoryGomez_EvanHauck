# used code from http://mitchfournier.com/2011/10/11/how-to-import-a-csv-or-tsv-file-into-a-django-model/ to import csv file

# Full path and name to your csv file
csv_filepathname="/home/evan/Documents/Capstone_randomFiles/weatherData.csv"
# Full path to your django project directory
your_djangoproject_home="/home/evan/Documents/Capstone_randomFiles/CapstoneProject/Capstone_CoryGomez_EvanHauck"

import django
django.setup()

import sys,os
sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from WeatherStation.models import Record
from datetime import datetime

import csv, pytz
from pytz import timezone

dataReader = csv.reader(open(csv_filepathname), delimiter=',')

pst = timezone('US/Pacific')

all_entries = Record.objects.all()

for row in dataReader:
    record = Record()

    #code to fix improper datetime formatting from CSV
    dt, tm = row[0].split(" ")
    m, d, y = dt.split("/")
    if( int(m) < 10):
        m = str(0) + m
    if (int(d) < 10):
        d = str(0) + d
    y = str(20) + y
    date = y + '-' + m + '-' + d #for checking reformatting
    h, mn = tm.split(":")
    if (int(h) < 10):
        h = str(0) + h
    t = h + ':' + mn #for checking reformatting
    dt_obj = date + ' ' + t #for checking reformatting
    print(dt_obj) #for testing import and format
    record.timeStamp = pst.localize(datetime(int(y), int(m), int(d), int(h), int(mn)))
    record.recordNum = row[1]
    record.battAvg = row[2]
    record.pTempCAvg = row[3]
    record.airTCAvg = row[4]
    record.rH = row[5]
    record.slrkW = row[6]
    record.slrMJTot = row[7]
    record.wSMs = row[8]
    record.windDir = row[9]
    record.pARDen = row[10]
    record.pARTotTot = row[11]
    record.bPMmHg = row[12]
    record.rainMmTot = row[13]
    record.save()