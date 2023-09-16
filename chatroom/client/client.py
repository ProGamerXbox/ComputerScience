import socket
import threading
import sys
import datetime
import getpass  # For password input
from colorama import Fore, init
from pythonping import ping

if sys.platform == "win32":
    import msvcrt
else:
    print("I don't know how to make it for Linux, maybe one day I'll work on it")

init()

# Constants for chat colors
USERNAME_COLOR = Fore.CYAN
SYSTEM_MESSAGE_COLOR = Fore.YELLOW
OTHER_USER_MESSAGE_COLOR = Fore.RESET

# Constants for commands
PING_COMMAND = '/ping'
EXIT_COMMAND = '/exit'

def clear_line():
    print("\033[A\033[K", end="")  # Clear the current line in the terminal

def print_system_message(message):
    print(f"{SYSTEM_MESSAGE_COLOR}[SYSTEM]: {message}{Fore.RESET}")

def get_user_input(prompt=""):
    if sys.platform == "win32":
        return input(prompt)
    else:
        return input(prompt)

def connect_to_server(ip, port):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((ip, port))
        return client
    except Exception as e:
        print_system_message(f"Failed to connect to the server: {e}")
        sys.exit(1)

def send_message(client, message):
    try:
        client.send(message.encode())
    except Exception as e:
        print_system_message(f"Failed to send message: {e}")

def receive_messages(client, username):
    try:
        while True:
            message = client.recv(1024).decode()
            if not message:
                print_system_message("Disconnected from the server.")
                client.close()
                break
            print_message(message, username)
    except Exception as e:
        print_system_message(f"An error occurred while receiving messages: {e}")

def print_message(message, username):
    if message.startswith("[SYSTEM]"):
        print_system_message(message)
    elif message.startswith(f"[{username}]"):
        clear_line()
        print(f"{USERNAME_COLOR}{message}{Fore.RESET}")
    else:
        clear_line()
        print(f"{OTHER_USER_MESSAGE_COLOR}{message}{Fore.RESET}")

def main():
    ip = input(f"{Fore.CYAN}Server IP address: {Fore.RESET}")
    port = 7976
    username = input(f"{Fore.CYAN}Username: {Fore.RESET}")
    password = getpass.getpass(f"{Fore.CYAN}Password (if required): {Fore.RESET}")

    client = connect_to_server(ip, port)

    # Send the username and password (if provided) to the server for authentication
    send_message(client, username)
    send_message(client, password)

    # Start a thread to receive messages from the server
    receive_thread = threading.Thread(target=receive_messages, args=(client, username))
    receive_thread.daemon = True
    receive_thread.start()

    while True:
        message = get_user_input()
        if message.lower() == PING_COMMAND:
            response_list = ping(ip, size=32, count=3)
            print_system_message(f"Ping to {ip}: {response_list.rtt_avg_ms} ms")
        elif message.lower() == EXIT_COMMAND:
            send_message(client, f"{EXIT_COMMAND} {username}")
            client.close()
            break
        else:
            send_message(client, message)

if __name__ == "__main__":
    main()
