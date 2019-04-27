import socket

def main():
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.绑定端口
    localaddress = ('', 8888)
    udp_socket.bind(localaddress)

    # 3.循环接收发送数据
    while True:
        # 3.1 每次接收1024kb的数据,一般情况下1024,再多的话或导致传输问题
        recv_msg = udp_socket.recvfrom(1024)
        recv_content = recv_msg[0]
        recv_ip = recv_msg[1]
        if recv_content.decode('gbk') == 'exit':
            return
        else:
            print('%s : %s' % (recv_ip[0], recv_content.decode('gbk')))





    udp_socket.close()

if __name__ == '__main__':
    main()