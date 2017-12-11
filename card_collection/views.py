from django.views.generic import DetailView, ListView, TemplateView
from .models import Card


class CardDetails(DetailView):
    model = Card
    template_name = 'card_collection/card_details.html'
    context_object_name = 'card'


class CardList(ListView):
    model = Card
    template_name = 'card_collection/card_list.html'
    context_object_name = 'cards_list'


class Index(TemplateView):
    template_name = 'card_collection/index.html'
