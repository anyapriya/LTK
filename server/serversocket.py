import socket 

host = '127.0.0.1'
port = 8000

s = socket.socket()
s.bind((host,port))
s.listen(10)

conn, address = s.accept()

conn.send("Hiiii".encode())
conn.close()

s.close()