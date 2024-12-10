list = ["hello", "hola", "hola", "bonjour", "ciao", "1", 1, True]
print(list)

tuple = ("manzana", "pera", "pera", "naranja", "platano", "1", 1, True)
print(tuple)

dict = {
    "color": "grey",
    "brand": "nissan",
    "model": "juke",
    "model": "juke",
    "year": 2015,
    "1": 1,
    3 : True,
    False : 4
}
print(dict)

set = {"apple", "banana", "cherry", "1", 1, True}
print(set)


def convert_usd_eur(montant_usd, taux_change):
    montant_eur = montant_usd * taux_change
    return montant_eur

montant_usd = 100
taux_change = 0.9460
montant_eur = convert_usd_eur(montant_usd, taux_change)
print(f"{montant_usd} USD équivalent à {montant_eur: .2f} EUR.")

# Récupérer le montant en euros saisi par l'utilisateur,
# puis dans la console afficher le montant converti en dollars

def convert_eur_usd(montant_eur, taux_change):
    montant_usd = montant_eur * taux_change
    return montant_usd

montant_eur = 100
taux_change = 1.0578
montant_usd = convert_eur_usd(montant_eur, taux_change)
print(f"{montant_eur} EUR équivalent à {montant_usd: .2f} USD.")



#def convert_usd(taux_change):
 #   montant_eur = input('Entrer un montant en euro : ')
 #   montant_usd = float(montant_eur) * taux_change

  #  return print(f"{montant_eur} EUR équivalent à {montant_usd: .2f} USD.")

# taux_change = 1.0578
# convert_usd(taux_change)

#-------------------------------------------------------------------#

# def euro_to_usd():
   # while True:
      #  try:
       #     euro = input("Entre le montant en euros: ")
       #     usd = 1.05
        #    euro = float(euro) * usd
         #   print(f"{usd} $ ")

     #   except ValueError:
      #      print("Veuillez entrer un nombre valide")
       #     continue
       # else:
        #    break
# euro_to_usd()

try:
	x = 10 / 0
except ZeroDivisionError:
    print("Erreur : Division par zéro.")

class Voiture:
    def __init__(self, marque, modele, annee, vitesse=0):
            self.marque = marque
            self.modele = modele
            self.annee = annee
            self.vitesse = vitesse

ma_voiture = Voiture("Tesla", "Model S", 2023)

print(ma_voiture.marque)


with open("fichier.txt", "w") as file:
    file.write("Bonjour, Python!")
