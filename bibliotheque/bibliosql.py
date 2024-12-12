import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    port="8889",
    user="root",
    password="root",
    database="bibliotheque"
)
cursor = conn.cursor()
print ("Connexion à la base de données réussie.")

# Création de la table livres
cursor.execute("""
    CREATE TABLE IF NOT EXISTS livres (
        id INT AUTO_INCREMENT PRIMARY KEY,
        titre VARCHAR(255) NOT NULL,
        auteur VARCHAR(255) NOT NULL,
        date INT NOT NULL
    )
""")
print("Table 'livres' créée avec succès.")
conn.commit()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS utilisateurs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nom VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE
    )
""")
print("Table 'utilisateurs' créée avec succès.")
conn.commit()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS audit_logs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        action VARCHAR(50) NOT NULL,
        livre_id INT,
        utilisateur_id INT,
        date_action TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (livre_id) REFERENCES livres(id),
        FOREIGN KEY (utilisateur_id) REFERENCES utilisateurs(id)
    )
""")
print("Table 'audit_logs' créée avec succès.")
conn.commit()

cursor.close()
conn.close()
