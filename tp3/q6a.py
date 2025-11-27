import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.preprocessing import MinMaxScaler 
  
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/cpuperformance/machine.data' 
names = ['constructor','Model','MYCT','MMIN','MMAX','CACH','CHMIN','CHMAX','PRP','ERP'] 
  
dataset = pd.read_csv(url, names=names) 
 
print("data:") 
print(dataset) 
  
# MIN MAX SCALING 
minmax_scale = MinMaxScaler().fit(dataset[['MYCT', 'MMAX']]) 
df_minmax = minmax_scale.transform(dataset[['MYCT', 'MMAX']])

# Créer un DataFrame avec les résultats
df_minmax_result = pd.DataFrame(df_minmax, columns=['MYCT_scaled', 'MMAX_scaled'])
print("\nDonnées après normalisation Min-Max:")
print(df_minmax_result)