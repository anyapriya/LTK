import logging


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





    def draw(self, n, deck):
        drawncards = deck.draw(n)
        self.hand += drawncards

#     def judgementdraw(self, deck):
#         judgement = deck.draw(1)
#         deck.discard(judgement)
#         return judgement

#     def discard(self, card = None, count = 1):
#         if card == None:
#             # have player choose {count} cards to discard
#             pass
#         #remove card(s) from hand or equipment depending
#         deck.discard(card)


#     def damaged(self, n):
#         self.health -= n

#     def heal(self, n):
#         if self.health < self.maxhealth:
#             self.health += n
#             return True
#         else: 
#             return False


#     def death(self, deck):

#         for i in self.hand:
#             deck.discard(i)
#         self.hand = []

#         for i in self.judgement:
#             deck.discard(i)
#         self.judgement = []

#         for key,val in self.equipment.items():
#             if val is not None:
#                 deck.discard(val)
#                 self.equipment[key] = None



#     ##########################################################################


    def beforeplayphase(self, deck):
        pass #for stuff like examining top of deck, etc

    # def judgmentphase(self, deck):
    #     if len(self.judgement) == 0:
    #         pass
    #     else:
    #         pass
    #         for i in reversed(judgement):
    #             judgementcard = judgementdraw(deck)
    #             if i == lightning:
    #                 #check if judgmentcard is a 2 through 9 of spades and resolve
    #                 #if it blows up, do self.discard, otherwise return card so it's passed to next player in LTK_board.py
    #                 pass 
    #             elif i == contentment:
    #                 #check if judgementcard is good or bad and resolve
    #                 #will need to return some method of telling LTK_board if action phase needs to be skipped
    #                 pass 
    #         # Remember to do self.discard(card) if needed
            


    def drawphase(self, deck):
        self.draw(2, deck)

#     #probably want each of the else sections to call a separate function so we can use inheritance to more easily modify small pieces for abilities but leave most of it in place for characters
#     def actionphase(self, deck): 
#         if len(hand) == 0:
#             return False #Done playing cards
#         else:
#             #check if want to play a card or done with turn
#             if done:
#                 return False #Done playing cards
#             else:
#                 #play card
#                 #remember to to self.discard(card) with cards that should be in the discard pile 
#                 if card == equipment:
#                     # Add to equipment section: replace equipment (do self.discard(card)) and put new equipment there
#                     return True
#                 elif card == lightning:
#                     # Add to judgement section, remove from hand
#                     return True
#                 elif card == peach:
#                     self.heal(1)
#                     self.discard(card) 
#                     return True
#                 elif card == somethingfornothing:
#                     self.draw(2, deck)
#                     self.discard(card)
#                     return True
#                 elif card == aoe:
#                     self.discard(card)
#                     return [card, "all"]
#                 elif card == contentment:
#                     # remove from hand, don't discard!  
#                     return [card, target]
#                 else:
#                     # Have player choose target, do self.discard(card)
#                     return [card, target]

#     def discardphase(self, deck):
#         if len(self.hand) > self.health:
#             self.discard(count = len(self.hand) - self.health)
        

#     def afterplayphase(self, deck):
#         pass #for stuff like drawing after turn


# #use inheritance to do all the characters and modify each phase 