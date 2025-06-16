class Card():
    SUITS = ("Hearts", "Clubs", "Spades", "Diamonds")
    RANKS = (
                "2", "3", "4", "5", "6","7","8","9","10",
                "Jack", "Queen", "King", "Ace"
            )
    
    @classmethod
    def create_52_cards(cls):
        return [
            cls(rank = rank, suit = suit)
            for suit in cls.SUITS
            for rank in cls.RANKS
        ]

        cards = []
        for suit in cls.SUITS:
            for rank in cls.RANKS:
                cards.append(cls(rank = rank, suit = suit))

        return cards

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank. Rank must be one of the following {self.RANKS}")

        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit. Suit must be one of {self.SUITS}")
        
        self.rank = rank
        self.suit = suit
        self.rank_index = self.RANKS.index(rank)
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"
    
    def __eq__(self, value):
        return self.rank == value.rank and self.suit == value.suit
    
    def __lt__(self, other_card):
        return self.rank_index < other_card.rank_index
