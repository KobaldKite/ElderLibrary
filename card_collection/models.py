from django.db import models
from django.contrib.auth.models import User


CARD_RARITIES_LIST = ['common', 'rare', 'epic', 'legendary', 'unique legendary']
CARD_TYPES_LIST = ['action', 'creature', 'item', 'support']
DECK_ARCHETYPES_LIST = ['aggro', 'midrange', 'control', 'support']

CARD_RARITIES = enumerate(CARD_RARITIES_LIST, 1)
CARD_TYPES = enumerate(CARD_TYPES_LIST, 1)
DECK_ARCHETYPES = enumerate(DECK_ARCHETYPES_LIST, 1)


class GeneralEntity(models.Model):
    name = models.CharField(max_length=256, primary_key=True)

    def __str__(self):
        return self.name


class Keyword(GeneralEntity):
    pass


class Attribute(GeneralEntity):
    pass


class Race(GeneralEntity):
    pass


class Expansion(GeneralEntity):
    pass


class Card(models.Model):
    name = models.CharField(max_length=256, primary_key=True)
    image = models.ImageField(upload_to='card_collection/static/card_collection/images/cards',
                              default='card_collection/static/images/card_collection/card_placeholder.png'
                              )

    card_type = models.IntegerField(choices=CARD_TYPES)
    attributes = models.ManyToManyField(Attribute)

    rarity = models.IntegerField(choices=CARD_RARITIES)
    summon_cost = models.IntegerField(null=True, blank=True)
    soultrap_cost = models.IntegerField(null=True, blank=True)

    magicka_cost = models.IntegerField()
    attack = models.IntegerField(null=True, blank=True)
    health = models.IntegerField(null=True, blank=True)

    mechanics_text = models.TextField()
    flavor_text = models.TextField()
    keywords = models.ManyToManyField(Keyword, blank=True)
    races = models.ManyToManyField(Race, blank=True)

    is_collectible = models.BooleanField()
    expansion = models.ForeignKey(Expansion)

    def __str__(self):
        return self.name


class Collection(models.Model):
    """This represents all cards owned by all users. One big collection."""
    owner = models.ManyToManyField(User)
    card = models.ManyToManyField(Card)
    number_of_cards = models.IntegerField()


class Deck(GeneralEntity):
    id = models.AutoField(primary_key=True)
    deck_archetype = models.IntegerField(choices=DECK_ARCHETYPES)
    deck_attributes = models.ManyToManyField(Attribute)
    author = models.ManyToManyField(User)


class DeckContent(models.Model):
    deck = models.ManyToManyField(Deck)
    card = models.ManyToManyField(Card)
    number_of_cards = models.IntegerField()
