from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^plot', views.plot, name='plot'),
    url(r'^download', views.downloadDbToCSV, name='download'),
    url(r'^downDate', views.queryToCSV, name='downDate')
]