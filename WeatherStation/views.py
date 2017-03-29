from django.http import HttpResponse
from django.shortcuts import render
from .models import Record


def index(request):
    #models db connector
    all_records = Record.objects.all()
    context = {'all_record': all_records}
    return render(request, 'Main_Page.html', context)


def plot(request):
    return render(request, 'temporary.html')