from Card import Card
from Deck import Deck
import unittest

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card=Card("Hearts","A")
        
    def test_init(self):
        """rank,suit  and error validation"""
        """user input rank and suit should be from available list"""
        
        self.assertEqual(self.card.rank,"A",msg="rank validation failed")
        self.assertEqual(self.card.suit,"Hearts",msg="suit validation failed")
        with self.assertRaises(ValueError,msg='error validation failed'):
            self.card_invalid=Card("Hearts","B")
    def test_repr(self):
        self.assertEqual(self.card.__repr__(),"A of Hearts",msg="__repr__ method validation failed")

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck_valid=Deck(1)
    def test_init(self):
        self.assertEqual(len(self.deck_valid.decks),52,msg="fresh deck validation failed")
        
     
if (__name__ == "__main__"):
    unittest.main()



