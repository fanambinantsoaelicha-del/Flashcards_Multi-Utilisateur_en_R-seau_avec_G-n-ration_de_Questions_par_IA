===========================================
FLASHCARDS MULTI-UTILISATEUR EN RESEAU
===========================================

Auteur :
Nom de l'étudiant : ...................................

Technologies utilisées :
- Python 3
- Socket TCP
- Threading
- Tkinter
- SQLite
- Intelligence Artificielle (API OpenAI ou modèle local)

-------------------------------------------

DESCRIPTION

Cette application permet à plusieurs utilisateurs de se connecter sur un même serveur.

Les utilisateurs peuvent :

- Se connecter simultanément.
- Réviser avec des flashcards.
- Répondre à des questionnaires.
- Obtenir un score.
- Consulter leur historique.

Le serveur distribue les questions aux clients.

Les résultats sont enregistrés dans une base de données SQLite.

-------------------------------------------

FICHIERS

server.py
Le serveur principal.

client.py
Le client qui se connecte au serveur.

database.py
Gestion de SQLite.

flashcards.py
Gestion des flashcards.

ai_generator.py
Génération automatique des questions.

quiz.py
Gestion des questionnaires.

score.py
Calcul des scores.

classement.py
Classement des utilisateurs.

historique.py
Historique des sessions.

-------------------------------------------

LANCEMENT

1. Démarrer le serveur

python server.py

2. Démarrer un ou plusieurs clients

python client.py

-------------------------------------------

PORT

5000

-------------------------------------------

Auteur

Projet Réseau Python
Université