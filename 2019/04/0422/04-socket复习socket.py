import socket

def main():
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        send_data = input('请输入您要发送的内容: ')
        if send_data == 'exit':
            return
        else:
            #2. 绑定端口发送套接字
            udp_socket.sendto(send_data.encode('gbk'), ('192.168.43.95', 8080))

    #3. 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()