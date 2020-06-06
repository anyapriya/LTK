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
    