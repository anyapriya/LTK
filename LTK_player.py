
class Player:

    def __init__(self, name, role):
        self.name
        self.hand = []
        self.equipment = {"Off_horse": None, "Def_horse": None, "Armor": None, "Weapon": None}
        self.judgement = []
        self.role = role
        self.maxhealth = 4
        self.health = 4
        if self.role == "Monarch":
            self.health += 1
            self.maxhealth += 1



    def death(self, deck):
        pass #do deck.discard() for all cards in hand, judgement, equipment

    def draw(self, n, deck):
        drawncards = deck.draw(n)
        hand += drawncards

    def discard(self, card = None):
        if card == None:
            # have player choose card
        #remove card from hand or equipment depending
        deck.discard(card)


    def damaged(self, n):
        self.health -= n


    ##########################################################################


    def beforeplayphase(self, deck):
        pass #for stuff like examining top of deck, etc

    def judgmentphase(self, deck):
        if len(judgement) == 0:
            pass
        else:
            # Remember to do self.discard(card) if needed
            pass


    def drawphase(self, deck):
        self.draw(2, deck)

    #probably want each of the else sections to call a separate function so we can use inheritance to more easily modify small pieces for abilities but leave most of it in place for characters
    def actionphase(self, deck): 
        if len(hand) == 0:
            return False #Done playing cards
        else:
            #check if want to play a card or done with turn
            if done:
                return False #Done playing cards
            else:
                #play card
                #remember to to self.discard(card) with cards that should be in the discard pile 
                if equipment:
                    # Add to equipment section: replace equipment (do self.discard(card)) and put new equipment there
                    return True
                elif lightning:
                    # Add to judgement section
                    return True
                elif peach:
                    if self.health < self.maxhealth:
                        self.health += 1
                    # Add 1 to health, do self.discard(card) 
                    return True
                elif somethingfornothing:
                    self.draw(2, deck)
                    return True
                elif aoe:
                    # Do self.discard(card)
                    return [card, "all"]
                elif ligtning:
                    # Add to judgment section
                    return True
                else:
                    # Have player choose target, do self.discard(card)
                    return [card, target]

    def discardphase(self, deck):
        pass
        #remember to do self.discard(card) with cards that should be in the discard pile and remove them from hard

    def afterplayphase(self, deck):
        pass #for stuff like drawing after turn


#use inheritance to do all the characters and modify each phase 