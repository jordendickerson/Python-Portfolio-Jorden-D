class Card(object):
    RANKS = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    SUITS = ["♠","♥","♣","♦"]

    def __init__(self,rank,suit):
        self.rank = rank
        self. suit = suit

    def __str__(self):
        rep = str.format("""
        _____________
       |{0}{1}          |
       |             |
       |             |
       |             |
       |             |
       |             |
       |             |
       |         {1}{0} |
        _____________
        """,self.rank,self.suit)
        return rep

class Pos_card(Card):
    def __init__(self, rank, suit, face_up = True):
        super(Pos_card, self).__init__(rank, suit)
        self.is_face_up = face_up
    def __str__(self):
        if self.is_face_up:
            rep = super(Pos_card, self).__str__()
        else:
            rep = """
        _____________
       |             |
       |             |
       |             |
       |             |
       |             |
       |             |
       |             |
       |             |
        _____________
        """
        return rep
    def flip(self):
        self.is_face_up = not self.is_face_up

class Hand(object):
    def __init__(self):
        self.cards = []

    @property
    def cardsTotal(self):
        return len(self.cards)

    def __str__(self):
        rep = ""
        if self.cards:
            for card in self.cards:
                rep += str(card)
        else:
            rep = "<EMPTY>"

        return rep

    def add(self,card):
        self.cards.append(card)

    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)

    def clear(self):
        self.cards.clear()

    """Deck of playing cards"""
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Can't continue deal. Out of Cards!")

if __name__ == "__main__":
    print("This is not aprogram try importing and using the classes.")
    input("\n\nPress the enter key to exit")


