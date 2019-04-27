import socket


def main():
    # 创建tcp链接
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('tcp_server创建成功')

    # 端口绑定(因为是服务端,所以要固定端口)
    tcp_server.bind(('', 9999))
    print('端口绑定成功')

    # 监听端口
    tcp_server.listen(128)
    print('监听端口成功')

    while True:
        # 等待客户端连接,若果没有客户端链接,就会发生阻塞这里
        new_client_socket, client_addr = tcp_server.accept()
        print('客户端连接成功')

        print(new_client_socket)
        print(client_addr)

        while True:
            # 客户端发送过来的请求
            recv_data = new_client_socket.recv(1024)
            # 打印客户端发送过来的内容
            print('客户端发送过来的内容: %s'% recv_data.decode('utf-8'))

            new_client_socket.send('有什么需要帮助的吗?'.encode('utf-8'))
            print('单次服务器相应完成')

    # 单个客户端服务关闭
    new_client_socket.close()
    # 整个服务器关闭
    tcp_server.close()


if __name__ == '__main__':
    main()