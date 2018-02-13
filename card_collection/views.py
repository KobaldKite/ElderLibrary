from django.views.generic import DetailView, ListView, TemplateView
from .models import Card, Deck


class CardDetails(DetailView):
    model = Card
    template_name = 'card_collection/card_details.html'
    context_object_name = 'card'


class CardList(ListView):
    model = Card
    template_name = 'card_collection/card_list.html'
    context_object_name = 'cards_list'
    paginate_by = 6


class DeckDetails(DetailView):
    model = Deck
    template_name = 'card_collection/deck_details.html'
    context_object_name = 'deck'


class DeckList(ListView):
    model = Deck
    template_name = 'card_collection/deck_list.html'
    context_object_name = 'decks_list'
    paginate_by = 6


class EditDeck(ListView):
    model = Card

    def get_user(self, request):
        self.current_user = request.user

    def get_queryset(self):  # TODO: add all possible filters
        return Card.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deck'] = Deck.objects.all() #filter(Author=current_user)
        # TODO: change it to a single deck
        return context


class Index(TemplateView):
    template_name = 'card_collection/index.html'
