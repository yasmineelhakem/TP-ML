import pandas as pd 
import numpy as np 
s = pd.Series([1, 2, 3, np.NaN, 5, 6, None]) 
print("Visualiser les donnees manquantes : true means a detection of a missing data") 
print (s.isnull()) 
print ("Isoler les donnees manquantes") 
print(s[s.isnull()]) 
print(s.fillna(int(s.mean()))) 
print(s.dropna()) 