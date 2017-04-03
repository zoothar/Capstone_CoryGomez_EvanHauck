from django.http import HttpResponseRedirect
from django.shortcuts import render
from . plotting import plotGraph
from datetime import datetime

def index(request):
    now = datetime.now()
    end = datetime.__str__(now)
    #models db connector
    context = {
        'enddate': end,
               }
    return render(request, 'Main_Page.html', context)


def plot(request):
    column = 0
    start = "2016-03-01"
    now = datetime.now()
    end = datetime.__str__(now)
    context = {
        'plotting': plotGraph(column, start, end)
    }
    return render(request, 'Plot_Page.html', context)

def submit(request):
    column = request.POST.get('column')
    start = request.POST.get('dateField1')
    end = request.POST.get('dateField2')
    #str = column + start + end
    #print(str)
    context = {
        'plotting': plotGraph(column, start, end)
    }
    #str = '<html><body>' + plotGraph(plotGraph(column, start, end)) + '</body></html'
    return HttpResponseRedirect('/main/submit/',context)
