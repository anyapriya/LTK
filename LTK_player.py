import logging
import traceback
from LTK_deck import cards


log = logging.getLogger('default')


class Player:

    def __init__(self, name, role):
        self.name = name
        self.hand = []
        self.equipment = {"Off_horse": None, "Def_horse": None, "Armor": None, "Weapon": None}
        self.judgement = []
        self.role = role
        self.maxhealth = 4
        self.health = 4
        if self.role == "Monarch":
            self.health += 1
            self.maxhealth += 1


    ##################################################################################################################################################
    #
    # Helper Functions
    #
    ##################################################################################################################################################



    def draw(self, deck, n):
        log.info("Player drawing cards")
        log.debug(self.hand)
        drawncards = deck.draw(n)
        log.info("Player drew cards:")
        log.info(drawncards)
        self.hand += drawncards
        log.debug(self.hand)
        log.info("Player finished drawing cards")

    def judgementdraw(self, deck):
        judgement = deck.draw(1)
        deck.discard(judgement)
        return judgement

    #cards should be a list if discarding specific card(s), else use count to specify how many and ask the player which to discard
    def discard(self, deck, cards = None, count = 1):
        if cards == None: 
            log.debug(self.hand)
            log.debug("Discarding {n} cards".format(n = count))
            for i in range(count):
                deck.discard(self.hand.pop(0)) #for now just remove the first card
        else:
            log.debug(self.hand)
            log.debug("Discarding the following cards:")
            log.debug(cards)
            for card in cards:
                self.hand.remove(card)
                deck.discard(card)

        log.debug(self.hand)


    def damaged(self, n):
        self.health -= n
        return self.health

    def heal(self, n):
        if self.health < self.maxhealth:
            self.health = min(self.health + n, self.maxhealth)
            return True
        else: 
            return False


    def loseEverything(self, deck):

        for i in self.hand:
            deck.discard(i)
        self.hand = []

        for i in self.judgement:
            deck.discard(i)
        self.judgement = []

        for key,val in self.equipment.items():
            if val is not None:
                deck.discard(val)
                self.equipment[key] = None



    ##################################################################################################################################################
    #
    # Turn Phases
    #
    ##################################################################################################################################################


    def beforeplayphase(self, deck):
        pass #for stuff like examining top of deck, etc

    def judgmentphase(self, deck):
        outcomes = {"Type": None, "Result": None} 
        if len(self.judgement) == 0:
            pass
        else:
            outcomes["Type"] = cards[self.judgement[-1]]["Type"]
            judgementcard = self.judgementdraw(deck)
            if outcomes["Type"] == "Lightning": #Last in, first out
                if cards[judgementcard]["Suit"] == "Spades" and (cards[judgementcard]["Value"] >= 2 or cards[judgementcard]["Value"] <= 9):
                    self.discard(self.judgement.pop(-1))
                    self.damaged(3)
                    outcomes["Result"] = -1
                else:
                    outcomes["Result"] = self.judgement.pop(-1)

            elif outcomes["Type"] == "Contentment":
                if cards[judgementcard["Suit"]] != "Hearts":
                    outcomes["Result"] = -1

            else:
                #TODO: raise issue, nothing else should be there right now 
                pass

        return outcomes
            


    def drawphase(self, deck):
        self.draw(deck, 2)

    #probably want each of the else sections to call a separate function so we can use inheritance to more easily modify small pieces for abilities but leave most of it in place for characters
    def actionphase(self, deck): 
        return False
        # if len(hand) == 0:
        #     return False #Done playing cards
        # else:
        #     #check if want to play a card or done with turn
        #     if done:
        #         return False #Done playing cards
        #     else:
        #         #play card
        #         #remember to to self.discard(card) with cards that should be in the discard pile 
        #         if card == equipment:
        #             # Add to equipment section: replace equipment (do self.discard(card)) and put new equipment there
        #             return True
        #         elif card == lightning:
        #             # Add to judgement section, remove from hand
        #             return True
        #         elif card == peach:
        #             self.heal(1)
        #             self.discard(card) 
        #             return True
        #         elif card == somethingfornothing:
        #             self.draw(2, deck)
        #             self.discard(card)
        #             return True
        #         elif card == aoe:
        #             self.discard(card)
        #             return [card, "all"]
        #         elif card == contentment:
        #             # remove from hand, don't discard!  
        #             return [card, target]
        #         else:
        #             # Have player choose target, do self.discard(card)
        #             return [card, target]


    def discardphase(self, deck):
        if len(self.hand) > self.health:
            self.discard(deck, count = len(self.hand) - self.health)
        

    def afterplayphase(self, deck):
        pass #for stuff like drawing after turn


# #use inheritance to do all the characters and modify each phase 