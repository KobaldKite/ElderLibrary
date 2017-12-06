![Image of ReadMe card](http://elderdecks.com/img/customcards/readme_2-793.png)



The web-application should help TESL (The Elder Scrolls Legends) players to keep track of their card collection and popular decks, so players know exactly what cards they are still missing to finish certain decks and how much would it cost to acquire those cards.

The application is a work in progress, and the ReadMe mostly covers features not yet released.

Features:
* import your card collection from a file (Universal Deck Tracker format)
* publish decks, see other people's decks, comment on and rate those decks
* see what cards your are missing in your collection to build certain decks and how much they cost
* look up information on cards and expansions

---------------------------

Entities:
* User:
** has a single collection which he can update
* can publish multiple decks
* can rate and comment on other people's decks
* Collection:
** just a list of all user's cards and their numbers
** hidden from other users
* Deck:
** a list of cards and their numbers that satisfies certain conditions (minimum number of cards in a deck, maximum number of card duplicates, etc.)
** has user rating and user comments
** has user applied tags (fast, slow, token) and properties for sorting and filtering (used card colors, total cost, cost of the cards user misses)
* Card:
** a number of properties and their values (rarity, stats, expansion they were introduced in, etc.)
