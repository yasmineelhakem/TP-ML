import pandas as pd 
import numpy as np 
from sklearn.impute import SimpleImputer

# Create an empty dataset 
df = pd.DataFrame() 
# Create two variables called x0 and x1. Make the first value of x1 a missing value 
df['x0'] = [0.3051,0.4949,0.6974,0.3769,0.2231,0.341,0.4436,0.5897,0.6308,0.5] 
df['x1'] = [np.nan,0.2654,0.2615,0.5846,0.4615,0.8308,0.4962,0.3269,0.5346,0.6731] 

# View the dataset 
print("Data :") 
print(df) 

# Create an imputer object that looks for 'Nan' values, then replaces them with the mean value of the feature  
print("chercher les valeurs manquantes et les remplacer par la moyenne de la colonne")
mean_imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
# Apply the imputer on the df dataset 
mean_imputer = mean_imputer.fit(df)
imputed_df = mean_imputer.transform(df.values)

# View the dataset 
print("data apres imputation") 
print(imputed_df)