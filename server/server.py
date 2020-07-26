import eventlet
import socketio
import json
import game
import random

sio = socketio.Server(cors_allowed_origins='*') # temporarily allow all origins to fix CORS issues
app = socketio.WSGIApp(sio)

@sio.event
def connect(sid, environ):
  print('connect ', sid)
  gamestate() # Send the client the current gamestate as soon as they connect (for now)

@sio.event
def shuffle_hand(sid):
  game.shuffle_hand()
  gamestate()

@sio.event
def discard_card(sid):
  game.discard_card()
  gamestate()

@sio.event
def draw_card(sid):
  game.draw_card()
  gamestate()

# Sends the current gamestate to all players
def gamestate():
  sio.emit('gamestate', game.hand)

@sio.event
def disconnect(sid):
  print('disconnect ', sid)

if __name__ == '__main__':
  game = game.Game()
  eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
