import LTK_deck 
import LTK_player
import random
import logging

log = logging.getLogger('default')

class board:

    ##################################################################################################################################################
    #
    # Initialization functions
    #
    ##################################################################################################################################################



    def __init__(self, n_players):
        self.table = {}
        self.assignPositionsandRoles(n_players)
        self.characterChoices()
        self.deck = LTK_deck.Deck()
        self.deal()
        self.playerturn = 0
        self.rounds = 0
        self.winner = None



    # assigns everyone a random role, put monarch at position 0, put everyone else at a random position
    def assignPositionsandRoles(self, n_players):
        roles = []
        for key,val in RoleDistribution[n_players].items():
            roles += [key]*val
        
        names = []
        for i in range(1, n_players + 1):
            names += [input("Please input player {n}'s name:\n".format(n = i))]

        for i in range(n_players):
            if i == 0:
                self.table[i] = [names.pop(random.randrange(0,len(names))), "Monarch"]
            else:
                self.table[i] = [names.pop(random.randrange(0,len(names))), roles.pop(random.randrange(0,len(roles)))]

        log.info("Assigned positions and rolls")
            
        


    def characterChoices(self):
        for i in range(len(self.table)):
            # have player at 0 (Monarch) choose character first, put the ones they didn't choose back in pool
            # for others, don't put choices back in pool
            # everything except Monarch should be simultaneous....  but for now..... a loop will do 
            # initialize players from LTK_player based on character selection - for now generic player
            self.table[i] = LTK_player.Player(self.table[i][0], self.table[i][1])


    def deal(self):
        for p in self.table.values():
            p.draw(self.deck, 4)


    ##################################################################################################################################################
    #
    # Gameplay
    #
    ##################################################################################################################################################



    def play(self):
        # basic rules for going around in order and having each character play 
        
        while not self.winner: 

            if self.playerturn == 0:
                self.rounds += 1 #everytime it's the monarch's turn, it counts as a new round 

            self.turn(self.playerturn) 

            self.playerturn = (self.playerturn + 1) % len(self.table) # just an update for who goes next 

            if self.rounds > 5:  #safety for now, remove later
                log.info("Reached over 5 rounds, we're quitting the game") 
                self.winner = "No one"

        log.info("The winner was: " + self.winner)



    def turn(self, playerposition):
        player = self.table[playerposition]

        player.beforeplayphase(self.deck)

        skipPlay = False
        while True: 
            output = player.judgmentphase(self.deck) #does nothing for now since no judgements in the deck yet, but it's coded
            if output["Type"] == "Lightning":
                if output["Result"] == -1:
                    self.checkDeath(playerposition, playerposition)
                else:
                    self.table[(self.playerturn + 1) % len(self.table)].judgement += output["Result"] #Put the card in the next person's judgement pile
            elif output["Type"] == "Contentment" and output["Result"] == -1:
                skipPlay = True
            else:
                break

        player.drawphase(self.deck)

        while not skipPlay: 
            output = player.actionphase(self.deck) #action phase returns False for now so doesn't do anything
            if output == False:
                break
            else:
                pass
                # TODO: Resolve play based on card, target.  If equipment or lightning, just report it 


        player.discardphase(self.deck)
        player.afterplayphase(self.deck)




    # def checkDistance(self, attacker, defender, card):

    #     #distance = min(abs(attacker position - defender postion), abs((attacker potion + len(self.table)) - defender position), abs(attacker position - (defender position + len(self.table))))
    #     #modify by horses
    #     if card == "Strike":
    #         # modify by weapons
    #         pass

    #     return distance



    def isGameOver(self):
        stillMonarch = False
        stillRebel = False
        stillTurncoat = False
        for i in self.table:
            if stillMonarch and (stillRebel or stillTurncoat):
                return False
            if i.role == "Monarch":
                stillMonarch = True
            if i.role == "Rebel":
                stillRebel = True
            if i.role == "Turncoat":
                stillTurncoat = True
        if stillMonarch:
            self.winner = "Team Monarch"
        elif stillRebel:
            self.winner = "Team Rebel"
        else:
            self.winner = "The Lone Turncoat"

        
        


    
    def checkDeath(self, playerposition, damagesourceposition):
        player = self.table[playerposition]

        if player.health > 0:
            return False
        else:
            peachorder = [i if i < len(self.table) else i % len(self.table) for i in range(damagesourceposition, damagesourceposition + len(self.table))]
            for i in peachorder:
                wanttogivepeaches = True
                while wanttogivepeaches & player.health < 1:
                    #ask player i for peaches
                    #if they give a peach:
                    #    discard peach
                    #    heal player
                    #else:
                    #    wanttogivepeaches = False
                    pass
                if player.health > 0:
                    return False
                
            # because of the return False above, if it gets here, the player is dead
            player.loseEverything(self.deck)
            if damagesourceposition != self.playerturn:
                if player.role == "Rebel":
                    self.table[damagesourceposition].draw(3)
                if player.role == "Minister" and self.table[damagesourceposition].role == "Monarch":
                    self.table[0].loseEverything(self.deck)
                    
            for i in range(playerposition, len(self.table) - 1):
                self.table[i] = self.table[i + 1]
            del(self.table[len(self.table) - 1]) #do we want some record of who's dead?  This doesn't seem the best method but it's a good temporary solution for making the game work
            if playerposition < self.playerturn:
                self.playerturn -= 1
            
            self.isGameOver()










    # ##################################################################################################################################################
    # #
    # # Stuff to play on your turn that affects other players (stuff that doesn't affect others will be dealt with in by player functions)
    # #
    # ##################################################################################################################################################

    # def Strike(self, attacker, defender):
    #     checkDistance(attacker, defender, "Strike")
    #     #check armor of defender
    #     #ask defender to play dodge or take hit
    #     #if struck, do defender.damage(n)
    #     pass
    
    # ####### Scrolls

    # def Dismantle(self, attacker, defender):
    #     pass

    # def BorrowedSword(self, attacker, puppet, defender):
    #     pass

    # def Snatch(self, attacker, defender):
    #     checkDistance(attacker, defender, "Snatch")
    #     pass

    # def Duel(self, attacker, defender):
    #     pass

    # def Contentment(self, attacker, defender):
    #     pass

    # ######## AOE Scrolls

    # def Barbarians(self, attacker):
    #     pass

    # def ArrowBarrage(self, attacker):
    #     pass

    # def PeachGarden(self, attacker):
    #     pass

    # def BountifulHarvest(self, attacker):
    #     pass




#Monarch is always 1
#Is this correct???
RoleDistribution = {4: {"Minister": 0, "Rebel": 2, "Turncoat": 1},
                    5: {"Minister": 1, "Rebel": 2, "Turncoat": 1}, 
                    6: {"Minister": 1, "Rebel": 3, "Turncoat": 1},
                    7: {"Minister": 2, "Rebel": 3, "Turncoat": 1},
                    8: {"Minister": 2, "Rebel": 4, "Turncoat": 1},
                    9: {"Minister": 3, "Rebel": 4, "Turncoat": 1},
                    10: {"Minister": 3, "Rebel": 4, "Turncoat": 2}}