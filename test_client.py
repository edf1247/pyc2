import socket 

HOST = "127.0.0.1" 
PORT = 4444

def main(): 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    client_socket.connect((HOST, PORT))
    
    client_message = "Hello world"
    client_socket.send(client_message.encode()) 

    while True:
        try:
            message = "Test"

            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)          # Receive data
            if not data:
                print("Server disconnected.")
                break
            print(f"Received from server: {data.decode()}")
        except ConnectionRefusedError:
            print("Connection refused. Server might not be running.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break   

main() 
