command_history = []
prompt = "shell> "
connections_dict = dict()

def shell_input(history, cmd_dict):
    command = input(prompt)
    while command != "quit":
        if command in cmd_dict:
            history.append(command)
            function = cmd_dict[command][0]
            args = cmd_dict[command][1]
            function(*args)
        else:
            print("Not a valid command.")
        command = input(prompt)
    return

def history(hist):
    print(f"{prompt}Command history: {hist}")
    return

def list_connections(connections_dict):
    for agent in connections_dict:
        print(f"{prompt}{agent}")
    return

command_dict = {"history": [history, [command_history]], "list": [list_connections, [connections_dict]]}

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
    shell_input(command_history, command_dict)
