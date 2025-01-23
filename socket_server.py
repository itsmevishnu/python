import socket

server = socket.socket()
host = '127.0.0.1'
port = 8001
message = 'Hi, I am your server'

#bind to ip address
server.bind((host, port))

server.listen(1)
print("Hi I am a server, listening port 8000")

client, a = server.accept()
print(f"A connection has established with {a}")

data = client.recv(1024).decode()
print(f"Message received from client : {data}")

client.send(message.encode())

# Close
client.close()
server.close()
