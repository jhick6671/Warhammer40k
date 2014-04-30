from django.views import generic
from .models import Army
# import WoundCounter

class MainPageView(generic.TemplateView):
    template_name = 'WebPages/MainPage.html'

class HobbyPageView(generic.TemplateView):
    template_name = 'WebPages/HobbyPage.html'

class ArmiesList(generic.ListView):
    model = Army
    template_name = 'WebPages/ArmiesPage.html'
    context_object_name = 'Armies'
