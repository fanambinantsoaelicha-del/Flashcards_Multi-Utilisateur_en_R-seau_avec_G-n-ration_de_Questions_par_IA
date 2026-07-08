import tkinter as tk
from tkinter import messagebox
from score import enregistrer_score

utilisateur = input("Nom du joueur : ")

questions = [

    {
        "question": "Python est un ... ?",
        "choix": ["Navigateur", "Langage", "Jeu"],
        "reponse": "Langage"
    },

    {
        "question": "HTML signifie ... ?",
        "choix": [
            "HyperText Markup Language",
            "Home Tool Markup Language",
            "Hyper Transfer"
        ],
        "reponse": "HyperText Markup Language"
    },

    {
        "question": "CSS sert à ... ?",
        "choix": [
            "Créer le style",
            "Créer la base",
            "Créer le serveur"
        ],
        "reponse": "Créer le style"
    }

]

numero = 0
score = 0


def verifier():

    global numero
    global score

    reponse = variable.get()

    if reponse == questions[numero]["reponse"]:
        score += 1

    numero += 1

    if numero == len(questions):

        enregistrer_score(utilisateur, score)

        messagebox.showinfo(
            "Résultat",
            f"Votre score est : {score}/{len(questions)}"
        )

        fenetre.destroy()

    else:
        afficher_question()


def afficher_question():

    question.config(text=questions[numero]["question"])

    variable.set(None)

    for i in range(3):
        boutons[i].config(
            text=questions[numero]["choix"][i],
            value=questions[numero]["choix"][i]
        )


fenetre = tk.Tk()

fenetre.title("Quiz Flashcards IA")
fenetre.geometry("500x350")

question = tk.Label(
    fenetre,
    font=("Arial", 14)
)

question.pack(pady=20)

variable = tk.StringVar()

boutons = []

for i in range(3):

    rb = tk.Radiobutton(
        fenetre,
        variable=variable,
        value="",
        font=("Arial", 12)
    )

    rb.pack(anchor="w")

    boutons.append(rb)

btn = tk.Button(
    fenetre,
    text="Suivant",
    command=verifier
)

btn.pack(pady=20)

afficher_question()

fenetre.mainloop()