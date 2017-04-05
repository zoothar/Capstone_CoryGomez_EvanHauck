import csv

from django.http import HttpResponseRedirect, StreamingHttpResponse
from django.shortcuts import render
from . plotting import plotGraph
import django
django.setup()
from WeatherStation.models import Record
#from pytz import timezone
from datetime import datetime
import csv


def index(request):
    now = datetime.now()
    end = datetime.__str__(now)
    plotName = 'plot'
    #models db connector
    context = {
        'endDate': end,
        'plots': plotName
               }
    return render(request, 'Main_Page.html', context)


def plot(request):
    column = request.POST.get('column')
    start = request.POST.get('dateField1')
    end = request.POST.get('dateField2')
    if column== None:
        column = '0'
    if start== None:
        start = "2016-03-01"
    if end== None:
        now = datetime.now()
        end = datetime.__str__(now)
    context = {
        'plotting': plotGraph(column, start, end)
    }
    return render(request, 'Plot_Page.html', context)

def downloadDbToCSV():
    filename = 'WeatherStation_EntireDb_' + datetime.now().strftime('%Y_%m_%d_') + '.csv'

    response = StreamingHttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="' + filename + '"'

    writer = csv.writer(response)
    for i in Record.objects.all():
        writer([str(i.timeStamp), str(i.recordNum), str(i.battAvg), str(i.pTempCAvg), str(i.airTCAvg), str(i.rH),
                str(i.slrkW), str(i.slrMJTot), str(i.wSMs), str(i.windDir), str(i.pARTotTot), str(i.bPMmHg),
                str(i.rainMmTot),
                str(i.pARDen)])
    return response

