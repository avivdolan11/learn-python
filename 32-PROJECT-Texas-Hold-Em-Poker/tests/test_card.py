import unittest
from poker.card import Card

class CardTest(unittest.TestCase):
    def test_has_rank(self):
        card = Card(rank = "Queen", suit = "Hearts")
        self.assertEqual(card.rank, "Queen")

    def test_has_suit(self):
        card = Card(rank = "2", suit = "Clubs")
        self.assertEqual(card.suit, "Clubs")
    
    def test_has_string_representation(self):
        card = Card("5", "Diamonds")
        self.assertEqual(str(card), "5 of Diamonds")
    
    def test_technical_representation(self):
        card = Card("9", "Spades")
        self.assertEqual(repr(card), "Card('9', 'Spades')")

    def test_card_has_four_possible_suits(self):
        self.assertEqual(
            Card.SUITS, 
            ("Hearts", "Clubs", "Spades", "Diamonds")
        )

    def test_card_has_thirteen_possible_ranks(self):
        self.assertEqual(
            Card.RANKS, 
            (
                "2", "3", "4", "5", "6","7","8","9","10",
                "Jack", "Queen", "King", "Ace"
                )
        )
    
    def test_card_only_allows_for_valid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank = "two", suit="Spades")

    def test_card_only_allows_for_valid_suit(self):
        with self.assertRaises(ValueError):
            Card(rank = "2", suit="Spade")

    def test_creates_standard_52_cards(self):
        cards = Card.create_52_cards()
        self.assertEqual(len(cards), 52)

        self.assertEqual(
            cards[0],
            Card(rank = "2", suit = "Hearts")
        )

        self.assertEqual(
            cards[-1],
            Card(rank = "Ace", suit= "Diamonds")
        )

    def test_figures_if_two_cards_equal(self):
        self.assertEqual(
        Card(rank = "Ace", suit= "Diamonds"),
        Card(rank = "Ace", suit= "Diamonds")
        )