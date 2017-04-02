from django.http import HttpResponse
from django.shortcuts import render
from . plotting import plotGraph
from . parameters import change
column = 0
start = "2016-03-30"
end = "2016-04-30"


def index(request):
    global column,start,end
    #models db connector
    context = {
        'column': column,
        'startdate': start,
        'enddate': end,
        'change': change(column, start, end)
               }
    return render(request, 'Main_Page.html', context)


def plot(request):
    global column,start,end
    context = {
        'column': column,
        'startdate': start,
        'enddate': end,
        'plotting': plotGraph(column, start, end)
    }
    return render(request, 'Plot_Page.html', context)