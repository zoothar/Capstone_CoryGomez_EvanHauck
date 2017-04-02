from django.http import HttpResponse
from django.shortcuts import render
from .models import Record
from.plotting import plotGraph

column = 0
start = "2016-03-30"
end = "2016-04-30"

def index(request):
    #models db connector
    context = {
        'column': column,
        'startdate': start,
        'enddate': end
               }
    return render(request, 'Main_Page.html', context)


def plot(request):
    column= 0
    start= "2016-03-30"
    end= "2016-04-30"
    context = {
        'column': column,
        'startdate': start,
        'enddate': end,
        'plotting': plotGraph(column, start, end)
    }
    return render(request, 'Plot_Page.html', context)