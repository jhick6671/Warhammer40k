from django.views.generic.edit import CreateView
from django.views import generic
from .models import WoundCounter, Army

class WoundCounterCreate(CreateView):
    model = WoundCounter
    template_name = 'WH40k/WoundCounter.html'

class MainPageView(generic.TemplateView):
    template_name = 'WebPages/MainPage.html'

class HobbyPageView(generic.TemplateView):
    template_name = 'WebPages/HobbyPage.html'

class ArmiesList(generic.ListView):
    model = Army
    template_name = 'WebPages/ArmiesPage.html'
    context_object_name = 'Armies'
