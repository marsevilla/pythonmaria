import pyjokes

#Déclarer la fonction
def joke():
    joke = pyjokes.get_joke()
    print(f"Voici une blague pour vous :\n{joke}\n")

#Appeler la fonction
joke()
