import sqlite3

def enregistrer_score(utilisateur, score):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO scores(utilisateur, score)
        VALUES(?, ?)
    """, (utilisateur, score))

    conn.commit()
    conn.close()


def afficher_scores():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT utilisateur, score
        FROM scores
        ORDER BY score DESC
    """)

    resultats = cursor.fetchall()

    conn.close()

    return resultats


if __name__ == "__main__":

    scores = afficher_scores()

    for utilisateur, score in scores:
        print(utilisateur, ":", score)