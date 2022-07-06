import socket
import threading
from datetime import datetime

e = datetime.now()

# Choosing Nickname
nickname = input("Choose your nickname \U0001F601 : ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('192.168.56.102', 8889))

# Listening to Server and Sending Nickname
def receive():

     while True:
            try:
                 # Receive Message From Server
                 # If 'NICK' Send Nickname
                  message = client.recv(1024).decode('ascii')
                  if message == 'NICK':
                     client.send(nickname.encode('ascii'))
                  else:
                     print(message)
            except:
                 # Close Connection When Error
                 print("An error occured!")
                 client.close()
                 break

# Sending Messages To Server
def write():
    while True:
               message = f'{nickname}: {input (" " )}'
               client.send(message.encode('ascii'))
               current = e.strftime("%H:%M:%S")
               print(current)

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
