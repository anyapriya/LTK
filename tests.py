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
    pass

class test_player(unittest.TestCase):
    pass

class test_deck(unittest.TestCase):
    pass



if __name__ == '__main__':
    unittest.main()
    