from django.http import HttpResponse
from django.shortcuts import render
from .models import Record
from.plotting import plotGraph

def index(request):
    #models db connector
    all_records = Record.objects.all()
    context = {'all_record': all_records}
    return render(request, 'Main_Page.html', context)


def plot(request):
    context = {'plotting': plotGraph(1, "2017-02-01", "2017-02-28")}
    return render(request, 'Plot_Page.html', context)