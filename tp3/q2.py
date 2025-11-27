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
db = df.duplicated() 
print(df[db]) 
 
df_new = df.drop_duplicates() 
print(df_new) 