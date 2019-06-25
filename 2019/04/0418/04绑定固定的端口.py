import socket

def main():
	# 创建套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	while  True:
		send_data = input("请输入您要发送的内容: ")
		if send_data == 'exit':
			break
		else:
			udp_socket.sendto(send_data.encode("utf-8"), ("192.168.1.109", 8080))


	# 关闭套接字
	udp_socket.close()



if __name__ == '__main__':
	main() 
