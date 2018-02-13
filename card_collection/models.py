from django.db import models
from django.contrib.auth.models import User


CARD_RARITIES_LIST = ['common', 'rare', 'epic', 'legendary', 'unique legendary']
CARD_TYPES_LIST = ['action', 'creature', 'item', 'support']
DECK_ARCHETYPES_LIST = ['aggro', 'midrange', 'control', 'hybrid']

CARD_RARITIES = enumerate(CARD_RARITIES_LIST, 0)
CARD_TYPES = enumerate(CARD_TYPES_LIST, 0)
DECK_ARCHETYPES = enumerate(DECK_ARCHETYPES_LIST, 0)


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
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='card_collection/images/cards',
                              default='card_collection/images/card_placeholder.png'
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

    def rarity_string(self):
        return CARD_RARITIES_LIST[self.rarity]

    def type_string(self):
        return CARD_TYPES_LIST[self.card_type]


class Collection(models.Model):
    """For now, only one copy of each card is available in a collection"""
    owner = models.ManyToManyField(User)
    cards = models.ManyToManyField(Card)


class Deck(models.Model):
    """For now, only one copy of each card is available in a deck"""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    deck_archetype = models.IntegerField(choices=DECK_ARCHETYPES)
    deck_attributes = models.ManyToManyField(Attribute)
    author = models.ForeignKey(User)
    cards = models.ManyToManyField(Card)

    def __str__(self):
        return self.name

    def archerype_string(self):
        return DECK_ARCHETYPES_LIST[self.deck_archetype]
