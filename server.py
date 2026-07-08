import socket
import threading

HOST = "0.0.0.0"
PORT = 5000

clients = []
usernames = []


def broadcast(message):
    for client in clients:
        client.send(message.encode())


def handle(client):

    while True:

        try:

            message = client.recv(1024).decode()

            if not message:
                break

            print(message)

            broadcast(message)

        except:
            index = clients.index(client)

            clients.remove(client)

            client.close()

            username = usernames[index]

            usernames.remove(username)

            broadcast(f"{username} a quitté le serveur.")

            break


def receive():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((HOST, PORT))

    server.listen()

    print("Serveur lancé...")

    while True:

        client, address = server.accept()

        print("Nouvelle connexion :", address)

        client.send("USERNAME".encode())

        username = client.recv(1024).decode()

        usernames.append(username)

        clients.append(client)

        print(username, "connecté.")

        broadcast(f"{username} a rejoint le serveur.")

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()