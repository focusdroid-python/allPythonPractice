import socket



def send_file_2_client(new_client_socket, client_addr):
    # 接收客户端发送的来的, 要下载的文件名
    file_name = new_client_socket.recv(1024).decode('utf-8')
    print('客户端(%s)下载的文件:%s' % (str(client_addr), file_name))

    file_content = None

    # 打开这个文件,读取数据
    try:
        f = open(file_name, 'rb')
        file_content = f.read()
        f.close()
    except Exception as ret:
        print('没有要下载的文件%s' % file_name)
    if file_content:
        # 发送数据给客户端
        new_client_socket.send(file_content)

def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    tcp_server_socket.bind(('', 8888))

    tcp_server_socket.listen(128) # listen中的128有一部分关系影响服务器

    while True:
        new_client_socket, client_addr = tcp_server_socket.accept()

        send_file_2_client(new_client_socket, client_addr)

        new_client_socket.close()
    tcp_server_socket.close()

if __name__ == '__main__':
    main()