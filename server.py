import socket

ip_address = '127.0.0.1'
port = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates ipv4 socket

s.bind((ip_address, port))

s.listen(2)

client_sock, address = s.accept()

msg = client_sock.recv(1024) # recieve certain num bytes

print(msg)

client_sock.close()
s.close()