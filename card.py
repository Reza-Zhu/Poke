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
