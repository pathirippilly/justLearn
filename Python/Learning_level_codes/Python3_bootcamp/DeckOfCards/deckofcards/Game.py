from Card import Card
from Deck import Deck


#Deck1=Deck(2)
#print(Deck1)
#print(Deck1._deal(5,2))
#print(Deck1)
#print(Deck1._deal(5,1))
#print(Deck1)

Deck1=Deck(1)
d=Deck1.CurrentDeck().copy()
d_s=Deck1.shuffleDeck().copy()
d_r=Deck1.resetDeck()
print(str(d_s))
print(str(d_s) == str(d_r))
print(d_r)

