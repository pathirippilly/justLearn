from Card import Card
from random import shuffle

class Deck:
 
    
    def __init__(self,count):
        if count>=0:
            
            self.count=count
            self.decks=[Card(suit,rank) for suit in Card.getSuit() for rank in Card.getRank()]*self.count
        else :
            raise ValueError("invalid entry.Number should be positive!!")
        #print(self.decks)
    def __repr__(self):
        count_per_deck=len(self.decks)
        return str(count_per_deck)   
        
    def CurrentDeck(self):
        return self.decks
    def CurrentCount(self):
        return len(self.decks)
    def _deal(self,num):
        if type(num) is int and num>=0 and self.decks != []:
            removed_cards=self.decks[:num:]
            self.decks[:num:]=[]
            return  removed_cards
        elif  type(num) is not int or num<=0 :
            raise Exception("Invalid entry,you shoud enter a positive number!!")
        elif self.decks==[]:
            raise ValueError("Deck is Empty") 
    def shuffleDeck(self):
        
        
        if len(self.decks) % 52 == 0:
            shuffle(self.decks)
            return self.decks
                
        else:
            raise Exception("Only a full deck can be shuffled")
        
    def deal_card(self):
        
        return self._deal(1)[0]
    def deal_hand(self,hand_size):
        return self._deal(hand_size)
    def resetDeck(self):
        self.decks=[Card(suit,rank) for suit in Card.getSuit() for rank in Card.getRank()]*self.count
        return self.decks
    
        
            
                
                 