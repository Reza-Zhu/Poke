from card import Card
from poke import Poke
player=[]
cd=Card()
pk=Poke()
def start(num):
    print('player'+str(num))
    return '\n %s'%(cd.cover())

print('发牌开始：\n')
i=1
while i<5:
    start(i)
    i=i+1

result=input('是否要翻牌？Y/N')
if result=='Y':
    cd.flip()
elif result=='N':
    j = 1
    while j < 5:
        start(j)
        j = j + 1

