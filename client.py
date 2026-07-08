import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

username = input("Nom d'utilisateur : ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


def receive():
    while True:
        try:
            message = client.recv(1024).decode()

            if message == "USERNAME":
                client.send(username.encode())
            else:
                print(message)

        except:
            print("Connexion interrompue.")
            client.close()
            break


def write():
    while True:
        message = input("")
        client.send(f"{username} : {message}".encode())


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()