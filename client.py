import socket
import threading

HOST = "192.168.88.47"   # IP an'ilay serveur
PORT = 5001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((HOST, PORT))
    print("Connecté au serveur")
except Exception as e:
    print("Impossible de se connecter au serveur")
    print(e)
    exit()

username = input("Votre nom : ")

# Mandray hafatra avy amin'ny serveur
def receive():
    while True:
        try:
            message = client.recv(1024).decode()

            if message == "USERNAME":
                client.send(username.encode())
            else:
                print(message)

        except:
            print("Connexion fermée.")
            client.close()
            break

# Mandefa hafatra any amin'ny serveur
def send():
    while True:
        try:
            message = input()
            client.send(f"{username} : {message}".encode())
        except:
            client.close()
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()
