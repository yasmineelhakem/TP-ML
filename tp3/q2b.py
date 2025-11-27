import pandas as pd 

# Exemple de jeu de données 
data = { 
    'Nom': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob'], 
    'Age': [25, 30, 35, 25, 30], 
    'Ville': ['Paris', 'Lyon', 'Marseille', 'Paris', 'Lyon'] 
} 

# Création d'un DataFrame 
df = pd.DataFrame(data) 

# Affichage du DataFrame original 
print("DataFrame original :") 
print(df) 

# Identifier les doublons basés sur la colonne 'Nom'
db = df.duplicated(subset=['Nom'])
print("\nLignes dupliquées basées sur 'Nom' :")
print(df[db])

# Supprimer les doublons en fonction de la colonne 'Nom'
df_new = df.drop_duplicates(subset=['Nom'])
print("\nDataFrame après suppression des doublons basés sur 'Nom' :")
print(df_new)