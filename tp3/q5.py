import pandas as pd 
import numpy as np 

df = pd.DataFrame({'A': [2,1,2,3,3,5,4],'B': [1,2,3,5,4,2,5], 
                   'C': [5,3,4,1,1,2,3]}) 

print("DataFrame original :")
print(df) 

print("\nLe jeu de données est trié selon la colonne 'A'") 
# Correction : utiliser 'sort_values' au lieu de 'sort_index'
df = df.sort_values(by=['A'], ascending=[True]) 
df = df.reset_index(drop=True) 
print(df) 

print("\nLe jeu de données est mélangé") 
index = df.index.tolist() 
np.random.shuffle(index) 
# Correction : utiliser 'iloc' au lieu de 'ix' (déprécié)
df = df.iloc[index] 
df = df.reset_index(drop=True) 
print(df)