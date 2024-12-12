import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    port="8889",
    user="root",
    password="root",
    database="ma_base"
)
cursor = conn.cursor()

# Création de la table avec Python
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100),
	age INT NOT NULL,
    email VARCHAR(100)
)
""")
# conn.commit()

# cursor.execute("INSERT INTO users (prenom, nom, age) VALUES (%s, %s, %s)", ("Katy", "Smith", 25))
# cursor.execute("INSERT INTO users (prenom, nom, age) VALUES (%s, %s, %s)", ("John", "Mars", 30))

# cursor.execute("SELECT * FROM users")
# resultats = cursor.fetchall() # Récupérer tous les résultats
# for users in resultats: #bucle fort
# 	print(users)

# cursor.execute("UPDATE users SET age = %s WHERE nom = %s", (26, "Smith"))

cursor.execute("DELETE FROM users WHERE nom = %s", ("Smith",))
conn.commit()

# Fermer le courseur et la connexion:
# On le place à la fin de la session d'utilisateur
cursor.close()
conn.close()
