import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '192.168.6.4'
port = 8889

server.connect((host,port))

file = open("sample.txt", "rb")
SendData = file.read(1024)

while True:

    sockets_list = [sys.stdin, server]
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])

    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            print (message)
        else:
            message = sys.stdin.readline()
            server.send(message.encode())
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
           # while SendData:
                  # server.send(SendData)
                  # SendData = file.read(1024) 
                  # print("\n\n################## File Transfer Status from server ################## \n\n ", server.recv(1024).decode("utf-8"))
server.close()
