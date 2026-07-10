import socket
import threading


HOST = "192.168.88.47"   # IP serveur
PORT = 5001


# Création connexion
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((HOST, PORT))
    print("Connecté au serveur")
except:
    print("Impossible de se connecter au serveur")
    exit()


# Nom utilisateur
username = input("Votre nom : ")


# Réception message
def receive():
    while True:
        try:
            message = client.recv(1024).decode()

            if message == "USERNAME":
                client.send(username.encode())

            else:
                print(message)

        except:
            print("Connexion fermée")
            client.close()
            break



# Envoi message
def write():
    while True:
        message = input()

        if message != "":
            message = username + " : " + message
            client.send(message.encode())



# Thread réception
receive_thread = threading.Thread(
    target=receive
)

receive_thread.start()


# Thread envoi
write_thread = threading.Thread(
    target=write
)

write_thread.start()