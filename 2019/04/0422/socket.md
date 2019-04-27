### socket发送数据和接收数据过程
> 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    % 端口号不能再电脑里边相同 %
    localAddress('192.168.1.109', 8800)
    udp_socket.bind()
> 2. 使用套接字收发数据
    udp_socket.sendto('xxxx', (ip, 端口))
    udp_socket.recvfrom(1024)
> 3. 关闭套接字
    udp_socket.close()
    
#### 一个收发消息(同时收发)
> 0. 创建一个套接字\


%& 一个套接字可以同时收发的
%& 



单工

半双工

全双工(socket)