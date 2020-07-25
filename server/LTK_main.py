import asyncio
import LTK_board
from LTK_Exceptions import PlayerCountOutOfBounds
import LTK_configs
import logging
# import multiprocessing
import time

log = logging.getLogger('default')

def getPlayers():
    # players = input("Please enter how many players (4-10): ")
    players = 4
    while True:
        try:
            
            players = int(players)
            if players < 4 or players > 10:
                raise PlayerCountOutOfBounds
            break
        except ValueError:
            log.debug("ValueError on player input (couldn't be parsed into an int): {inp}".format(inp = players))
            players = input("Did not enter a number.  Please input a number between 4 and 10 and hit enter: ")
        except PlayerCountOutOfBounds:
            log.debug("Too low or too high number on player input: {inp}".format(inp = players))
            players = input("Number was not an allowed number of players.  Please input a number between 4 and 10 and hit enter: ")
    return players


async def game(queue):
    # websocket_process = multiprocessing.Process(target=start_websocket, args=())
    # websocket_process.start()
    await queue.put("TEST")
    await asyncio.sleep(5)
    log.info("Getting player counts")
    players = getPlayers()
    log.info("Initializing board with {n} players".format(n = players))
    # await send("TESTING")
    board = LTK_board.board(players)
    board.play()
    return


if __name__ == "__main__":
    pass