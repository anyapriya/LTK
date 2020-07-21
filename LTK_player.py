import logging
import traceback
import LTK_deck
from LTK_Exceptions import NoActionDefinedForCard
import random #only needed as a placeholder 

log = logging.getLogger('default')


class Player:

    def __init__(self, name, role, position, deck, board):
        self.position = position
        self.name = name
        self.hand = []
        self.equipment = {"Off_horse": None, "Def_horse": None, "Armor": None, "Weapon": None}
        self.judgement = []
        self.role = role
        self.maxhealth = 4
        self.health = 4
        self.deck = deck
        self.board = board
        if self.role == "Monarch":
            self.health += 1
            self.maxhealth += 1


    ##################################################################################################################################################
    #
    # Helper Functions
    #
    ##################################################################################################################################################


    #TODO: make tests!
    def draw(self, n):
        log.info("Player drawing cards")
        log.debug(self.hand)
        drawncards = self.deck.draw(n)
        log.info("Player drew cards:")
        log.info(drawncards)
        self.hand += drawncards
        log.debug(self.hand)
        log.info("Player finished drawing cards")


    #TODO: make tests!
    def judgementdraw(self):
        judgement = self.deck.draw(1)
        self.deck.discard(judgement)
        return judgement


    #cards should be a list if discarding specific card(s), else use count to specify how many and ask the player which to discard - TODO: probably should be 2 different functions
    def discard(self, cards = None, count = 1):
        if cards == None: 
            log.debug(self.hand)
            log.debug("Discarding {n} cards".format(n = count))
            for i in range(count):
                self.deck.discard(self.hand.pop(0)) #for now just remove the first card, TODO: have player choose cards
        else:
            log.debug(self.hand)
            log.debug("Discarding the following cards:")
            log.debug(cards)
            for card in cards:
                self.hand.remove(card)
                self.deck.discard(card)

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


    #TODO: after we code in equipment cards, update tests!
    def loseEverything(self):

        for i in self.hand:
            self.deck.discard(i)
        self.hand = []

        for key,val in self.equipment.items():
            if val is not None:
                self.deck.discard(val)
                self.equipment[key] = None

    #TODO: make tests!
    def strike(self):
        reach = 1
        # TODO: add to it based on equipment, for now no equipment

        possibletargets = []
        print(self.board.table)
        for key,val in self.board.table.items():
            pass
            # TODO: check other people's range/equipement and see if they can be reached, what damage should be 

        # TODO: They can't play a strike
        # if len(possibletargets) == 0: 
        #     return False 

        # TODO: Choose who striking from possible targets, for now just next player
        target = (self.position + 1) % len(self.board.table)

        log.info("Player {offense} struck {defense}".format(offense = self.name, defense = self.board.table[target].name))
        self.board.table[target].dodge(1, self.position)
        return True


    #TODO: make tests!
    def dodge(self, damage, source):
        #TODO: have player decide if they want to play a dodge and which dodge
        for i in self.hand:
            if LTK_deck.cards[i]["Type"] == "Dodge":
                self.discard([i])
                log.info("Dodged")
                return True

        self.damaged(damage)
        self.board.checkDeath(self.position, source)
        return False


    ##################################################################################################################################################
    #
    # Turn Phases
    #
    ##################################################################################################################################################

    #TODO: make tests!
    def beforeplayphase(self):
        pass #for stuff like examining top of deck, etc


    #TODO: make tests!
    def judgmentphase(self):
        outcomes = {"Type": None, "Result": None} 
        if len(self.judgement) == 0:
            pass
        else:
            outcomes["Type"] = LTK_deck.cards[self.judgement[-1]]["Type"]
            judgementcard = self.judgementdraw()
            if outcomes["Type"] == "Lightning": #Last in, first out
                if LTK_deck.cards[judgementcard]["Suit"] == "Spades" and (LTK_deck.cards[judgementcard]["Value"] >= 2 or LTK_deck.cards[judgementcard]["Value"] <= 9):
                    self.deck.discard(self.judgement.pop(-1))
                    self.damaged(3)
                    outcomes["Result"] = -1
                else:
                    outcomes["Result"] = self.judgement.pop(-1)

            elif outcomes["Type"] == "Contentment":
                if LTK_deck.cards[judgementcard["Suit"]] != "Hearts":
                    outcomes["Result"] = -1

            else:
                #TODO: raise issue, nothing else should be there right now 
                pass

        return outcomes
            


    #TODO: make tests!
    def drawphase(self):
        self.draw(2)

    #TODO: make tests!
    #probably want each of the else sections to call a separate function so we can use inheritance to more easily modify small pieces for abilities but leave most of it in place for characters
    def actionphase(self): 

        if len(self.hand) == 0:
            log.info("Player {name} is out of cards".format(name = self.name))
            return False #Done playing cards
            
        else:
            #TODO: Ask player which card they want to play or if they're done 
            cardPlayed = random.randint(-1, len(self.hand) - 1)

            if cardPlayed == -1:
                log.info("Player {name} chose to end turn".format(name = self.name))
                return False #Done playing cards
            else:
                cardType = LTK_deck.cards[self.hand[cardPlayed]]["Type"]

                log.info("Player {name} chose to play {card}".format(name = self.name, card = cardType))
                
                if cardType == "Dodge" or cardType == "Ward":
                    # Can't play dodge or ward on turn, TODO: give warning to player
                    return True

                elif cardType == "Peach":
                    self.heal(1)
                    self.discard([self.hand[cardPlayed]]) 
                    return True

                elif cardType == "Strike": 
                    couldPlay = self.strike()
                    if couldPlay:
                        self.discard([self.hand[cardPlayed]]) 
                    return True 

                # elif cardType == "SomethingForNothing":
                #     self.draw(2)
                #     self.discard([self.hand[cardPlayed]])
                #     return True

                #Gotta do scrolls and equipment

                # elif cardType == equipment:
                #     # Add to equipment section: replace equipment (do self.discard(card)) and put new equipment there
                #     return True
                # elif cardType == "Lightning":
                #     # Add to judgement section, remove from hand
                #     return True

                else:
                    log.error("Nothing in ActionPhase defined for the following card definition:")
                    log.error(LTK_deck.cards[self.hand[cardPlayed]])
                    raise NoActionDefinedForCard


    #TODO: make tests!
    def discardphase(self):
        if len(self.hand) > self.health:
            self.discard(count = len(self.hand) - self.health)
        

    #TODO: make tests!
    def afterplayphase(self):
        pass #for stuff like drawing after turn


