import factory
from factory import fuzzy
from . import models
from .models import CARD_RARITIES_LIST, CARD_TYPES_LIST

INDEX_SHIFT = 1
GENERAL_RANGE = [0, 10]
CARD_RARITY_RANGE = [INDEX_SHIFT, len(CARD_RARITIES_LIST) + INDEX_SHIFT]

CARD_ATTRIBUTES = ['agility', 'endurance', 'intelligence',
                   'strength', 'willpower', 'neutral']

ACTION = CARD_TYPES_LIST.index('action') + INDEX_SHIFT
CREATURE = CARD_TYPES_LIST.index('creature') + INDEX_SHIFT
ITEM = CARD_TYPES_LIST.index('item') + INDEX_SHIFT


class AttributeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Attribute

    name = factory.Iterator(CARD_ATTRIBUTES)


class ExpansionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Expansion

    name = fuzzy.FuzzyText(length=6, prefix='Expansion_')


class KeywordFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Keyword

    name = factory.Faker('word')


class RaceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Race

    name = factory.Faker('word')


class CardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Card

    name = factory.Faker('word')
    image = factory.django.ImageField()
    attributes = models.Attribute.objects.all().first()
    rarity = fuzzy.FuzzyInteger(*CARD_RARITY_RANGE)
    summon_cost = fuzzy.FuzzyInteger(*GENERAL_RANGE)
    soultrap_cost = fuzzy.FuzzyInteger(*GENERAL_RANGE)
    magicka_cost = fuzzy.FuzzyInteger(*GENERAL_RANGE)
    mechanics_text = factory.Faker('word')
    flavor_text = factory.Faker('sentence')
    is_collectible = fuzzy.FuzzyChoice([True, False])
    expansion = factory.Iterator(models.Expansion.objects.all())


class CreatureCardFactory(CardFactory):
    card_type = CREATURE
    name = factory.Faker('job')

    attack = fuzzy.FuzzyInteger(*GENERAL_RANGE)
    health = fuzzy.FuzzyInteger(*GENERAL_RANGE)
    keywords = factory.Iterator(models.Keyword.objects.all())
    races = factory.Iterator(models.Race.objects.all())


class ItemCardFactory(CardFactory):
    card_type = ITEM
    keywords = factory.Iterator(models.Keyword.objects.all())


class ActionCardFactory(CardFactory):
    card_type = ACTION

# TODO: tweak the factories so multiple keywords, races, and attributes are assigned
