import random
class Poke():

    def __init__(self):
        self.FaceNum = list(range(1, 14))
        self.Suit = ['heart', 'spade', 'club', 'diamond']
        self.cards = []
        self.player1 = []
        self.player2 = []
        self.player3 = []
        self.player4 = []
    def populate(self):
        for suit in self.Suit:
            for number in self.FaceNum:
                self.cards.append(suit+' '+str(number))
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self):
        self.player1 = self.cards[0:13]
        for player in self.player1:
            print(player.strip())
        self.player2 = self.cards[13:26]
        print(self.player2)
        self.player3 = self.cards[26:39]
        print(self.player3)
        self.player4 = self.cards[39:52]
        print(self.player4)
pk = Poke()
pk.populate()
pk.shuffle()
pk.deal()