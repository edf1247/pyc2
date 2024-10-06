import socket

ip_address = '127.0.0.1'
port = 4444

cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates ipv4 socket

cs.connect((ip_address, port))

msg = "Hello World"

cs.send(msg.encode())

cs.close()
