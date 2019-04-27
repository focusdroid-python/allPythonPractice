import socket


def send_msg(udp_socket):
    """发送消息"""
    dest_ip = input('请输入对方的ip: ')
    dest_port = int(input('请输入对方的端口: '))
    send_data = input('请输入需要发送的内容: ')
    # 发数据
    udp_socket.sendto(send_data.encode('utf-8'), (dest_ip, dest_port))

def recv_msg(udp_socket):
    """接收数据"""
    recv_data = udp_socket.recvfrom(1024)
    print('%s : %s' % (recv_data[1], recv_data[0].decode('utf-8')))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定端口
    udp_socket.bind(('', 7788))

    while True:
        print('收发消息--------')
        op = input('请输入功能: ')
        if op == '1':
            # 发数据
            send_msg(udp_socket)
        elif op == '2':
            # 接受数据并显示
            recv_msg(udp_socket)
        else:
            print('输入有误!')


if __name__ == '__main__':
    main()