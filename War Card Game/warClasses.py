import cards as c
import hands as h
import commonGameFunctions as cgf
import random

class War_Card(c.Pos_card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = War_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None

        return v

class War_Hand(h.Hand):
    def __init__(self, name):
        super(War_Hand, self).__init__()
        self.name = name

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None

        # add up card values, treat each Ace as 1
        t = 0
        for card in self.cards:
            t += card.value
        # determine if hand contains an Ace
        contains_ace = False
        for card in self.cards:
            if card.value == War_Card.ACE_VALUE:
                contains_ace = True
        if contains_ace and t <= 11:
            t += 10
        return t


    def __str__(self):
        rep = h.Hand.__str__(self)
        rep += self.name + "\t" + "(" + str(self.total) + ")"
        return rep

    def flipHand(self):
        for card in self.cards:
            card.is_face_up = True



class War_Deck(object, c):
    def add(self,card):
        self.cards.append(card)
    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)
    def populate(self):
        for suit in War_Card.SUITS:
            for rank in War_Card.RANKS:
                card = War_Card(rank, suit)
                self.add(card)
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self, players, oneHand, twoHand):
        for player in players:
            self.give(self.cards, oneHand)
            self.give(self.cards, twoHand)







class War_Player(War_Hand):
    def lose(self):
        print(self.name, "loses.")

    def win(self):
        print(self.name, "wins.")

class War_Game(object):

    def __init__(self, names):
        self.players = []
        self.playerOneHand = []
        self.playerTwoHand = []
        self.table = []
        for name in names:
            player = War_Player(name)
            self.players.append(player)

        self.deck = War_Deck()
        self.deck.populate()
        self.deck.shuffle()

    def battle(self):

        for hand in self.players:
            hand.flipHand()

        for player in self.players:
            print(player)
        if self.players[0].total > self.players[1].total:
            print(self.players[0], "wins both cards")


        else:
            print(self.players[1], "wins both cards")
        input("Press enter to go to the next round")


    def play(self):
        print(self.playerOneHand)
        print(self.playerTwoHand)

        # if self.players[0] != self.players[1]:
        #     self.battle()
        # else:
        #     pass



