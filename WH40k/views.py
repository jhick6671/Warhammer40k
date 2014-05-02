from django.views import generic
from .models import Army
# import WoundCounter

class MainPageView(generic.TemplateView):
    template_name = 'WebPages/MainPage.html'

    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        armies = Army.objects.all()
        for army in armies:
            army.template_height = int(army.symbols.height / 100.0)
            army.template_width = int(army.symbols.width / 50.0)
            if army.template_height <= army.template_width:
                army.template_height = army.symbols.height/army.template_width
                army.template_width = army.symbols.width/army.template_width
            else:
                army.template_height = army.symbols.height/army.template_height
                army.template_width = army.symbols.width/army.template_height
        context['armies'] = armies
        return context


class HobbyPageView(generic.TemplateView):
    template_name = 'WebPages/HobbyPage.html'

class ArmiesList(generic.DetailView):
    model = Army
    template_name = 'WebPages/ArmiesPage.html'
    context_object_name = 'Armies'
