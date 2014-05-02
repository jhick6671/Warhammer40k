"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from .views import MainPageView, HobbyPageView, ArmiesList

class UrlTest(TestCase):
    def test_MainPage_url(self):
        MainPage = resolve(reverse('WebPages:MainPage'))
        return self.assertEqual(MainPage.func.__name__,
                                MainPageView.__name__)

    def test_HobbyPage_url(self):
        HobbyPage = resolve(reverse('WebPages:HobbyPage'))
        return self.assertEqual(HobbyPage.func.__name__,
                                HobbyPageView.__name__)

    def test_ArmiesPage_url(self):
        ArmiesPage = resolve(reverse('WebPages:ArmiesPage'))
        return self.assertEqual(ArmiesPage.func.__name__,
                                ArmiesList.__name__)

