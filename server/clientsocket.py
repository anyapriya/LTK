import socket

host = '127.0.0.1'
port = 8000

s = socket.socket()
s.connect((host,port))

while True:
  print(s.recv(1024))

s.close()