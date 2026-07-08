import sqlite3
import tkinter as tk

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
SELECT utilisateur, question, reponse
FROM historique
""")

historique = cursor.fetchall()

conn.close()

fenetre = tk.Tk()
fenetre.title("Historique")
fenetre.geometry("700x400")

texte = tk.Text(fenetre)

texte.pack(fill="both", expand=True)

if len(historique) == 0:
    texte.insert(tk.END, "Aucun historique disponible.")
else:
    for utilisateur, question, reponse in historique:
        texte.insert(
            tk.END,
            f"Utilisateur : {utilisateur}\n"
            f"Question : {question}\n"
            f"Réponse : {reponse}\n"
            "-------------------------\n"
        )

fenetre.mainloop()