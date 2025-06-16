class Hand():
    def __init__(self, cards):
        copy = cards[:]
        copy.sort()
        self.cards = copy

    @property
    def rank_validations_from_best_to_worst(self):
        return (
            ("Royal Flush", self.royal_flush),
            ("Straight Flush", self.straight_flush),
            ("Four of a Kind", self.four_of_a_kind),
            ("Full House", self.full_house),
            ("Flush", self.flush),
            ("Straight", self.straight),
            ("Three of a Kind", self.three_of_a_kind),
            ("Two Pair", self.two_pair),
            ("Pair", self.pair),
            ("High Card", self.high_card),
            ("No Cards", self.no_cards)
        )

    def best_rank(self):
        for rank in self.rank_validations_from_best_to_worst:
            name, validator_func = rank
            if validator_func():
                return name
            
    def royal_flush(self):
        is_straight_flush = self.straight_flush()
        if not is_straight_flush:
            return False
        is_royal = self.cards[-1].rank == "Ace"
        return is_straight_flush and is_royal
            
    def straight_flush(self):
        return self.flush() and self.straight()
            
    def four_of_a_kind(self):
        ranks_with_four_of_a_kind = self.ranks_with_count(4)
        return len(ranks_with_four_of_a_kind) == 1
    
    def full_house(self):
        return self.three_of_a_kind() and self.pair()
    
    def flush(self):
        suits_that_occur_5_or_more_times = {
            suit: suit_count
            for suit, suit_count in self.card_suit_counts.items()
            if suit_count >= 5
        }

        return len(suits_that_occur_5_or_more_times) == 1
            
    def straight(self):
        if len(self.cards) <5:
            return False

        rank_indexes = [card.rank_index for card in self.cards]
        starting_rank_index = rank_indexes[0]
        last_rank_index = rank_indexes[-1]
        straight_consecutive_indexes = list(
            range(starting_rank_index, last_rank_index + 1)
        )
        if rank_indexes == straight_consecutive_indexes and len(rank_indexes) == 5:
            return "Straight"
    
    def three_of_a_kind(self):
        ranks_with_three_of_a_kind = self.ranks_with_count(3)
        return len(ranks_with_three_of_a_kind) == 1
    
    def two_pair(self):
        ranks_with_pairs = self.ranks_with_count(2)
        return len(ranks_with_pairs) == 2
    
    def pair(self):
        ranks_with_pairs = self.ranks_with_count(2)
        return len(ranks_with_pairs) == 1
    
    def high_card(self):
        return len(self.cards) >= 2
    
    def no_cards(self):
        return len(self.cards) == 0

    def ranks_with_count(self, count):
        return {
            rank: rank_count
            for rank, rank_count in self.card_rank_counts.items() 
            if rank_count == count
        }
    
    @property
    def card_rank_counts(self):
        card_rank_counts = {}

        for card in self.cards:
            card_rank_counts.setdefault(card.rank, 0)
            card_rank_counts[card.rank] += 1

        return card_rank_counts
    
    @property
    def card_suit_counts(self):
        card_suit_counts = {}

        for card in self.cards:
            card_suit_counts.setdefault(card.suit, 0)
            card_suit_counts[card.suit] += 1

        return card_suit_counts