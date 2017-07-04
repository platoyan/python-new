from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
HOST = '11.205.240.93'
PORT = 8080
BUFFERSIZE = 1024
ADDRESS = (HOST, PORT)

tcp_client_socket = socket(AF_INET, SOCK_STREAM)
tcp_client_socket.connect(ADDRESS)

while True:
    data = input(">")
    if not data:
        break
    tcp_client_socket.send(bytes(data, encoding="utf-8"))
    data = tcp_client_socket.recv(BUFFERSIZE)
    if not data:
        break
    print(data)
tcp_client_socket.close()