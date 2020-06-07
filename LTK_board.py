import LTK_deck 
import LTK_player
import random
import logging

log = logging.getLogger('default')

class board:
    def __init__(self, n_players):
        self.table = {}
        self.assignPositionsandRoles(n_players)
        self.characterChoices()
        self.deck = LTK_deck.Deck()
        self.deal()
        self.playerturn = 0
        self.gameover = False




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
            p.draw(4, self.deck)


    # def play(self):
    #     # basic rules for going around in order and having each character play 
        
    #     while not gameover():
    #         self.turn(self.table[self.playerturn])
    #         self.playerturn = (self.playerturn + 1) % len(self.table)

    #     # say who won game



    # def turn(self, player):
    #     player.beforeplayphase(deck)
    #     player.judgmentphase(deck)
    #     player.drawphase(deck)
    #     while True: 
    #         output = player.actionphase(deck)
    #         if output == False:
    #             break
    #         else:
    #             pass
    #             # Resolve play based on card, target.  If equipment or lightning, just report it 
    #     player.discardphase(deck)
    #     player.afterplayphase(deck)




    # def checkDistance(self, attacker, defender, card):

    #     #distance = min(abs(attacker position - defender postion), abs((attacker potion + len(self.table)) - defender position), abs(attacker position - (defender position + len(self.table))))
    #     #modify by horses
    #     if card == "Strike":
    #         # modify by weapons
    #         pass

    #     return distance



    # def gameover(self):
    #     pass
    #     # check if game over based on roles left, if it is then set self.gameover = True



    # def death(self, player, damagesource):
    #     pass
    #     # check for peaches
    #     # if dead:
    #     #     call player.death() 
    #     #     resolve additional stuff based on player.role (i.e. give cards to damage source if rebel)
    #     #     remove them from the table and move everyone after them up one position (i.e. if player at position 6 dies, move player 7 at position 7 to position 6)
    #     #     if position of player < self.playerturn: 
    #     #         self.playerturn += 1
    #     #     self.gameover() to check if the games over







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