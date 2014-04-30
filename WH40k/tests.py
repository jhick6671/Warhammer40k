"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import random

from django.test import TestCase
from django.core.urlresolvers import resolve, reverse
from .views import MainPageView, HobbyPageView, ArmiesList
from .WoundCounter import Dice
random.seed(0)
class ToHitTest(TestCase):
    def test_ToHit(self):
        """ In this test the ToHit part of the WoundCounter is being tested. The outcome should be the number of hits
        being delivered to the defending unit."""
        # random.seed(0)
        d = Dice(20, 4, 4, 3)
        self.assertEqual(d.ToHit(),13)

class ToWoundTest(TestCase):
    def test_ToWound(self):
        """ In this test the ToWound part of the WoundCounter is being tested. The outcome should be the number of wounds
        being delivered to the defending unit."""
        # random.seed(0)
        d = Dice(20, 4, 4, 3)
        self.assertEqual(d.ToWound(),10)

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

class WoundsDealtTest(TestCase):
    def test_wound_counter(self):
        """ In this test the whole WoundCounter python script is ran. The outcome is the number of wound that"""
        # random.seed(0)
        d = Dice(20, 4, 4, 3)
        self.assertEqual(d.WoundsDealt(),4)