from cards import *
import commonGameFunctions as cgf
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


class Deck(Hand, Card):
    """Deck of playing cards"""
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                card = Pos_card(rank, suit)
                self.add(card)
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self, hands, per_hand = 1):
        cards_needed = len(hands)* per_hand
        if len(self.cards) >= cards_needed + len(hands)*3:

            for rounds in range(per_hand):
                for hand in hands:

                        top_card = self.cards[0]
                        self.give(top_card, hand)
        else:
            print("Not enough cards to deal")
            x = cgf.ask_yes_no("Do you want to keep playing? (y/n): ")
            if x == "y":
                for hand in hands:
                    hand.clear()
                self.clear()
                self.populate()
                self.shuffle()
                self.deal(hands,per_hand)
            else:
                return

if __name__ == "__main__":
    print("This is not aprogram try importing and using the classes.")
    input("\n\nPress the enter key to exit")