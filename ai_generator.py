import random

questions = [

    ("Qu'est-ce que Python ?",
     "Python est un langage de programmation."),

    ("Que signifie HTML ?",
     "HyperText Markup Language."),

    ("Que signifie CSS ?",
     "Cascading Style Sheets."),

    ("Quel est le rôle d'un serveur ?",
     "Il répond aux demandes des clients.")
]

def generer_question():

    return random.choice(questions)


if __name__ == "__main__":

    q, r = generer_question()

    print("Question :", q)
    print("Réponse :", r)