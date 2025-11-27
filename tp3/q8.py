from sklearn.datasets import load_iris 
iris = load_iris() 
import pandas as pd 
import numpy as np 
 
iris_nparray = iris.data 
iris_dataframe = pd.DataFrame(iris.data, columns=iris.feature_names) 
iris_dataframe['group'] = pd.Series([iris.target_names[k] for k in iris.target], dtype="category") 
print("IRIS data values:") 
print(iris_dataframe) 
print("Mean value :") 
print (iris_dataframe.mean(numeric_only=True)) 
print("Median value :") 
print (iris_dataframe.median(numeric_only=True)) 
print("Discrétisation basée sur des effectifs égaux (ou quantiles) :") 
print(iris_dataframe.quantile(np.array([0,.25,.50,.75,1]))) 
#Le binning transforme les variables numériques en variables catégoriques 
iris_binned = pd.concat([ 
        pd.qcut(iris_dataframe.iloc[:,0], [0, .25, .5, .75, 1]), 
        pd.qcut(iris_dataframe.iloc[:,1], [0, .25, .5, .75, 1]), 
        pd.qcut(iris_dataframe.iloc[:,2], [0, .25, .5, .75, 1]), 
        pd.qcut(iris_dataframe.iloc[:,3], [0, .25, .5, .75, 1]), 
        ], join='outer', axis = 1) 
print("Bining IrisData") 
print(iris_binned) 
 
#obtenir une fréquence pour chaque variable catégorique de l'ensemble de données  
print("Fréquence dans chanque catégorie") 
print (iris_dataframe['group'].value_counts()) 
 
print("Fréquence pour chaque marge de valeurs") 
print (iris_binned['petal length (cm)'].value_counts())