import socket 
import time

host = '127.0.0.1'
port = 8000

s = socket.socket()
s.bind((host,port))
s.listen(10)

conn, address = s.accept()
print(conn, address)

while True:
  conn.send("Hiiii".encode())
  print('Sent message')
  time.sleep(2)
conn.close()

s.close()