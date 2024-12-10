# On va créer la class livre avec ses attributs
class Livre:
    # Utilisation de __init__ pour initialiser les attributs
    def __init__(self, titre, auteur, date):
        self.titre = titre
        self.auteur = auteur
        self.date = date

    # Utilisation de __str__ pour afficher les attributs
    # On va afficher le titre, l'auteur et l'année
    def __str__(self):
        return f"{self.titre}, écrit par {self.auteur} en {self.date}"

# Notre methode
def bibliotheque():
    # On va créer une liste pour stocker les livres
    livres = []
    # On va presenter les options dans notre menu
    while True:
        print("\nMenu :")
        print("1. Ajouter un livre")
        print("2. Afficher les livres")
        print("3. Rechercher un livre par titre")
        print("4. Eliminer un livre")
        print("5. Quitter")

        # utilisations de try et except pour gerer les erreurs
        try:
        # On va recuperer la reponse de l'utilisateur
            choix = int(input("\nChoix :"))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        # AJOUTER un livre
        if choix == 1:
            try:
                titre = input("\nEntrez le titre du livre : ").strip()
                auteur = input("Entrez le nom de l'auteur : ").strip()
                date = input("Entrez la date de publication : ").strip()
                livre = Livre(titre, auteur, date)
                # Utilisation de append() pour ajouter un element a la fin de la liste
                livres.append(livre)
                print(f"\nLe livre '{titre}' a été ajouté.")
            except Exception as e:
                print(f"Une erreur est survenue : {e}")

        # AFFICHER les livres
        elif choix == 2:
            if livres:
                print("\nListe des livres :")
                # Utilisation de enumerate() pour iterer dans la liste
                for index, livre in enumerate(livres):
                    print(f"{index + 1}. {livre}")
            else:
                print("Aucun livre dans la liste.")

        # RECHERCHER un livre par titre
        elif choix == 3:
            # Utilisation de lower() pour convertir en minuscule
            recherche = input("Entrez le titre du livre à rechercher : ").strip().lower()
            resultats = [
                livre for livre in livres if recherche in livre.titre.lower()
            ]
            if resultats:
                print("\nLivres trouvés :\n")
                for livre in resultats:
                    print(livre)
            else:
                print("Aucun livre trouvé.")

        # SUPPRIMER un livre
        elif choix == 4:
            if livres:
                print("\nListe des livres :")
                # Utilisation de enumerate()
                for index, livre in enumerate(livres):
                    print(f"{index + 1}. {livre}")
                try:
                    indice = int(input("\nEntrez le numéro du livre à supprimer : \n")) - 1
                    if 0 <= indice < len(livres):
                        livre_supprime = livres.pop(indice)
                        print(f"\nLe livre '{livre_supprime.titre}' a été supprimé.\n")
                    else:
                        print("Numéro invalide.")
                except ValueError:
                    print("Veuillez entrer un numéro valide.")
                except Exception as e:
                    print(f"Une erreur est survenue : {e}")
            else:
                print("\nLa liste est vide. Aucun livre à supprimer.\n")
        # EXIT
        elif choix == 5:
            print("\nMerci d'avoir utilisé la bibliothèque. Au revoir !\n")
            break

        else:
            print("\nChoix invalide. Veuillez réessayer.\n")

# Lancer le programme
bibliotheque()
