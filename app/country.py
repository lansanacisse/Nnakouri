import streamlit as st
import pandas as pd
import sqlite3

# Connexion à la base de données
conn = sqlite3.connect('../databases/african_countries.db')

# Récupérer les pays depuis la base de données
query = "SELECT DISTINCT name FROM african_countries ORDER BY name"
countries_df = pd.read_sql_query(query, conn)
countries = countries_df['name'].tolist()

# Fermer la connexion
conn.close()

# Créer un onglet de filtre pour les pays
st.sidebar.header("Filtres")
selected_countries = st.sidebar.multiselect(
    "Sélectionner les pays:",
    options=countries,
    default=countries[:3] if len(countries) >= 3 else countries
)

# Afficher les pays sélectionnés
st.write("Pays sélectionnés:", selected_countries)