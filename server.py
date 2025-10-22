import socket
import threading
from datetime import datetime

command_history = []
prompt = "shell> "
connections_dict = dict()
port = 4444
ip_addr = "127.0.0.1"


def shell_input(history, cmd_dict, stop_event):
    user_input = input(prompt)
    split_input = user_input.split(" ")
    command = split_input[0]
    
    while command != "quit":
        if command in cmd_dict:
            history.append(command)
            function = cmd_dict[command][0]
            args = cmd_dict[command][1]
            if len(split_input) == 1:
                function(*args)
            else:
                user_args = split_input[1:]
                function(*args, *user_args)
        else:
            print("Not a valid command.")
        user_input = input(prompt)
        split_input = user_input.split(" ")
        command = split_input[0]
    stop_event.set()
    return

def history(hist):
    print(f"{prompt}Command history: {hist}")
    return

def list_connections(connections_dict):
    for agent in connections_dict:
        print(f"{prompt}{agent}")
    return

def kill_agent(connections_dict, agent_id):
    if agent_id in connections_dict:
        connections_dict[agent_id].close()
        print(f"{prompt}{agent_id} killed.")
        del connections_dict[agent_id]
    else:
        print(f"Invalid agent id.")

def start_server(host, port, stop_event):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    server.settimeout(0.5)
    print(f"{prompt}Listening on {host}:{port}")
    try:
        while not stop_event.is_set():
            try:    
                conn, addr = server.accept()
            except socket.timeout:
                continue
            except OSError:
                break
            else:
                print(f"{prompt}Connection recieved from {addr}")
                agent_id = "agent_" + addr[0] + ":" + str(addr[1])
                connections_dict[agent_id] = conn 
    finally:
        server.close()
        print("Server shutting down.")

command_dict = {}

def help_menu():
    print("Help menu:")
    for key in command_dict.keys():
        print(f"> {key}")

command_dict = {"kill": [kill_agent, [connections_dict]],"help": [help_menu, []],"history": [history, [command_history]], "list": [list_connections, [connections_dict]], "quit": 0}

def welcome_message():
    banner = "=" * 77
    message = r"""
 _    _      _                            _         ______      _____  _____ 
| |  | |    | |                          | |        | ___ \    /  __ \/ __  \
| |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___   | |_/ /   _| /  \/`' / /'
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  |  __/ | | | |      / /  
\  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |  | |_| | \__/\./ /___
 \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  \_|   \__, |\____/\_____/
                                                           __/ |             
                                                          |___/              
"""
    print(banner)
    print(message)
    print(banner)



if __name__ == "__main__":
    welcome_message()
    stop_event = threading.Event()
    server_thread = threading.Thread(target=start_server, args=(ip_addr, port, stop_event))
    input_thread = threading.Thread(target=shell_input, args=(command_history, command_dict, stop_event))
    server_thread.start()
    input_thread.start()

    server_thread.join()
    input_thread.join()
