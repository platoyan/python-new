from socket import socket
from socket import AF_INET
from socket import SOCK_STREAM
from time import ctime

HOST = '11.205.240.93'
PORT = 8080
BUFFERSIZE = 1024
ADDRESS = (HOST, PORT)


def create_server_socket():
    """创建一个服务端Sockett,并且监听本地5257端口
    """
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.bind(ADDRESS)
    # 设置最大连接数为10
    tcp_socket.listen(10)
    # tcp_socket.setblocking(False)
    return tcp_socket


def server_socket_start_work(server_tcp_socket):
    """服务端开始工作
    """
    print("等待客户端的链接")
    while True:
        tcp_client_socket, addr = server_tcp_socket.accept()
        print("有客户端连接")
        print(addr)
        # 接收发送的数据
        while True:
            data = tcp_client_socket.recv(BUFFERSIZE)
            if not data:
                break
            print(data)
            tcp_client_socket.send(bytes('[%s] %s' % (ctime(), data), encoding='utf-8'))
            # tcp_client_socket.close()
    server_tcp_socket.close()

if __name__ == '__main__':
    server_socket = create_server_socket()
    server_socket_start_work(server_socket)