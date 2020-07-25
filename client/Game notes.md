# How a game is played
1. Lobby created by Leader
  * Min players (unless CPUs)
  * Max players
2. Players join lobby
3. Game started by Leader
4. Positions and Roles distributed randomly
5. Hero selection
  * Monarch chooses
  * Everyone sees Monarch's choice
  * Other players choose
6. Game begins
  * Hands distributed
  * Monarch starts turn
  * Turns rotate between players until one team is left
7. Game over
  * Server sends all players' roles and cards to all players
  * Winner(s) is shown
  * Play Again? (Leader)
  * End Lobby? (Leader)
  * Automatically end lobby after set amount of time

# Turn phases order
* Beginning of turn
* Judgement
* Draw
* Play phase
* Discard
* End of turn

Server sends changes of board state and possible actions after every game state change
  * What was added
  * What was removed
  * What was changed

One active player at any time:
  * Usually the player currently taking their turn
  * Responses:
    - Warding scrolls
    - Peaching someone on Death's Door
    - When being struck to dodge
    - When being targeted with Duel, Blaze, etc
    - AOE scrolls or abilities like Barbarians
    - Some hero abilities (more complex, mostly expansion heroes)
  * Responses where the player is unable to respond will be delayed a random amount of time

Client error logs sent to server