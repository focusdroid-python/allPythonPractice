tcp_server_socket = socket(.....)

tcp_server_socket.setblocking(False) # 设置套接字为非阻塞的方式

client_socket_list = list()


while True:
    try:
        new_socket, new_addr = tcp_server_socket.accept()
    except Exception as ret:
        print('----没有新客户端到来----')
    else:
        print('----只要没有产生异常，那么就表示来了一个新客户端')
        new_socket.serblocking(False)
        client_socket_list.append(new_socket)

    for client_socket in client_socket_list:
        try:
            client_socket.recv()
        except Exception as ret:
            print('----这个客户端没有发送数据----')
        else:
            print('-----客户端发送过来新数据----')