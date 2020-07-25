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
        self.judgementpile = []
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



    def draw(self, n):
        drawncards = self.deck.draw(n)
        log.info("Player {name} drew cards:".format(name = self.name))
        log.info(drawncards)
        self.hand += drawncards
        log.debug(self.hand)


    #TODO: make tests!
    def judgementdraw(self):
        judgement = self.deck.draw(1)
        self.deck.discard(judgement)
        return judgement


    # cards should be a list if discarding specific card(s), else use count to specify how many and ask the player which to discard
    # TODO: probably should be 2 different functions
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


    def checkDeath(self, damagesourceposition):

        if self.health > 0:
            return False
        else:
            self.askForPeaches(damagesourceposition)
            if self.health > 0:
                return False
                
            # because of the return False above, if it gets here, the player is dead
            self.loseEverything()
            if damagesourceposition != self.position:
                if self.role == "Rebel":
                    self.board.table[damagesourceposition].draw(3)
                if self.role == "Minister" and self.board.table[damagesourceposition].role == "Monarch":
                    self.board.table[0].loseEverything()
                    
            self.board.deadPlayers.append(self)
            for i in range(self.position, len(self.board.table) - 1):
                self.board.table[i] = self.board.table[i + 1]
            del(self.board.table[len(self.board.table) - 1]) #do we want some record of who's dead?  This doesn't seem the best method but it's a good temporary solution for making the game work
            if self.position < self.board.playerturn:
                self.board.playerturn -= 1
            
            self.position = -1
            for key, val in self.board.table.items():
                val.position = key

            self.board.isGameOver()



    ##################################################################################################################################################
    #
    # Off turn Actions
    #
    ##################################################################################################################################################


    #TODO: make tests!
    def dodge(self, damage, source):
        #TODO: have player decide if they want to play a dodge and which dodge
        for i in self.hand:
            if LTK_deck.cards[i]["Type"] == "Dodge":
                self.discard([i])
                log.info("Dodged")
                return True

        self.damaged(damage)
        self.checkDeath(source)
        return False


    def wardSomething(self):
        #TODO: If player has a ward in hand, ask if they want to ward a card, if yes, discard ward and check for more wards, if ward goes through then return True, otherwise return False
        return False

    def askForWards(self):
        #Joe's idea - if no one has any, this will run super fast and give away that no one has any - choose a random small amount of time, if it ran faster than that, then have it sleep difference 
        wardOrder = [i if i < len(self.board.table) else i % len(self.board.table) for i in range(self.position, self.position + len(self.board.table))]
        for i in wardOrder:
            if self.board.table[i].wardSomething():
                return True #warded

        return False #not warded


    def peachsomeonedying(self):
        #TODO: If player has a peach in hand, ask if they want to peach the person dying, if yes, discard peach and return True, otherwise return False
        return False


    def askForPeaches(self, damagesourceposition):
        #Joe's idea - if no one has any, this will run super fast and give away that no one has any - choose a random small amount of time, if it ran faster than that, then have it sleep difference 
        peachOrder = [i if i < len(self.board.table) else i % len(self.board.table) for i in range(damagesourceposition, damagesourceposition + len(self.board.table))] #TODO: this should be from damage source, it's from dying person's right now
        for i in peachOrder:
            while self.health < 1:
                if self.board.table[i].peachsomeonedying():
                    self.health += 1
                else: 
                    break
            if self.health > 0:
                return False
        




    ##################################################################################################################################################
    #
    # On turn actions
    #
    ##################################################################################################################################################

    ####### Basic cards


    #TODO: make tests!
    def Strike(self):
        reach = 1
        # TODO: add to it based on equipment, for now no equipment

        possibletargets = []
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

    def Equipment(self, card):
        # Have a dict that maps card id to equipment type
        # if there's something in the equipment slot, so self.deck.discard it
        # put the new equipment in the slot
        pass


    ####### Delayed Scrolls

    def Contentment(self):
        #Ask who it's targeting
        pass



    ####### Scrolls

    def Dismantle(self): #TODO
        #Ask who it's targeting
        if not self.askForWards(): 
            return True
        else:
            return True

    def BorrowedSword(self): #TODO
        #Ask who it's targeting as a puppet (make sure someone with a weapon) and who they can target (someone in range) - if unplayable return False
        if not self.askForWards(): 
            return True
        else:
            return True #playable, just warded

    def Snatch(self): #TODO
        #Ask who it's targeting (make sure in range) - if unplayable return False
        if not self.askForWards(): 
            return True
        else:
            return True #playable, just warded

    def Duel(self): #TODO
        #Ask who it's targeting
        if not self.askForWards(): 
            return True
        else:
            return True 

    ######## AOE Scrolls

    def Barbarians(self, attacker): #TODO
        pass

    def ArrowBarrage(self, attacker): #TODO
        pass

    def PeachGarden(self, attacker): #TODO
        pass

    def BountifulHarvest(self, attacker): #TODO
        pass



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
        if len(self.judgementpile) == 0:
            pass
        else:
            outcomes["Type"] = LTK_deck.cards[self.judgementpile[-1]]["Type"]

            if self.askForWards():
                judgementcard = None
            else:
                judgementcard = LTK_deck.cards[self.judgementdraw()]

            #Last in, first out

            if outcomes["Type"] == "Lightning": 
                if judgementcard is None or (judgementcard["Suit"] != "Spades" or judgementcard["Value"] < 2 or judgementcard["Value"] > 9):
                    outcomes["Result"] = 0
                    self.board.table[(self.board.playerturn + 1) % len(self.board.table)].judgementpile.append(self.judgementpile.pop(-1)) #Put the card in the next person's judgement pile
                else:
                    self.deck.discard(self.judgementpile.pop(-1))
                    self.damaged(3)
                    outcomes["Result"] = 1
                    self.checkDeath(self.position)

            elif outcomes["Type"] == "Contentment":
                self.deck.discard(self.judgementpile.pop(-1))
                if judgementcard is None or judgementcard["Suit"] == "Hearts":
                    outcomes["Result"] = 0
                else:
                    outcomes["Result"] = 1

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
                

                #BASIC CARDS 
                if cardType == "Dodge" or cardType == "Ward":
                    # Can't play dodge or ward on turn, TODO: make sure they can't choose it 
                    return True

                #TODO: - instead call corresponding function that shares name with cardType?  Gets rid of all the if statements...  
                elif cardType == "Peach":
                    self.heal(1)
                    self.discard([self.hand[cardPlayed]]) 
                    return True

                elif cardType == "Strike": 
                    couldPlay = self.Strike()
                    if couldPlay:
                        self.discard([self.hand[cardPlayed]]) 
                    return True 


                #DELAYED SCROLLS
                elif cardType == "Lightning":
                    self.judgementpile.append(cardPlayed)
                    return True

                elif cardType == "Contentment": #TODO
                    return True


                #REGULAR SCROLLS
                elif cardType == "SomethingForNothing": 
                    if not self.askForWards():
                        self.draw(2)
                    self.discard([self.hand[cardPlayed]])
                    return True

                elif cardType == "Snatch": #TODO
                    couldPlay = self.Snatch()
                    if couldPlay:
                        self.discard([self.hand[cardPlayed]]) 
                    return True

                elif cardType == "BorrowedSword": #TODO
                    couldPlay = self.BorrowedSword()
                    if couldPlay:
                        self.discard([self.hand[cardPlayed]]) 
                    return True

                elif cardType == "Dismantle": #TODO
                    self.Dismantle()
                    self.discard([self.hand[cardPlayed]]) 
                    return True

                elif cardType == "Duel": #TODO
                    self.Duel()
                    self.discard([self.hand[cardPlayed]]) 
                    return True


                #AOE SCROLLS
                elif cardType == "BountifulHarvest": #TODO
                    return True

                elif cardType == "PeachGarden": #TODO
                    return True

                elif cardType == "ArrowBarrage": #TODO
                    return True

                elif cardType == "BarbarianInvasion": #TODO
                    return True


                #EQUIPMENT
                elif cardType == "Equipment": #TODO
                    self.Equipment(cardPlayed)
                    self.hand.remove(cardPlayed)
                    return True



    #TODO: make tests!
    def discardphase(self):
        if len(self.hand) > self.health:
            self.discard(count = len(self.hand) - self.health)
        

    #TODO: make tests!
    def afterplayphase(self):
        pass #for stuff like drawing after turn


