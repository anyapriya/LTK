import LTK_board
from LTK_Exceptions import PlayerCountOutOfBounds



if __name__ == "__main__":
    
    players = input("Please enter how many players (4-10): ")
    while True:
        try:
            
            players = int(players)
            if players < 4 or players > 10:
                raise PlayerCountOutOfBounds
            break
        except ValueError:
            players = input("Did not enter a number.  Please input a number between 4 and 10 and hit enter: ")
        except PlayerCountOutOfBounds:
            players = input("Number was not an allowed number of players.  Please input a number between 4 and 10 and hit enter: ")

    board = LTK_board.board(players)
    # board.play()


