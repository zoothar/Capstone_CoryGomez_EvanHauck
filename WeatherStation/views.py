from django.http import HttpResponseRedirect
from django.shortcuts import render
from . plotting import plotGraph
from datetime import datetime


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

