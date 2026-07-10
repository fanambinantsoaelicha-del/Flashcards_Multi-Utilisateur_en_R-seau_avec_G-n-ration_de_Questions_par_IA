import socket
import threading


HOST = "0.0.0.0"
PORT = 5001


flashcards = [
    {
        "question": "Qu'est-ce que Python ?",
        "answer": "langage de programmation"
    },
    {
        "question": "Qu'est-ce que HTML ?",
        "answer": "langage de balisage"
    },
    {
        "question": "Qu'est-ce que SQL ?",
        "answer": "base de donnees"
    }
]


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen()

print("Serveur démarré...")
print("En attente d'un client...")


def handle(client):

    score = 0


    try:

        for card in flashcards:

            # Envoyer question
            client.send(
                card["question"].encode()
            )


            # Recevoir réponse
            response = client.recv(1024).decode().lower()


            # Vérification
            if card["answer"] in response:

                score += 1

                message = "Correct !"

            else:

                message = (
                    "Faux ! Bonne réponse : "
                    + card["answer"]
                )


            client.send(
                message.encode()
            )


        # Score final

        final = (
            "FINI\n"
            "Votre score final : "
            + str(score)
            + "/"
            + str(len(flashcards))
        )


        client.send(
            final.encode()
        )


    except:

        print("Client déconnecté")


    finally:

        client.close()



while True:

    client, address = server.accept()

    print(
        "Nouveau client :",
        address
    )


    thread = threading.Thread(
        target=handle,
        args=(client,)
    )

    thread.start()