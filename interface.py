import tkinter as tk
from tkinter import messagebox
import subprocess
import sqlite3


def connexion():

    nom = entree.get().strip()

    if nom == "":
        messagebox.showerror("Erreur", "Veuillez entrer votre nom.")
        return

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT OR IGNORE INTO utilisateurs(nom) VALUES(?)",
        (nom,)
    )

    conn.commit()
    conn.close()

    fenetre.destroy()

    menu_principal(nom)


def ouvrir_flashcards():
    subprocess.Popen(["python", "flashcards.py"])


def ouvrir_quiz():
    subprocess.Popen(["python", "quiz.py"])


def ouvrir_historique():
    subprocess.Popen(["python", "historique.py"])


def ouvrir_classement():
    subprocess.Popen(["python", "classement.py"])


def menu_principal(nom):

    menu = tk.Tk()

    menu.title("Flashcards IA")

    menu.geometry("400x420")

    titre = tk.Label(
        menu,
        text="FLASHCARDS IA",
        font=("Arial", 20, "bold")
    )

    titre.pack(pady=20)

    bienvenue = tk.Label(
        menu,
        text=f"Bienvenue {nom}",
        font=("Arial", 13)
    )

    bienvenue.pack(pady=10)

    tk.Button(
        menu,
        text="Flashcards",
        width=25,
        command=ouvrir_flashcards
    ).pack(pady=5)

    tk.Button(
        menu,
        text="Quiz",
        width=25,
        command=ouvrir_quiz
    ).pack(pady=5)

    tk.Button(
        menu,
        text="Historique",
        width=25,
        command=ouvrir_historique
    ).pack(pady=5)

    tk.Button(
        menu,
        text="Classement",
        width=25,
        command=ouvrir_classement
    ).pack(pady=5)

    tk.Button(
        menu,
        text="Quitter",
        width=25,
        command=menu.destroy
    ).pack(pady=20)

    menu.mainloop()


fenetre = tk.Tk()

fenetre.title("Connexion")

fenetre.geometry("350x220")

tk.Label(
    fenetre,
    text="FLASHCARDS IA",
    font=("Arial", 18, "bold")
).pack(pady=20)

tk.Label(
    fenetre,
    text="Nom d'utilisateur"
).pack()

entree = tk.Entry(fenetre)

entree.pack(pady=10)

tk.Button(
    fenetre,
    text="Connexion",
    command=connexion
).pack()

fenetre.mainloop()