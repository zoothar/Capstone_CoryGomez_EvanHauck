from django.http import HttpResponse
from django.template import loader
from django.contrib import messages



def index(request):
    t = loader.get_template('Main_Page.html')
    c = {'foo': 'bar'}
    messages.add_message(request, messages.INFO, 'Hello world.')
    return HttpResponse(t.render(c, request))


def plot(request):
    t = loader.get_template('Plot.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))