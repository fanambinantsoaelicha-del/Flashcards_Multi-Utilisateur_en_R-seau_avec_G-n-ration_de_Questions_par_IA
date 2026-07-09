import socket
import threading
import tkinter as tk
from tkinter import scrolledtext


HOST = "192.168.88.47"   # IP an'ny serveur
PORT = 5001


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((HOST, PORT))
except:
    print("Impossible de se connecter au serveur")
    exit()


username = input("Votre nom : ")


def receive():
    while True:
        try:
            message = client.recv(1024).decode()

            if message == "USERNAME":
                client.send(username.encode())

            else:
                chat_area.config(state="normal")
                chat_area.insert(tk.END, message + "\n")
                chat_area.config(state="disabled")
                chat_area.yview(tk.END)

        except:
            break


def send_message():
    message = message_entry.get()

    if message:
        message = username + " : " + message
        client.send(message.encode())
        message_entry.delete(0, tk.END)


# Fenêtre principale
window = tk.Tk()
window.title("Chat Application")
window.geometry("500x500")


# Zone affichage message
chat_area = scrolledtext.ScrolledText(
    window,
    state="disabled",
    width=50,
    height=25
)

chat_area.pack(pady=10)


# Zone écriture
message_entry = tk.Entry(
    window,
    width=40
)

message_entry.pack(side=tk.LEFT, padx=10)


# Bouton envoyer
send_button = tk.Button(
    window,
    text="Envoyer",
    command=send_message
)

send_button.pack(side=tk.RIGHT, padx=10)


# Thread réception
receive_thread = threading.Thread(target=receive)
receive_thread.daemon = True
receive_thread.start()


window.mainloop()