import pandas as pd

df = pd.read_csv("tp2/prets.csv")

# 2
print(df.columns)
print(df.shape)

# 3
nb_villes = df['ville'].nunique()
print("Nombre de villes uniques :", nb_villes)

# 4
df["taux_endettement"] = (df["remboursement"] * 100 / df["revenu"]).round(2)
df.rename({"taux": "taux_interet"}, axis=1, inplace=True)
print(df.head())

# 5
df["cout_total"] = df["remboursement"] * df["duree"]
df["benefices"] = (df["cout_total"] * df["taux_interet"]) / 24
print(df.head())

# 6
top_benefices = df.sort_values("benefices", ascending=False).head(5)
print('max', top_benefices)

# 7
clients_risque = df[df["taux_endettement"] > 40]
print("Nombre de clients  risque :", len(clients_risque))

# 8
df["risque"] = df["taux_endettement"].apply(lambda x: "Oui" if x > 40 else "Non")
print(df.head())

# 9
nb_pret_auto = df[df["type"] == "automobile"].shape[0]
print("Nombre de prets auto :", nb_pret_auto)

cout_moyen_auto = df[df["type"] == "automobile"]["cout_total"].mean()
print("Cout total moyen des prets auto :", round(cout_moyen_auto, 2))

# 10
benefice_paris = df[df["ville"] == "PARIS"]["benefices"].sum()
print("Benefice total mensuel de Paris :", round(benefice_paris, 2))