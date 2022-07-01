import time, socket, sys

socket_server = socket.socket()
server_host = ''
ip = '192.168.6.6'
sport = 8889

print('This is your IP address: ',ip)
server_host = input('Enter friend\'s IP address:')
FriendsName = input('Enter your friend\'s name: ')
name = input('Enter your name: ')


socket_server.connect((server_host, sport))

socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(server_name,' has joined...')
while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name, ":", message)
    message = input("Me : ")
    socket_server.send(message.encode())
