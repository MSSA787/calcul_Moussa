import matplotlib.pyplot as plt

nom = ["R101", "R102", "R103", "R104", "R105", "R106", "R107", "R108", "R109",
       "R110", "R111", "R112", "R113", "R114", "R115"]
coef = [10, 10, 7, 7, 0, 5, 0, 6, 0, 5, 4, 2, 5, 5, 0]


notes = {}

# Saisie des notes
for i in range(len(nom)):
    note = input(f"Entrez votre note pour {nom[i]} (ou laissez vide si pas de note) : ")
    if note != "":
        notes[nom[i]] = float(note)


def calcul(notes, nom, coef):
    somme = 0
    somme_coef = 0
    for mat in notes:
        i = nom.index(mat)   
        somme += notes[mat] * coef[i]
        somme_coef += coef[i]
    return somme / somme_coef if somme_coef else 0


moyenne = calcul(notes, nom, coef)
print(f"\nVotre moyenne pondérée est : {moyenne:.2f}/20")


def get_color(value):
    return 'green' if value >= 10 else 'red'

matieres = list(notes.keys())
valeurs = list(notes.values())
colors = [get_color(v) for v in valeurs]

plt.bar(matieres, valeurs, color=colors)        
plt.xticks(rotation=45)
plt.ylabel("Notes")
plt.title("Graphique des notes")
plt.legend()
plt.show()