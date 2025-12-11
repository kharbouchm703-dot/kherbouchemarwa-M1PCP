import pandas as pd

# 1) Créer et afficher le tableau
data = {
    "Séquence": [
        "ATGCGTACGTA",
        "GCTAGCTAGGCC",
        "ATGCGCGTAAGT",
        "TACGATCGTA",
        "ATGAAAGGCTT",
        "CGTACCTAGC",
        "TTAACCGGAT"
    ],
    "Longueur": [12, 12, 12, 10, 11, 10, 10],
    "Pourcentage_GC": [50, 66.67, 58.33, 40, 45.45, 60, 50]
}

df = pd.DataFrame(data)
print("Tableau initial :")
print(df)