from poker.card import Card
from poker.deck import Deck
from poker.hand import Hand
from poker.player import Player

deck = Deck()
cards = Card.create_52_cards()

deck.add_cards(cards)

hand1 = Hand(cards= [])
hand2 = Hand(cards= [])

player1 = Player("Aviv", hand1)
player2 = Player("Boris", hand2)

# card1 = Card(rank = "2", suit= "Spades")
# card2 = Card(rank= "Ace", suit= "Hearts")

print(cards)