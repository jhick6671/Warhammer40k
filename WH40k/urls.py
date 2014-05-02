from django.conf.urls import patterns, include, url
from .views import MainPageView, HobbyPageView, ArmiesList, WoundCounterCreate, WoundResults

urlpatterns = patterns('',

    url(r'mainpage$', MainPageView.as_view(), name='mainpage'),
    url(r'hobbypage$', HobbyPageView.as_view(), name='hobbypage'),
    url(r'armies/(?P<pk>\d+)$', ArmiesList.as_view(), name='army'),
    url(r'^woundcounter$', WoundCounterCreate.as_view(), name='woundcounter'),
    url(r'^woundcounter/results/(?P<pk>\d+)$', WoundResults.as_view()),
)
