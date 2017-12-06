from django.db import models
from django.contrib.auth.models import User


class GeneralEntity(models.Model):
    name = models.CharField(max_length=256, primary_key=True)

    def __str__(self):
        return self.name


class Keyword(GeneralEntity):
    pass


class Rarity(GeneralEntity):
    pass


class Attribute(GeneralEntity):
    pass


class CardType(GeneralEntity):
    pass


class Race(GeneralEntity):
    pass


class Expansion(GeneralEntity):
    is_actual = models.BooleanField()


class Card(models.Model):
    name = models.CharField(max_length=256, primary_key=True)
    image = models.ImageField(upload_to='card_collection/static/card_collection/images/cards',
                              default='card_collection/static/images/card_collection/card_placeholder.png'
                              )

    card_type = models.ForeignKey(CardType)
    attributes = models.ManyToManyField(Attribute)

    rarity = models.ForeignKey(Rarity)
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


class DeckClass(GeneralEntity):
    attributes = models.ManyToManyField(Attribute)


class DeckArchetype(GeneralEntity):
    pass


class Deck(GeneralEntity):
    id = models.AutoField(primary_key=True)
    deck_class = models.ForeignKey(DeckClass)
    deck_archetype = models.ForeignKey(DeckArchetype)


class DeckAuthors(models.Model):
    author = models.ManyToManyField(User)
    deck = models.ManyToManyField(Deck)


class DeckContent(models.Model):
    deck = models.ManyToManyField(Deck)
    card = models.ManyToManyField(Card)
    number_of_cards = models.IntegerField()
