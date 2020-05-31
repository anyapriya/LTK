import random



class Deck:

    def __init__(self):
        self.deck = [i for i in cards]
        self.discard = []
        self.shuffle()

    def shuffle(self):
        self.deck += self.discard
        random.shuffle(self.deck)
        self.discard = []

    def draw(self, n):
        drawn = []
        for i in n:
            drawn += [self.deck.pop(0)]
        return drawn


    def discard(self, cards):
        if type(cards) is list:
            self.discard += cards
        else:
            self.discard += [cards] #can get rid of this if we're always careful about inputting a list of even just one item 
        



# cards will be represented numerically, so deck and hand just have ints that can be used to call and get info of card from this dict 
# this dict might be replaced with a DB table, and just get the data from there and fill the info in with code
# for now though, will hard code in a few cards just for use
cards = {1: {"Card": "Strike", "Value": 10, "Suit": "Spades"},
         2: {"Card": "Strike", "Value": 10, "Suit": "Spades"},
         }


