import sqlite3

def create_database():
    # Créer une connexion à la base de données
    conn = sqlite3.connect('african_countries.db')
    cursor = conn.cursor()
    
    # Créer la table des restaurants africains
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS restaurants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT,
            city TEXT,
            country TEXT,
            phone TEXT,
            email TEXT,
            cuisine_type TEXT,
            rating REAL,
            description TEXT
        )
    ''')
    
    # Sauvegarder et fermer
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()