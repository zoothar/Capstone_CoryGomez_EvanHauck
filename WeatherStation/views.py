from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from .models import Record


def index(request):
    #models db connector
    all_records = Record.objects.all()
    t = loader.get_template('Main_Page.html')
    c = {'foo': 'bar'}
    messages.add_message(request, messages.INFO, 'Hello world.')
    return HttpResponse(t.render(c, request))


def plot(request, plot_id):
    return HttpResponse("<h2>ID for this page is:" + str(plot_id)+"</h2>" )