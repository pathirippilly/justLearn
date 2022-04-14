class Card:
    """
    only below values allowded 
    
    suit=("Hearts","Diamonds","Clubs","Spades")
    rank=("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    """
    _suit=("Hearts","Diamonds","Clubs","Spades")
    _rank=("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        if(self.suit not in Card._suit or self.rank not in Card._rank):
            raise ValueError('CardNotFound') 
               
    def __repr__(self):
        return self.rank+" of "+self.suit
    
    def getRank():
        return Card._rank
    
    def getSuit():
        return Card._suit
