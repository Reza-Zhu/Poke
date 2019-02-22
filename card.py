class Card():
    def __init__(self):
        self.FaceNum=list(range(1,14))
        self.Suit=['heart','spade','club','diamond']
    def _str_(self):
        return "POINT: %d+ %s"%(self.Suit,self.FaceNum)
    def pic_order(self):
        for suit in self.Suit:
            if suit=='club':
                for number in self.FaceNum:
                    order=number+0
            if suit=='diamond':
                for number in self.FaceNum:
                    order=number+13
            if suit=='heart':
                for number in self.FaceNum:
                    order=number+26
            if suit=='spade':
                for number in self.FaceNum:
                    order=number+39
    def flip(self,player):
        from poke import Poke                ##没有放在开头，避免模块交叉引用
        poke=Poke()
        if player=='player1':
            print(poke.player1)
        elif player=='player2':
            print(poke.player2)
        elif player=='player3':
            print(poke.player3)
        elif player=='player4':
            print(poke.player4)

    def cover(self):
        num=0
        player_cover=[]
        while num < 13:
            player_cover.append(' * ')
            num = num + 1
        print(player_cover)