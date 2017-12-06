from django.contrib import admin
from .models import Attribute, Card, CardType, Deck, DeckArchetype, DeckClass,\
    Expansion, Keyword, Race, Rarity

admin.site.register(Attribute)
admin.site.register(Card)
admin.site.register(CardType)
admin.site.register(Deck)
admin.site.register(DeckArchetype)
admin.site.register(DeckClass)
admin.site.register(Expansion)
admin.site.register(Keyword)
admin.site.register(Race)
admin.site.register(Rarity)
