import socket
import select
import sys
import os
from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host = ''
port = 8889

try:
    server.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waiting for a Connection..')
server.listen(50)

#file = open("recv.txt", "wb")
list_of_clients = []

def threaded_client(conn, addr):
    conn.send(str.encode('Welcome to this chatroom!\n'))
    while True:
            try:
                message = conn.recv(2048)
                if message:
                    print("<" + addr[0] + "> " + message)
                    message_to_send = "<" + addr[0] + "> " + message
                    broadcast(message_to_send, conn)


                    #RecvData = conn.recv(1024)
                    #while RecvData:
                         #file.write(RecvData)
                         #RecvData = conn.recv(1024)

                    #file.close()
                    #print("\n File has been copied successfully \n")

                else:
                    """message may have no content if the connection
                    is broken, in this case we remove the connection"""
                    remove(conn)

            except:
                continue

def broadcast(message, connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
               clients.send(message)
            except:
                clients.close()

                remove(clients)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:

    conn, addr  = server.accept()

    list_of_clients.append(conn)

    print (addr[0] + " connected")

    start_new_thread(threaded_client,(conn,addr))

conn.close()
server.close()
