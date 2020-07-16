import random
import logging

log = logging.getLogger('default')

class Deck:

    def __init__(self):
        self.deck = []
        self.discardpile = [i for i in cards]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.discardpile)
        self.deck += self.discardpile
        self.discardpile = []

    def draw(self, n):
        drawn = []
        if n > len(self.deck):
            self.shuffle()
        for i in range(n):
            drawn += [self.deck.pop(0)]
        return drawn


    def discard(self, cards):
        if type(cards) is list:
            self.discardpile += cards
        else:
            self.discardpile += [cards] #can get rid of this if we're always careful about inputting a list of even just one item 
        



# cards will be represented numerically, so deck and hand just have ints that can be used to call and get info of card from this dict 
# this dict might be replaced with a DB table, and just get the data from there and fill the info in with code
# for now though, will hard code in a few cards just for use
cards = {1: {"Type": "Strike", "Value": 10, "Suit": "Spades"},
         2: {"Type": "Strike", "Value": 10, "Suit": "Spades"},
         3: {"Type": "Strike", "Value": 9, "Suit": "Spades"},
         4: {"Type": "Strike", "Value": 9, "Suit": "Spades"},
         5: {"Type": "Strike", "Value": 8, "Suit": "Spades"},
         6: {"Type": "Strike", "Value": 8, "Suit": "Spades"},
         7: {"Type": "Strike", "Value": 7, "Suit": "Spades"},
         8: {"Type": "Strike", "Value": 10, "Suit": "Hearts"},
         9: {"Type": "Strike", "Value": 10, "Suit": "Hearts"},
         10: {"Type": "Strike", "Value": 10, "Suit": "Spades"},
         11: {"Type": "Strike", "Value": 10, "Suit": "Spades"},
         12: {"Type": "Strike", "Value": 10, "Suit": "Spades"},
         13: {"Type": "Strike", "Value": 9, "Suit": "Spades"},
         14: {"Type": "Strike", "Value": 9, "Suit": "Spades"},
         15: {"Type": "Strike", "Value": 8, "Suit": "Spades"},
         16: {"Type": "Strike", "Value": 8, "Suit": "Spades"},
         17: {"Type": "Strike", "Value": 7, "Suit": "Spades"},
         18: {"Type": "Strike", "Value": 10, "Suit": "Hearts"},
         19: {"Type": "Strike", "Value": 10, "Suit": "Hearts"},



         30: {"Type": "Peach", "Value": 3, "Suit": "Hearts"}, 
         31: {"Type": "Peach", "Value": 4, "Suit": "Hearts"},
         32: {"Type": "Peach", "Value": 6, "Suit": "Hearts"},


         50: {"Type": "Dodge", "Value": 2, "Suit": "Diamonds"}, 
         51: {"Type": "Dodge", "Value": 2, "Suit": "Diamonds"},
         52: {"Type": "Dodge", "Value": 3, "Suit": "Diamonds"},
         53: {"Type": "Dodge", "Value": 4, "Suit": "Diamonds"},
         54: {"Type": "Dodge", "Value": 5, "Suit": "Diamonds"},
         55: {"Type": "Dodge", "Value": 6, "Suit": "Diamonds"},
         56: {"Type": "Dodge", "Value": 7, "Suit": "Diamonds"},
         57: {"Type": "Dodge", "Value": 2, "Suit": "Diamonds"}, 
         58: {"Type": "Dodge", "Value": 2, "Suit": "Diamonds"},
         59: {"Type": "Dodge", "Value": 3, "Suit": "Diamonds"},
         69: {"Type": "Dodge", "Value": 4, "Suit": "Diamonds"},
         61: {"Type": "Dodge", "Value": 5, "Suit": "Diamonds"},
         62: {"Type": "Dodge", "Value": 6, "Suit": "Diamonds"},
         63: {"Type": "Dodge", "Value": 7, "Suit": "Diamonds"},


         }
# Value will be an int so: 1 is Ace?  11 is Jack? 12 is Queen? 13 is King?  