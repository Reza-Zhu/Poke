import random
import copy
from card import Card
from hand import Hand
class Poke(Hand):

    def __init__(self):
        super().__init__()
        self.cd=Card()
    def populate(self):
        for suit in self.cd.Suit:
            for number in self.cd.FaceNum:
                self.cards.append(suit+' '+str(number))
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self):
        self.player1 = self.cards[0:13]
        self.player2 = self.cards[13:26]
        self.player3 = self.cards[26:39]
        self.player4 = self.cards[39:52]