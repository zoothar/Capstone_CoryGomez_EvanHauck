import csv

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from . plotting import plotGraph
import django
django.setup()
from WeatherStation.models import Record
from pytz import timezone
from datetime import datetime
import csv
import warnings
from . import jsonParse

pst = timezone('UTC')
#View for the main page, the context are connection points between python and the html for enddate
# and the plot url in the iframe
def index(request):
    now = datetime.now()
    end = datetime.__str__(now)
    plotName = 'plot'
    #models db connector
    context = {
        'endDate': end,
        #'query': jsonParse.queryWeatherStation(),
        'plots': plotName
               }
    return render(request, 'Main_Page.html', context)

# view for the plot page to show the generated graph in the iframe of the main page, this has a default value for
# battery average from the first data set to the last the context creates the whole template dynamically and is called
# in the template page as {{ plotting }}
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
        'start': start,
        'end': end,
        'plotting': plotGraph(column, start, end)
    }
    return render(request, 'Plot_Page.html', context)

def downloadDbToCSV(request):

    filename = 'WeatherStation_EntireDb_' + datetime.now().strftime('%Y_%m_%d_') + '.csv'

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="' + filename + '"'

    writer = csv.writer(response)
    writer.writerow(['timeStamp', 'recordNum', 'battAvg', 'pTempCAvg', 'rH', 'slrkW', 'slrMJTot', 'wSMs', 'pARTotTot',
                     'bPMmHg','rainMmHg','pARDen'])
    for i in Record.objects.all():
        writer.writerow([str(i.timeStamp), str(i.recordNum), str(i.battAvg), str(i.pTempCAvg), str(i.airTCAvg), str(i.rH),
                str(i.slrkW), str(i.slrMJTot), str(i.wSMs), str(i.windDir), str(i.pARTotTot), str(i.bPMmHg),
                str(i.rainMmTot), str(i.pARDen)])
        warnings.filterwarnings(
            'error', r"DateTimeField .* received a naive datetime",
            RuntimeWarning, r'django\.db\.models\.fields',
        )
    return response

# for downloading csv file between two dates with all columns
def queryToCSV(request):
    startDate = request.POST.get('startDate')
    endDate = request.POST.get('endDate')

    filename ='WeatherStation_' + datetime.now().strftime('%Y_%m_%d__%H_%M') + '.csv'

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="' + filename + '"'

    writer = csv.writer(response)
    writer.writerow(['timeStamp', 'recordNum', 'battAvg', 'pTempCAvg', 'rH', 'slrkW', 'slrMJTot', 'wSMs', 'pARTotTot',
                     'bPMmHg', 'rainMmHg', 'pARDen'])
    for i in Record.objects.filter(timeStamp__range=(startDate, endDate)):
        writer.writerow([str(i.timeStamp), str(i.recordNum), str(i.battAvg), str(i.pTempCAvg), str(i.airTCAvg), str(i.rH),
                str(i.slrkW), str(i.slrMJTot), str(i.wSMs),str(i.windDir),str(i.pARTotTot),str(i.bPMmHg),str(i.rainMmTot),
                str(i.pARDen)])
    return response

