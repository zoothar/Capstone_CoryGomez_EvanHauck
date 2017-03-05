from django.http import HttpResponse
from django.template import loader

def index(request):
    t = loader.get_template('WeatherStation/Main_Page.html')
    c = {'foo': 'bar'}
    return HttpResponse(t.render(c, request), content_type='application/xhtml+xml')