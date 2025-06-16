import unittest
from poker.card import Card
from poker.hand import Hand

class HandTest(unittest.TestCase):
    def test_recieves_and_stores_cards(self):
        ace_of_spades = Card("Ace", "Spades")
        six_of_clubs = Card("6", "Clubs")
        cards = [
            ace_of_spades,
            six_of_clubs
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.cards,
            [
                six_of_clubs,
                ace_of_spades
            ]
        )

    