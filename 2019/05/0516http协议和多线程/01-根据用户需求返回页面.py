import socket
import re

def server_client(new_socket):
    request = new_socket.recv(1024)
    print('>>>'*10)
    print(request)

    response = 'HTTP/1.1 200 OK\r\n'
    response += '\r\n'


    f = open('./html/index.html', 'rb')
    html_content = f.read()
    f.close()

    # 将response headers发送给用户
    new_socket.send(response.encode('utf-8'))
    # 将response body发送给用户
    new_socket.send(html_content)

    new_socket.close()

def main():
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    tcp_server.bind(('', 7890))

    tcp_server.listen(128)

    while True:
        new_socket, client_addr = tcp_server.accept()

        server_client(new_socket)

    tcp_server.close()

if __name__ == '__main__':
    main()