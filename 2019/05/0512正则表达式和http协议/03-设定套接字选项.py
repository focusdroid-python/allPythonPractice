import socket

def service_client(new_socket):
    # 1. 接收浏览器发送过来的请求
    # GET / HTTP/1.1
    # ...
    request = new_socket.recv(1024)
    print(request)

    # 2. 返回http格式的数据，给浏览器
    # 2。1 准备给浏览器的数据
    response = 'HTTP/1.1 200 OK\r\n'
    response += '\r\n'
    # 2.2 准备发送给浏览器的数据
    response += "<h1>这是一段测试文字，由服务端发送过来的</h1>"
    new_socket.send(response.encode('gbk'))

    new_socket.close()


def main():
    '''整体流程'''
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 保证端口不会因为中断而不可使用的情况
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SOREUSEADDR, 1)

    # 2. 绑定
    tcp_server_socket.bind(('', 7890))

    # 3. 监听套接字
    tcp_server_socket.listen(128)
    while True:
        # 4. 等待新客户端的链接
        new_socket, client_addr = tcp_server_socket.accept()

        # 5. 为这个客户端服务
        service_client(new_socket)

    tcp_server_socket.close()

if __name__ == '__main__':
    main()