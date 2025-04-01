import unittest
from poker.card import Card
from poker.hand import Hand

class HangTest(unittest.TestCase):
    def test_recieves_and_stores_cards(self):
        cards = [
            Card("Ace", "Spades"),
            Card("6", "Clubs")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.cards,
            cards
        )