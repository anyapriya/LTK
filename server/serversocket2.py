#!/usr/bin/env python

# WS server example

import asyncio
import websockets
from LTK_main import game

async def game_handler(queue):
  await game(queue)

# returns the latest game state
async def producer(queue):
  return await queue.get()

async def producer_handler(websocket, path, queue):
  while True:
    message = await producer(queue)
    await websocket.send(message)

# reads the latest client updates
async def consumer(message):
  print(f"< {message}")

async def consumer_handler(websocket, path):
  while True:
    message = await websocket.recv()
    await consumer(message)

async def handler(websocket, path):
    message_queue = asyncio.Queue()
    game_task = asyncio.ensure_future(game_handler(message_queue))
    consumer_task = asyncio.ensure_future(consumer_handler(websocket, path))
    producer_task = asyncio.ensure_future(producer_handler(websocket, path, message_queue))
    done, pending = await asyncio.wait(
        [consumer_task, producer_task, game_task],
        return_when=asyncio.FIRST_COMPLETED, # Should this be all_completed?
    )
    print("Done")
    for task in pending:
        task.cancel()

def start_websocket():
  start_server = websockets.serve(handler, "localhost", 8000)

  asyncio.get_event_loop().run_until_complete(start_server)
  asyncio.get_event_loop().run_forever()

start_websocket()