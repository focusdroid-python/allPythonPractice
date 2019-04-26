import socket

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    localaddress = ('', 9999)
    udp_socket.bind(localaddress)
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data[0].decode('gbk'))

    udp_socket.close()


if __name__ == '__main__':
    main()