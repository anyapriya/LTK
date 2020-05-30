


class Deck:

    def __init__(self):
        self.deck = []
        self.discard = []
        self.shuffle()

    def shuffle(self):
        pass

    def draw(self, n):
        pass
        #remove n cards from deck and return them

    def discard(self, cards):
        #add cards to discard
        pass



# cards will be represented numerically, so deck and hand just have ints that can be used to call and get info of card from this dict 
cards = {1: {"Card": "Strike", "Value": 10, "Suit": "Spades"},
         2: {"Card": "Strike", "Value": 10, "Suit": "Spades"},
         }


