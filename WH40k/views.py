from django.views.generic.edit import CreateView
from django.views import generic
from .models import WoundCounter, Army
from .WoundCounter import Dice

class WoundCounterCreate(CreateView):
    model = WoundCounter
    template_name = 'WH40k/WoundCounter.html'

class WoundResults(generic.TemplateView):
    model = WoundCounter
    template_name = 'WH40k/WoundResults.html'

    def get_context_data(self, **kwargs):
        context = super(WoundResults, self).get_context_data(**kwargs)
        wound = WoundCounter.objects.filter(pk=self.kwargs['pk'])[0]

        def statistics(dice, hit, wound, save, runtime=100):
            """ In this section we want the program to run X amount of times and produce statistics from the results. To keep it
            simple we just want to see the maximum, minimum, and average for hit, wound and saved."""
            count = 0
            results = []
            while count < runtime:
                d = Dice(dice, hit, wound, save)
                results.append((d.ToHit(), d.ToWound(), d.WoundsDealt()))
                count += 1

            p = ["The maximum number of hits:" + str(max([r[0] for r in results])),
                "The minimum number of hits:" + str(min([r[0] for r in results])),
                "The average number of hits:" + str(sum([r[0] for r in results])/len([r[0] for r in results])),
                "The maximum number of wounds:" + str(max([r[1] for r in results])),
                "The minimum number of wounds:" + str(min([r[1] for r in results])),
                "The average number of wounds:" + str(sum([r[1] for r in results])/len([r[1] for r in results])),
                "The maximum number of wounds dealt:" + str(max([r[2] for r in results])),
                "The minimum number of wounds dealt:" + str(min([r[2] for r in results])),
                "The average number of wounds dealt:" + str(sum([r[2] for r in results])/len([r[2] for r in results]))]

            return p

        context['results'] = statistics(int(wound.dice),
                                        int(wound.hit),
                                        int(wound.wound),
                                        int(wound.saves))
        return context



class MainPageView(generic.TemplateView):
    template_name = 'WebPages/MainPage.html'

class HobbyPageView(generic.TemplateView):
    template_name = 'WebPages/HobbyPage.html'

class ArmiesList(generic.ListView):
    model = Army
    template_name = 'WebPages/ArmiesPage.html'
    context_object_name = 'Armies'
