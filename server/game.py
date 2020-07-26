import random

possible_cards = ['Strike', 'Dodge', 'Peach', 'Borrowed Sword', 'Wine']

class Game(object):
  def __init__(self):
    self.hand = ['Strike', 'Strike', 'Dodge', 'Peach']

  def draw_card(self):
    self.hand.append(random.choice(possible_cards))

  def shuffle_hand(self):
    random.shuffle(self.hand)

  def discard_card(self):
    self.hand.pop(0)