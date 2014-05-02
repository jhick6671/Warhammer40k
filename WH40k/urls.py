from django.conf.urls import patterns, include, url
from .views import MainPageView, HobbyPageView, ArmiesList

urlpatterns = patterns('',

    url(r'^$', MainPageView.as_view(), name='mainpage'),
    url(r'hobbypage$', HobbyPageView.as_view(), name='hobbypage'),
    url(r'armies/(?P<pk>\d+)$', ArmiesList.as_view(), name='army'),
)
