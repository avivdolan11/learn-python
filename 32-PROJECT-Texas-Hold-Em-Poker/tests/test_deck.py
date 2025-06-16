import unittest
from poker.card import Card
from poker.deck import Deck
from poker.hand import Hand

class DeckTest(unittest.TestCase):
    def test_stores_no_cards_at_start(self):
        deck = Deck()
        self.assertEqual(
            deck.cards,
            []
        )

    def test_add_cards_to_its_collection(self):
        card = Card(rank="Ace", suit= "Spades")
        deck = Deck()
        deck.add_cards([card])

        self.assertEqual(
            deck.cards,
            [card]
        )
    
    def test_figures_out_high_card_is_best_rank(self):
        cards = [
            Card("Ace", "Diamonds"),
            Card("7", "Clubs")
        ]

        hand = Hand(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            "High Card"
        )

    def test_figures_out_pair_is_best_rank(self):
        cards = [
            Card("Ace", "Spades"),
            Card("Ace", "Hearts")
        ]

        hand = Hand(cards=cards)

        self.assertEqual(
            hand.best_rank(),
            "Pair"
        )

    def test_figures_out_two_pair_is_best_rank(self):
        cards = [
            Card("Ace", "Spades"),
            Card("Ace", "Hearts"),
            Card("5", "Diamonds"),
            Card("King", "Spades"),
            Card("King", "Clubs")
        ]

        hand = Hand(cards=cards)

        self.assertEqual(
            hand.best_rank(),
            "Two Pair"
        )

    def test_figures_out_three_of_a_kind_is_best_rank(self):
        cards = [
            Card("King", "Hearts"),
            Card("Ace", "Hearts"),
            Card("5", "Diamonds"),
            Card("King", "Spades"),
            Card("King", "Clubs")
        ]

        hand = Hand(cards=cards)

        self.assertEqual(
            hand.best_rank(),
            "Three of a Kind"
        )

    def test_figures_out_that_straight_is_the_best_hand(self):
        cards = [
            Card("6", "Hearts"),
            Card("7", "Hearts"),
            Card("8", "Diamonds"),
            Card("9", "Spades"),
            Card("10", "Clubs")
        ]

        hand = Hand(cards=cards)

        self.assertEqual(
            hand.best_rank(),
            "Straight"
        )
    def test_figures_out_best_rank_when_flush(self):
        cards = [
            Card(rank=rank, suit = "Hearts")
            for rank in ["2", "5", "8", "10", "Ace"]
        ]

        hand = Hand(cards=cards)

        self.assertEqual(
            hand.best_rank(),
            "Flush"
        )

    def test_figures_out_best_rank_when_full_house(self):
        cards = [
            Card("3", "Hearts"),
            Card("3", "Clubs"),
            Card("3", "Diamonds"),
            Card("9", "Hearts"),
            Card("9", "Spades")
        ]

        hand = Hand(cards=cards)

        self.assertEqual(
            hand.best_rank(),
            "Full House"
        )

    def test_figures_out_best_rank_when_four_of_a_kind(self):
        cards = [
            Card("3", "Hearts"),
            Card("3", "Clubs"),
            Card("3", "Diamonds"),
            Card("3", "Spades"),
            Card("9", "Spades")
        ]

        hand = Hand(cards=cards)

        self.assertEqual(
            hand.best_rank(),
            "Four of a Kind"
        )

    def test_figures_out_best_rank_when_straight_flush(self):
        cards = [
            Card("3", "Clubs"),
            Card("4", "Clubs"),
            Card("5", "Clubs"),
            Card("6", "Clubs"),
            Card("7", "Clubs")
        ]

        hand = Hand(cards=cards)

        self.assertEqual(
            hand.best_rank(),
            "Straight Flush"
        )

    def test_figures_out_best_rank_when_royal_flush(self):
        cards = [
            Card("10", "Clubs"),
            Card("Jack", "Clubs"),
            Card("Queen", "Clubs"),
            Card("King", "Clubs"),
            Card("Ace", "Clubs")
        ]

        hand = Hand(cards=cards)

        self.assertEqual(
            hand.best_rank(),
            "Royal Flush"
        )

    def test_figures_out_no_cards_is_best_rank(self):
        hand = Hand([])

        self.assertEqual(
            "No Cards",
            hand.best_rank()
        )