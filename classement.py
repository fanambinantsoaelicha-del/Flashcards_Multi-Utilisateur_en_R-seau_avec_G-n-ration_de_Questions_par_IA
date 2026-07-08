import sqlite3
import tkinter as tk

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
SELECT utilisateur,
MAX(score)
FROM scores
GROUP BY utilisateur
ORDER BY MAX(score) DESC
""")

classement = cursor.fetchall()

conn.close()

fenetre = tk.Tk()
fenetre.title("Classement")
fenetre.geometry("400x300")

titre = tk.Label(
    fenetre,
    text="CLASSEMENT",
    font=("Arial", 18, "bold")
)

titre.pack(pady=10)

for i, (utilisateur, score) in enumerate(classement, start=1):

    texte = tk.Label(
        fenetre,
        text=f"{i}. {utilisateur} : {score} points",
        font=("Arial", 12)
    )

    texte.pack()

fenetre.mainloop()