import socket

def main():
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 手动输入对方的ip
    dest_ip = input('请输入对方IP: ')
    # 手动输入对方端口
    dest_port = int(input('请输入对方端口号: '))
    while True:
        send_data = input('请输入您要发送的内容: ')
        if send_data == 'exit':
            udp_socket.close()
            return
        else:
            # 发送数据
            # udp_socket.sendto(send_data.encode('gbk'), ('192.168.42.95', 8080))
            udp_socket.sendto(send_data.encode('utf-8'), (dest_ip, dest_port))

            recv_data = udp_socket.recvfrom(1024)

            print(recv_data)

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()