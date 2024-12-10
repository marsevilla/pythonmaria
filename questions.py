import random

# Exercise: quiz interactive
	# Possez des questions aléatoires sur Python.
	# Utilisez le module intégré random pour choisir des questions aléatoires.
	# Bonus: Comptez les réponses correctes.

# Avant de commencer posez votre analyse, définissez les étapes.

# 1. On défini les questions et les réponses
questions_reponses = {
    "Quelle fonction est utilisée pour afficher quelque chose dans la console en Python ?": "print",
    "Quel type de données est utilisé pour stocker du texte en Python ?": "str",
    "Comment définit-on une variable en Python ?": "variable = valeur",
    "Quel opérateur est utilisé pour comparer l'égalité en Python ?": "==",
    "Quel est l'indice initial d'une liste en Python ?": "0",
    "Quel mot-clé est utilisé pour définir une fonction en Python ?": "def",
    "Comment commence-t-on une boucle for en Python ?": "for",
    "Comment commente-t-on des lignes en Python ?": "#",
    "Quelle fonction est utilisée pour obtenir la longueur d'une liste ou d'une chaîne en Python ?": "len",
    "Quel est l'opérateur utilisé pour la division en Python ?": "/",
    "Quel est l'opérateur utilisé pour la multiplication en Python ?": "*",
    "Quel est l'opérateur utilisé pour la soustraction en Python ?": "-",
    "Quel est l'opérateur utilisé pour l'addition en Python ?": "+",
    "Quel est l'opérateur utilisé pour la puissance en Python ?": "**",
    "Quel est l'opérateur utilisé pour le modulo en Python ?": "%",
    "Quel est l'opérateur utilisé pour la division entière en Python ?": "//",
    "Quel est l'opérateur utilisé pour l'assignation en Python ?": "=",
    "Quel est l'opérateur utilisé pour la différence en Python ?": "!=",
}

# 2. On initialise les points
points = 0

# 3. On défini la fonction pour poser_questions
def poser_questions():
# 4. Variable de points qui va stocker les points de l'utilisateur
    global points
# 5. On choisit une question aléatoire
    question = random.choice(list(questions_reponses.keys()))
    print(f"\n{question}\n")
    reponse = input("Réponse : ")

# 6. On compare la réponse de l'utilisateur avec la réponse correcte
    if reponse == questions_reponses[question]:
        print("Bonne réponse")
        points += 1
    else:
        print(f"Mauvaise réponse. La bonne réponse était : {questions_reponses[question]}")

# 7. On affiche les points
    print(f"Vous avez {points} points.")

# 8. Boucle
def quiz():
    print("Bienvenue dans le quiz Python.")
    while True :
        poser_questions()
        continuer = input("Voulez-vous continuer ? (oui/non) : ")
        if continuer != "oui":
            print(f"Merci d'avoir joué ! Vous avez terminé avec {points} point(s).")
            break

# 9. On appelle la fonction quiz
quiz()
