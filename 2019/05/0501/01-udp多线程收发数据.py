import socket
import threading

def recv_msg(udp_socket):
    ''''''
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)

def send_data(udp_socket):
    while True:
        send_data = input('输入您要发送的数据： ')
        udp_socket.sendto(send_data.encode('gbk'), ('192.168.1.109', 8080))


def main():
    '''完成udp聊天器的整体控制'''
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_socket.bind(('', 7890))

    t1 = threading.Thread(target=recv_msg, args=(udp_socket,))
    t2 = threading.Thread(target=send_data, args=(udp_socket,))


    t1.start()
    t2.start()





if __name__ == '__main__':
    main()