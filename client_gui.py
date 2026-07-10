import socket
import threading
import tkinter as tk


HOST = "192.168.88.47"
PORT = 5001


client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)


try:

    client.connect(
        (HOST, PORT)
    )

    print("Connecté au serveur")


except:

    print("Connexion impossible")
    exit()



def receive():

    while True:

        try:

            message = client.recv(1024).decode()


            if message.startswith("FINI"):

                question_label.config(
                    text="Terminé !"
                )

                result_label.config(
                    text=message,
                    font=("Arial", 16)
                )


                answer_entry.config(
                    state="disabled"
                )

                validate_button.config(
                    state="disabled"
                )


            elif message.startswith("Correct") or message.startswith("Faux"):

                result_label.config(
                    text=message
                )


            else:

                question_label.config(
                    text=message
                )



        except:

            break




def send_answer():

    answer = answer_entry.get()


    if answer:

        client.send(
            answer.encode()
        )


        answer_entry.delete(
            0,
            tk.END
        )




# =====================
# Interface graphique
# =====================


window = tk.Tk()

window.title(
    "Flashcards IA"
)

window.geometry(
    "500x400"
)



question_label = tk.Label(
    window,
    text="Question",
    font=("Arial",16),
    wraplength=400
)

question_label.pack(
    pady=30
)



answer_entry = tk.Entry(
    window,
    width=40
)

answer_entry.pack()



validate_button = tk.Button(
    window,
    text="Valider",
    command=send_answer
)

validate_button.pack(
    pady=20
)



result_label = tk.Label(
    window,
    text="",
    font=("Arial",12)
)

result_label.pack()



receive_thread = threading.Thread(
    target=receive
)

receive_thread.daemon = True

receive_thread.start()



window.mainloop()
