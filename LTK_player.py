
class Player():
    def __init__(self, name, role):
        self.name
        self.hand = []
        self.equipment = {"Off_horse": None, "Def_horse": None, "Armor": None, "Weapon": None}
        self.judgement = []
        self.role = None

    def play(self, deck):
        self.judgment()
        self.draw(deck)
        self.action()
        self.discard()

    def judgment(self):
        pass

    def draw(self, deck):
        drawncards = deck.draw(2)
        #add cards to hand

    def action(self):
        pass

    def discard(self):
        pass

#use inheritance to do all the characters and modify each phase 