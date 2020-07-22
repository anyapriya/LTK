import unittest
from unittest.mock import patch
import itertools

from LTK_main import getPlayers
from LTK_board import board
from LTK_deck import Deck
from LTK_player import Player



class test_main(unittest.TestCase):

    getPlayers_data = [['4'], ['10'], ['6'], ['3', '4'], ['11', '10'], ['Meow', '6.5', '4']]
    @patch('builtins.input', side_effect= itertools.chain.from_iterable(getPlayers_data))
    def test_getPlayers(self, mock_input, getPlayers_data= getPlayers_data):
        for i in getPlayers_data:
            self.assertEqual(getPlayers(), int(i[-1]))



class test_board(unittest.TestCase):
    pass #TODO


class test_player(unittest.TestCase):
    def test_draw(self):
        deck = Deck()
        player = Player("Azulon", "Monarch", 0, deck, None)
        self.assertEqual(len(player.hand), 0)
        player.draw(4)
        self.assertEqual(len(player.hand), 4)
        for i in player.hand:
            self.assertNotIn(i, deck.deck)
            self.assertNotIn(i, deck.discardpile)


    def test_judgementdraw(self):
        pass #TODO


    def test_discard(self):
        deck = Deck()
        player = Player("Bumi", "Monarch", 0, deck, None)
        player.draw(8)

        discardedcard = player.hand[2]
        self.assertNotIn(discardedcard, deck.deck)
        self.assertNotIn(discardedcard, deck.discardpile)
        self.assertIn(discardedcard, player.hand)

        player.discard(cards = [discardedcard])

        self.assertNotIn(discardedcard, deck.deck)
        self.assertIn(discardedcard, deck.discardpile)
        self.assertNotIn(discardedcard, player.hand)

        discardedcards = player.hand[1:4]

        for discardedcard in discardedcards:
            self.assertNotIn(discardedcard, deck.deck)
            self.assertNotIn(discardedcard, deck.discardpile)
            self.assertIn(discardedcard, player.hand)

        player.discard(cards = discardedcards)

        for discardedcard in discardedcards:
            self.assertNotIn(discardedcard, deck.deck)
            self.assertIn(discardedcard, deck.discardpile)
            self.assertNotIn(discardedcard, player.hand)


        handsize = len(player.hand)
        discardpilesize = len(deck.discardpile)
        player.discard(count = 3)
        self.assertEqual(handsize - 3, len(player.hand))
        self.assertEqual(discardpilesize + 3, len(deck.discardpile))


    def test_damaged_and_heal(self):
        deck = Deck()
        player = Player("Zuko", "Monarch", 0, deck, None)
        startinghealth = player.health

        player.damaged(2)
        self.assertEqual(startinghealth - 2, player.health)

        player.heal(1)
        self.assertEqual(startinghealth - 1, player.health)

        player.damaged(8)
        self.assertEqual(startinghealth - 9, player.health) #health can go negative

        player.heal(10)
        self.assertEqual(player.health, player.maxhealth) #shouldn't go over max health
        

    def test_loseEverything(self):
        deck = Deck()
        player = Player("Ozai", "Monarch", 0, deck, None)
        player.draw(4)
        #TODO: put something in player's equipement pile once we have equipment cards coded in

        self.assertNotEqual(player.hand, [])
        # self.assertNotEqual(player.equipment, {"Off_horse": None, "Def_horse": None, "Armor": None, "Weapon": None})

        player.loseEverything()

        self.assertEqual(player.hand, [])
        self.assertEqual(player.equipment, {"Off_horse": None, "Def_horse": None, "Armor": None, "Weapon": None})

    def test_strike(self):
        pass #TODO

    def test_dodge(self):
        pass #TODO

    def test_beforeplayphase(self):
        pass #TODO

    def test_judgementphast(self):
        pass #TODO

    def test_drawphase(self):
        pass #TODO

    def test_actionphase(self):
        pass #TODO
    
    def test_discardphase(self):
        pass #TODO

    def test_afterplayphase(self):
        pass #TODO




class test_deck(unittest.TestCase):
    
    def test_shuffle(self):
        deck = Deck()

        originaldrawpilesize = len(deck.deck)
        drawncards = deck.draw(originaldrawpilesize - 3)
        deck.discard(drawncards)

        deckremaining = deck.deck.copy()
        deck.shuffle()

        self.assertEqual(originaldrawpilesize, len(deck.deck))
        self.assertEqual(deckremaining, deck.deck[:3])
        for i in drawncards:
            self.assertIn(i, deck.deck[3:])



    def test_drawanddiscardlist(self):
        deck = Deck()
        n = 4

        originaldrawpilesize = len(deck.deck)
        drawncards = deck.draw(n)
        self.assertEqual(originaldrawpilesize - n, len(deck.deck))

        for i in drawncards:
            self.assertNotIn(i, deck.deck)
            
        originaldiscardpilesize = len(deck.discardpile)
        deck.discard(drawncards)
        self.assertEqual(originaldiscardpilesize + n, len(deck.discardpile))
        for i in drawncards:
            self.assertIn(i, deck.discardpile)
                

    def test_drawanddiscardsingle(self):
        deck = Deck()
        n = 4

        originaldrawpilesize = len(deck.deck)
        drawncards = deck.draw(n)
        self.assertEqual(originaldrawpilesize - n, len(deck.deck))

        for i in range(len(drawncards)):
            self.assertNotIn(drawncards[i], deck.deck)
            originaldiscardpilesize = len(deck.discardpile)
            deck.discard(drawncards[i])
            self.assertIn(drawncards[i], deck.discardpile)
            self.assertEqual(originaldiscardpilesize + 1, len(deck.discardpile))



    def test_notenoughindrawpile(self):
        deck = Deck()

        originaldrawpilesize = len(deck.deck)

        firstdrawncards = deck.draw(originaldrawpilesize - 3)
        deck.discard(firstdrawncards)

        seconddrawncards = deck.draw(5)
        for i in firstdrawncards:
            self.assertTrue( (i in deck.deck) ^ (i in seconddrawncards) )




if __name__ == '__main__':
    unittest.main()
    