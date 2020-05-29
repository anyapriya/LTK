
class Player:

    def __init__(self, name, role):
        self.name
        self.hand = []
        self.equipment = {"Off_horse": None, "Def_horse": None, "Armor": None, "Weapon": None}
        self.judgement = []
        self.role = role
        self.health = 4
        if self.role == "Monarch":
            self.health += 1



    def death(self, deck):
        pass #do deck.discard() for all cards in hand, judgement, equipment

    def draw(self, n, deck):
        drawncards = deck.draw(n)
        hand += drawncards

    def damaged(self, n):
        self.health -= n

    def beforeplayphase(self, deck):
        pass #for stuff like examining top of deck, etc

    def judgmentphase(self, deck):
        if len(judgement) == 0:
            pass
        else:
            # Remember to do deck.discard() if needed
            pass

    def drawphase(self, deck):
        self.draw(2, deck)

    def actionphase(self, deck):
        if len(hand) == 0:
            return False
        else:
            #check if want to play a card or done with turn
            if done:
                return False
            else:
                #play card
                #remember to to deck.discard() with cards that should be in the discard pile and remove them from hard
                if equipment:
                    # Add to equipment section: replace equipment (do deck.discard()) and put new equipment there
                    return True
                elif aoe:
                    # Remove from hand and do deck.discard()
                    return [card, "all"]
                elif ligtning:
                    # Add to judgment section
                    return True
                else:
                    # Have player choose 
                    return [card, target]

    def discardphase(self, deck):
        pass
        #remember to do deck.discard() with cards that should be in the discard pile and remove them from hard

    def afterplayphase(self, deck):
        pass #for stuff like drawing after turn


#use inheritance to do all the characters and modify each phase 