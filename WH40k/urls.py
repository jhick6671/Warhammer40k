from django.conf.urls import patterns, include, url
from .views import WoundCounterCreate

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc2.views.home', name='home'),
    # url(r'^gisc2/', include('gisc2.foo.urls')),
     url(r'^woundcounter$', WoundCounterCreate.as_view(), name='woundcounter),
)