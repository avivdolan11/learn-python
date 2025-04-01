from poker.card import Card
from poker.deck import Deck

deck = Deck()
cards = Card.create_52_cards()

deck.add_cards(cards)

# card1 = Card(rank = "2", suit= "Spades")
# card2 = Card(rank= "Ace", suit= "Hearts")

print(cards)