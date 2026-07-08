import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS utilisateurs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS scores(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    utilisateur TEXT,
    score INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS historique(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    utilisateur TEXT,
    question TEXT,
    reponse TEXT
)
""")

conn.commit()

print("Base de données créée.")

conn.close()

cursor.execute("""
CREATE TABLE IF NOT EXISTS historique(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    utilisateur TEXT,
    question TEXT,
    reponse TEXT
)
""")