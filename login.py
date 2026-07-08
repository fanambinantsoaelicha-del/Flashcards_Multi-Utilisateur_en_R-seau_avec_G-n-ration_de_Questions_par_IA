import sqlite3

def login():

    nom = input("Entrez votre nom : ")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT OR IGNORE INTO utilisateurs(nom) VALUES(?)",
        (nom,)
    )

    conn.commit()
    conn.close()

    print(f"Bienvenue {nom} !")

    return nom


if __name__ == "__main__":
    login()