from django.http import HttpResponse
from django.template import loader

def index(request):
    t = loader.get_template('Main_Page.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request))