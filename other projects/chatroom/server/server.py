import socket
import threading
import json
import datetime
from colorama import Fore, init

init()

# Server configuration
HOST = ''
PORT = 7976
PASSWORD_FILE = 'password.json'

# Global data structures
clients = []
nicknames = []
last_message_per_user = {}

# Load passwords from JSON file
with open(PASSWORD_FILE, 'r') as file:
    passwords = json.load(file)

# Function to log messages to a file
def log_message(message):
    now_text = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("log.log", 'a') as f:
        f.write("[" + now_text + "] | " + message.strip("'") + '\n')

# Function to broadcast a message to all clients
def broadcast(message):
    log_message(message)
    for client in clients:
        client.send(message)

# Function to handle a client connection
def handle_client(client):
    while True:
        try:
            now = datetime.datetime.timestamp(datetime.datetime.now())
            diff = now - last_message_per_user[client]

            message = client.recv(1024)
            if message:
                msg = message.decode().split(' ')
                last_message_per_user[client] = datetime.datetime.timestamp(datetime.datetime.now())
                if msg[1] == '/ping':
                    client.send(f'{Fore.RED}[*] - TG TU EST GAY - [*]'.encode())
                elif msg[1] == '/online':
                    online_users = ', '.join(nicknames)
                    online_users_message = (
                        f'{Fore.GREEN}\n---------------------------------\n'
                        f'Online: {online_users}\n'
                        f'---------------------------------\n'
                        f'Online Count: {len(clients)}\n'
                    )
                    client.send(online_users_message.encode())
                else:
                    now_text = datetime.datetime.now().strftime("%H:%M")
                    print(message)
                    message_text = f'{Fore.GREEN}[{now_text}] ' + message.decode()
                    broadcast(message_text.encode())
            else:
                client.send(f'{Fore.RED}[*]'.encode())
        except Exception as e:
            print(f"An error occurred: {e}")
            break

# Function to accept and authenticate client connections
def accept_clients(server):
    while True:
        print(f'[{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}] {Fore.GREEN}[INFO]: Server is running and listening ...')
        client, address = server.accept()
        print(f"{Fore.GREEN}[CONNECTION]{Fore.RESET}" + ": Connected with {}".format(str(address)))

        client.send('NICKNAME'.encode())
        nickname = client.recv(1024).decode()
        password = client.recv(1024).decode()

        if nickname in passwords:
            if passwords[nickname] == password:
                nicknames.append(nickname)
                last_message_per_user[client] = datetime.datetime.timestamp(datetime.datetime.now())
                clients.append(client)
                print(f"{Fore.BLUE}[NICK] : Nickname is {Fore.RED}" + '{}'.format(nickname) + rf"{Fore.RESET}")
                welcome_message = f'{Fore.GREEN}[*] - [{nickname}] : {nickname} joined the channel !'.format(nickname)
                broadcast(welcome_message.encode())
                client.send('[INFO] : Connected to server!'.encode())

                thread = threading.Thread(target=handle_client, args=(client,))
                thread.start()
            else:
                client.send(f"{Fore.RED}Wrong password".encode())
        else:
            client.send(f"{Fore.RED}Wrong Username".encode())

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    accept_thread = threading.Thread(target=accept_clients, args=(server,))
    accept_thread.start()
