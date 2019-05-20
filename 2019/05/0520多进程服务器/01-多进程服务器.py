import socket
import re

def server_client(new_socket):
    request = new_socket.recv(1024).decode('utf-8')
    print('>>>'*10)
    # print(request)

    request_lines = request.splitlines()
    print('')

    print('>>'*20)
    print(request_lines)

    ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])

    if ret:
        file_name = ret.group(1)
        print('*'*20, file_name)

    try:
        f = open('./html' + file_name, 'rb')
    except:
        response = 'HTTP/1.1 404 NOT FOUND\r\n'

        response += '\r\n'
        new_socket.send(response.encode('utf-8'))
    else:
        html_content = f.read()
        f.close()

        response = 'HTTP/1.1 200 OK\r\n'
        response += '\r\n'
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

        new_socket.close() # 多进程开辟新的进程要进行关闭

    tcp_server.close()

if __name__ == '__main__':
    main()