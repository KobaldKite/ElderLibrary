import factory
from factory import fuzzy
from .models import Attribute, Card, Expansion, Keyword, Race
from .models import CARD_TYPES_LIST, CARD_RARITIES_LIST

INDEX_SHIFT = 1
GENERAL_RANGE = [0, 10]
CARD_RARITY_RANGE = [INDEX_SHIFT, len(CARD_RARITIES_LIST) + INDEX_SHIFT]

CARD_ATTRIBUTES = ['agility', 'endurance', 'intelligence',
                   'strength', 'willpower', 'neutral']

ACTION = CARD_TYPES_LIST.index('action') + INDEX_SHIFT
CREATURE = CARD_TYPES_LIST.index('creature') + INDEX_SHIFT
ITEM = CARD_TYPES_LIST.index('item') + INDEX_SHIFT


class AttributeFactory(factory.Factory):
    class Meta:
        model = Attribute

    name = factory.Iterator(CARD_ATTRIBUTES, cycle=False)


class ExpansionFactory(factory.Factory):
    class Meta:
        model = Expansion

    name = fuzzy.FuzzyText(length=6, prefix='Expansion_')


class KeywordFactory(factory.Factory):
    class Meta:
        model = Keyword

    name = factory.Faker('word')


class RaceFactory(factory.Factory):
    class Meta:
        model = Race

    name = factory.Faker('word')


class CardFactory(factory.Factory):
    class Meta:
        model = Card

    name = factory.Faker('word')
    image = factory.django.ImageField(color='green')
    attributes = factory.RelatedFactory(AttributeFactory)
    rarity = fuzzy.FuzzyInteger(*CARD_RARITY_RANGE)
    summon_cost = fuzzy.FuzzyInteger(*GENERAL_RANGE)
    soultrap_cost = fuzzy.FuzzyInteger(*GENERAL_RANGE)
    magicka_cost = fuzzy.FuzzyInteger(*GENERAL_RANGE)
    mechanics_text = factory.Factory('word')
    flavor_text = factory.Factory('sentence')
    is_collectible = fuzzy.FuzzyChoice([True, False])
    expansion = factory.RelatedFactory(ExpansionFactory)


class CreatureCardFactory(CardFactory):
    card_type = CREATURE

    attack = fuzzy.FuzzyInteger(*GENERAL_RANGE)
    health = fuzzy.FuzzyInteger(*GENERAL_RANGE)
    keywords = factory.RelatedFactory(KeywordFactory)
    races = factory.RelatedFactory(KeywordFactory)


class ItemCardFactory(CardFactory):
    card_type = 3
    keywords = factory.RelatedFactory(KeywordFactory)


class ActionCardFactory(CardFactory):
    card_type = 1

#TODO: tweak the factories so multiple keywords, races, and attributes are assigned
