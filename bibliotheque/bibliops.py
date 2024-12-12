import mysql.connector

# Conexión a la base de datos
conn = mysql.connector.connect(
    host="localhost",
    port="8889",
    user="root",
    password="root",
    database="bibliotheque"
)
cursor = conn.cursor()

# Agregar un usuario si no existe
def ajouter_utilisateur(nom):
    try:
        cursor.execute("""
            SELECT id FROM users WHERE name = %s
        """, (nom,))
        utilisateur = cursor.fetchone()

        if utilisateur:
            print(f"L'utilisateur '{nom}' ya existe en la base de données.")
            return utilisateur[0]  # Retorna el ID del usuario existente
        else:
            cursor.execute("""
                INSERT INTO users (name) VALUES (%s)
            """, (nom,))
            conn.commit()
            print(f"L'utilisateur '{nom}' a été ajouté avec succès.")
            return cursor.lastrowid  # Retorna el ID del nuevo usuario
    except mysql.connector.Error as err:
        print(f"Erreur lors de l'ajout de l'utilisateur : {err}")
        return None

# Agregar un libro
def ajouter_livre(titre, auteur, date, utilisateur_id, conn, cursor):
    try:
        # Comprobar que el usuario existe antes de agregar el libro
        cursor.execute("SELECT id FROM users WHERE id = %s", (utilisateur_id,))
        utilisateur = cursor.fetchone()

        if not utilisateur:
            print(f"Erreur : L'utilisateur avec ID {utilisateur_id} n'existe pas.")
            return

        # Insertar el libro en la tabla "livres"
        cursor.execute("""
            INSERT INTO livres (titre, auteur, date)
            VALUES (%s, %s, %s)
        """, (titre, auteur, date))
        conn.commit()

        livre_id = cursor.lastrowid  # Obtener el ID del libro agregado
        print(f"Livre '{titre}' ajouté avec succès! (ID: {livre_id})")

        # Crear una entrada en el log de auditoría
        cursor.execute("""
            INSERT INTO historique_user (action, livre_id, utilisateur_id)
            VALUES (%s, %s, %s)
        """, ("ajout", livre_id, utilisateur_id))
        conn.commit()
        print(f"Audit log créé pour l'ajout du livre '{titre}'.")

    except mysql.connector.Error as err:
        print(f"Erreur lors de l'ajout du livre: {err}")

# Eliminar un libro
def supprimer_livre(livre_id, utilisateur_id, conn, cursor):
    try:
        # Comprobar si el usuario existe
        cursor.execute("SELECT id FROM users WHERE id = %s", (utilisateur_id,))
        utilisateur = cursor.fetchone()

        if not utilisateur:
            print(f"Erreur : L'utilisateur avec ID {utilisateur_id} n'existe pas.")
            return

        # Comprobar si el libro existe antes de intentar eliminarlo
        cursor.execute("SELECT id FROM livres WHERE id = %s", (livre_id,))
        livre = cursor.fetchone()

        if not livre:
            print(f"Erreur : Le livre avec ID {livre_id} n'existe pas.")
            return

        # Añadir un log de auditoría antes de eliminar el libro
        cursor.execute("""
            INSERT INTO historique_user (action, livre_id, utilisateur_id)
            VALUES (%s, %s, %s)
        """, ("suppression", livre_id, utilisateur_id))
        conn.commit()
        print(f"Audit log créé pour la suppression du livre ID {livre_id}.")

        # Eliminar el libro de la tabla "livres"
        cursor.execute("DELETE FROM livres WHERE id = %s", (livre_id,))
        conn.commit()

        print(f"Livre ID {livre_id} supprimé avec succès par l'utilisateur ID {utilisateur_id}.")

    except mysql.connector.Error as err:
        print(f"Erreur lors de la suppression du livre : {err}")
        conn.rollback()  # Realizar rollback si ocurre un error



# Función de gestión de la biblioteca
def bibliotheque(conn, cursor):
    while True:
        print("\nMenu :")
        print("1. Ajouter un livre")
        print("2. Afficher les livres")
        print("3. Rechercher un livre par titre")
        print("4. Éliminer un livre")
        print("5. Quitter")

        try:
            choix = int(input("\nChoix : "))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        if choix == 1:
            try:
                titre = input("\nEntrez le titre du livre : ").strip()
                auteur = input("Entrez le nom de l'auteur : ").strip()
                date = input("Entrez la date de publication : ").strip()
                utilisateur_nom = input("Entrez le nom de l'utilisateur : ").strip()

                # Asegurarse de que el usuario exista o se cree
                utilisateur_id = ajouter_utilisateur(utilisateur_nom)

                if utilisateur_id:
                    ajouter_livre(titre, auteur, date, utilisateur_id, conn, cursor)

            except Exception as e:
                print(f"Une erreur est survenue : {e}")

        elif choix == 2:
            cursor.execute("SELECT titre, auteur, date FROM livres")
            livres_db = cursor.fetchall()
            if livres_db:
                print("\nListe des livres :")
                for index, (titre, auteur, date) in enumerate(livres_db, start=1):
                    print(f"{index}. {titre}, écrit par {auteur} en {date}")
            else:
                print("Aucun livre dans la base de données.")

        elif choix == 3:
            recherche = input("Entrez le titre du livre à rechercher : ").strip()
            cursor.execute("SELECT titre, auteur, date FROM livres WHERE titre LIKE %s", (f"%{recherche}%",))
            resultats = cursor.fetchall()
            if resultats:
                print("\nLivres trouvés :")
                for titre, auteur, date in resultats:
                    print(f"{titre}, écrit par {auteur} en {date}")
            else:
                print("Aucun livre trouvé.")

        elif choix == 4:
            try:
                livre_id = int(input("Entrez l'ID du livre à supprimer : "))
                utilisateur_nom = input("Entrez le nom de l'utilisateur : ").strip()

                # Asegurarse de que el usuario exista o se cree
                utilisateur_id = ajouter_utilisateur(utilisateur_nom)

                if utilisateur_id:
                    supprimer_livre(livre_id, utilisateur_id, conn, cursor)

            except Exception as e:
                print(f"Une erreur est survenue : {e}")

        elif choix == 5:
            print("\nMerci d'avoir utilisé la bibliothèque. Au revoir !")
            break

        else:
            print("\nChoix invalide. Veuillez réessayer.")

# Ejemplo de uso
if __name__ == "__main__":
    bibliotheque(conn, cursor)

# Cerrar conexiones
cursor.close()
conn.close()
