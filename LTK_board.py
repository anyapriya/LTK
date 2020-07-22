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
        self.table = {} #key is position, and stores player object
        self.deadPlayers = []
        self.deck = LTK_deck.Deck()

        self.assignPositionsandRoles(n_players)
        self.characterChoices()
        self.deal()

        self.playerturn = 0
        self.rounds = 0
        self.winner = None





    # assigns everyone a random role, put monarch at position 0, put everyone else at a random position
    def assignPositionsandRoles(self, n_players):
        roles = []
        for key,val in RoleDistribution[n_players].items():
            roles.extend([key]*val)
        
        names = []
        for i in range(1, n_players + 1):
            inputname = input("Please input player {n}'s name:\n".format(n = i))
            while inputname in names:
                inputname = input("That name has already been chosen, please input another name for player {n}:\n".format(n = i))
            names.append(inputname) 

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
            self.table[i] = LTK_player.Player(self.table[i][0], self.table[i][1], i, self.deck, self)




    def deal(self):
        for p in self.table.values():
            p.draw(4)


    ##################################################################################################################################################
    #
    # Gameplay
    #
    ##################################################################################################################################################



    def play(self):
        # basic rules for going around in order and having each character play 
        
        while not self.winner: 

            log.info("Round: {rounds}".format(rounds = self.rounds))
            log.info("Player Turn: {name}".format(name = self.table[self.playerturn]))
            for i in self.table:
                log.info("Player {name} currently has {health} health".format(name = self.table[i].name, health = self.table[i].health))


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

        player.beforeplayphase()

        skipPlay = False
        while True: 
            output = player.judgmentphase() 
            if output["Type"] is None:
                break
            elif output["Type"] == "Contentment" and output["Result"] == -1:
                skipPlay = True

        player.drawphase()

        while not skipPlay: 
            output = player.actionphase() 
            if output == False: #no more cards to play, or player decided to end turn
                break


        player.discardphase()
        player.afterplayphase()



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








#Monarch is always 1
#TODO: check if this role distribution is correct
RoleDistribution = {4: {"Minister": 0, "Rebel": 2, "Turncoat": 1},
                    5: {"Minister": 1, "Rebel": 2, "Turncoat": 1}, 
                    6: {"Minister": 1, "Rebel": 3, "Turncoat": 1},
                    7: {"Minister": 2, "Rebel": 3, "Turncoat": 1},
                    8: {"Minister": 2, "Rebel": 4, "Turncoat": 1},
                    9: {"Minister": 3, "Rebel": 4, "Turncoat": 1},
                    10: {"Minister": 3, "Rebel": 4, "Turncoat": 2}}