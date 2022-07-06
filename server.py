import socket
import threading

# Connection Data
host = '192.168.56.102' #localhost
port = 8889

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []

# Sending Messages To All Connected Clients
def broadcast(message):
      for client in clients:
          client.send(message)

# Handling Messages From Clients
def handle(client):
        while True:
               try:

                   # Broadcasting Messages
                   message = client.recv(1024)
                   broadcast(message)

               except:
                   # Removing And Closing Clients
                   index = clients.index(client)
                   clients.remove(client)
                   client.close()
                   nickname = nicknames[index]
                   broadcast(f'{nickname} left the chat!'.encode('ascii'))
                   nicknames.remove(nickname)
                   break

# Receiving / Listening Function
def receive():
      while True:
            # Accept Connection
            client, address = server.accept()
            print(f'Connected with {str(address)}')

            # Request And Store Nickname
            client.send('NICK'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            nicknames.append(nickname)
            clients.append(client)

            # Print And Broadcast Nickname
            print(f'Nickname of the client is {nickname}!')
            broadcast(f'{nickname} joined the chat! '.encode('ascii'))
            client.send('Connected to server!'.encode('ascii'))

            # Start Handling Thread For Client 
            thread = threading.Thread(target=handle, args=(client,))
            thread.start()

print("Server is listening… \N{smiling face with sunglasses} \N{zipper-mouth face} \N{loudly crying face} \N{rolling on the floor laughing} \N{face with tears of joy}")
receive()
