from django.conf.urls import patterns, include, url
from .views import MainPageView, HobbyPageView, ArmiesList, WoundCounterCreate

urlpatterns = patterns('',

    url(r'mainpage$', MainPageView.as_view(), name='mainpage'),
    url(r'hobbypage$', HobbyPageView.as_view(), name='hobbypage'),
    url(r'armiespage$', ArmiesList.as_view(), name='armiespage'),
    url(r'^woundcounter$', WoundCounterCreate.as_view(), name='woundcounter'),

    
)
