import tkinter as tk
import random

# Lisitry ny flashcards
flashcards = [
    {
        "question": "Qu'est-ce que Python ?",
        "answer": "Python est un langage de programmation."
    },
    {
        "question": "Que signifie HTML ?",
        "answer": "HyperText Markup Language."
    },
    {
        "question": "Que signifie CSS ?",
        "answer": "Cascading Style Sheets."
    },
    {
        "question": "Que signifie SQL ?",
        "answer": "Structured Query Language."
    },
    {
        "question": "Quel est le rôle d'un serveur ?",
        "answer": "Il fournit des services aux clients via un réseau."
    }
]

# Sélection aléatoire de la première question
carte = random.choice(flashcards)

# Fonction pour afficher la réponse
def afficher_reponse():
    lbl_reponse.config(text=carte["answer"])

# Fonction pour passer à une autre carte
def carte_suivante():
    global carte

    carte = random.choice(flashcards)

    lbl_question.config(text=carte["question"])
    lbl_reponse.config(text="")

# Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("Flashcards IA")
fenetre.geometry("600x350")

titre = tk.Label(
    fenetre,
    text="FLASHCARDS IA",
    font=("Arial", 20, "bold")
)

titre.pack(pady=15)

lbl_question = tk.Label(
    fenetre,
    text=carte["question"],
    font=("Arial", 14),
    wraplength=500
)

lbl_question.pack(pady=20)

btn_reponse = tk.Button(
    fenetre,
    text="Afficher la réponse",
    command=afficher_reponse
)

btn_reponse.pack()

lbl_reponse = tk.Label(
    fenetre,
    text="",
    font=("Arial", 13),
    fg="blue",
    wraplength=500
)

lbl_reponse.pack(pady=20)

btn_suivant = tk.Button(
    fenetre,
    text="Carte suivante",
    command=carte_suivante
)

btn_suivant.pack()

fenetre.mainloop()