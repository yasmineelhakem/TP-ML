import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.decomposition import PCA 
from sklearn.preprocessing import StandardScaler 
from sklearn.datasets import load_iris 
import seaborn as sns 
# Charger un jeu de données Iris 
data = load_iris() 
X = data.data  # Caractéristiques 
y = data.target  # Étiquettes 
# Étape 1 : … 
scaler = StandardScaler() 
X_scaled = scaler.fit_transform(X) 
# Étape 2 : … 
pca = PCA(n_components=2)  
X_pca = pca.fit_transform(X_scaled) 
# Étape 3 : … 
print(pca.explained_variance_ratio_) 
# Étape 4 : … 
df_pca = pd.DataFrame(X_pca, columns=['Composante 1', 'Composante 2']) 
df_pca['Classe'] = y 
 
7 
 
print(df_pca.head()) 
 
#plot graphique d’observation des données 
with plt.style.context('seaborn-v0_8-whitegrid'): 
    plt.figure(figsize=(6, 4)) 
    for lab, col in zip((0, 1, 2), 
                        ('blue', 'red', 'green')): 
        plt.scatter(X_pca[y==lab, 0], 
                    X_pca[y==lab, 1], 
                    label=lab, 
                    c=col) 
    plt.xlabel('Principal Component 1') 
    plt.ylabel('Principal Component 2') 
    plt.legend(loc='lower center') 
    plt.tight_layout() 
    plt.show() 
 
# Gaphique de la variance expliquée cumulative 
pca_full = PCA().fit(X_scaled) 
plt.plot(range(1, len(pca_full.explained_variance_ratio_) + 1),  
         pca_full.explained_variance_ratio_.cumsum(), marker='o') 
plt.xlabel('Nombre de Composantes') 
plt.ylabel('Variance expliquée cumulée') 
plt.title('Sélection du nombre de composantes') 
plt.show() 