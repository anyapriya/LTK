import LTK_deck 
import LTK_player


class board:
    def __init__(self, n_players):
        # for number of players, get player names somehow
        self.table = self.assignPositionsandRoles(playernames)
        self.characterChoices()
        self.deck = LTK_deck.Deck()
        self.deal()
        self.playerturn = 0
        self.gameover = False


    def assignPositionsandRoles(self, playernames):
        # assign everyone a random role, put monarch at position 0, put everyone else at a random position
        # self.table = {0: ["playername1", "monarch"], 1: ["playername1", role], 2: "playername2", ["playername2", role]}
        pass


    def characterChoices(self)
        # character selection
        for key, val in self.table.items():
            # have player (val[0]) choose character
            # initialize players from LTK_player based on character selection - initialize with role, player name
            # self.table[key] = initialized player 
            pass

    def deal(self):
        for i in range(4):
            for p in self.table.values:
                p.draw(1, self.deck)


    def play(self):
        # basic rules for going around in order and having each character play 
        
        while not gameover():
            self.turn(self.table[self.playerturn])
            self.playerturn = (self.playerturn + 1) % len(self.table)

        # say who won game



    def turn(self, player):
        player.beforeplayphase(deck)
        player.judgmentphase(deck)
        player.drawphase(deck)
        while True: 
            output = player.actionphase(deck)
            if output == False:
                break
            else:
                pass
                # Resolve play based on card, target.  If equipment or lightning, just report it 
        player.discardphase(deck)
        player.afterplayphase(deck)




    def checkDistance(self, attacker, defender, card):

        
        #distance = min([abs(attacker position - defender postion), abs((attacker potion + len(self.table)) - defender position), abs(attacker position - (defender position + len(self.table)))])
        #modify by horses
        if card == "Strike":
            pass # modify by weapons too

        return distance



    def gameover(self):
        pass
        # check if game over based on roles left, if it is then set self.gameover = True



    def death(self, player, damagesource):
        pass
        # check for peaches
        # if dead:
            # call player.death() 
            # resolve additional stuff based on player.role (i.e. give cards to damage source if rebel)
            # remove them from the table and move everyone after them up one position (i.e. if player at position 6 dies, move player 7 at position 7 to position 6)
            # self.gameover() to check if the games over




    def Strike(self, attacker, defender):
        checkDistance(attacker, defender, "Strike")
        #check armor of defender
        #ask defender to play dodge or take hit
        #if struck, do defender.damage(n)
        pass
    
  