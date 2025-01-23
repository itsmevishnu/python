import socket

client = socket.socket()

#connect to server

host = '127.0.0.1'
port = 8001
message = 'Hi, I am your client'

client.connect((host, port))

client.send(message.encode())
print("Sending message to server")

data = client.recv(1024).decode()
print(f"Recieved data from server {data}")

client.close()