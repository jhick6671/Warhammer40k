from django.views.generic.edit import CreateView
from .models import WoundCounter

class WoundCounterCreate(CreateView):
    model = WoundCounter
    template_name = 'WH40k/Wound Counter.html'
