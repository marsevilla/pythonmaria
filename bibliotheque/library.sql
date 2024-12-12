CREATE DATABASE IF NOT EXISTS bibliotheque;
USE bibliotheque;

DROP TABLE IF EXISTS historique_user;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS livres;


-- Crear la tabla livres
CREATE TABLE IF NOT EXISTS livres (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titre VARCHAR(100) NOT NULL,
    auteur VARCHAR(100) NOT NULL,
    date INT(4) NOT NULL
);

-- Crear la tabla users (usuarios)
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Crear la tabla historique_user con claves foráneas correctas
CREATE TABLE IF NOT EXISTS historique_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    action VARCHAR(50) NOT NULL,
    livre_id INT,
    utilisateur_id INT,
    date_action TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (livre_id) REFERENCES livres(id) ON DELETE SET NULL,
    FOREIGN KEY (utilisateur_id) REFERENCES users(id) ON DELETE CASCADE
);
