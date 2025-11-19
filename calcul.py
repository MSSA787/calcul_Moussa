import matplotlib.pyplot as plt
import numpy as np
 #c == float(input("entrez votre note de R103 :"))] 
nom = ["R101", "R102", "R103", "R104", "R105", "R106", "R107", "R108", "R109","R110","R111","R112","R113", "R114","R115"]
coef = [10, 10, 7, 7, 0, 5, 0, 6, 0, 5, 4, 2, 5, 5, 0]
notes = {} 


i = 0
while i <= len(nom):
    notes= (input("entrez votre notes :"))
    i+=1
resultat=dict(zip(nom,notes))

def calcul(nom,notes) :
    if not notes :
        return 0
    somme = sum(notes[s]*coef[s] for s in resultat.keys())
    coef = sum(coef[s] for s in resultat.keys())
    return somme/coef if coef else 0
           
def get_color(value):
    return 'green' if value > 10 else 'red'
colors = [get_color(val) for val in [10,20,15] ]
plt.bar([], [12,26,15], color=colors)
plt.show()


coef_ue1={
    "R101":10, 
    "R102":10,
    "R103":7,
    "R104":7,
    "R105":[], 
    "R106":5,
    "R107":[],
    "R108":6, 
    "R109":[],
    "R110":5,
    "R111":4,
    "R112":2,
    "R113":5, 
    "R114":5,
    "R115":[], }


a1 = float(input("entrez le coef R101 :"))
    b = float(input("entrez votre notes de R102 :"))
    b1 = float(input("entrez le coef de R102 :"))


 for elt in range(len(notes)) :
            r101 = (a*a1)/ a1
            r102 = (b*b1)/ b1
            note.append(r101)
            note.append(r102)
        return notes

r101 =(elt[0]*coef_ue1["R101"])/ coef_ue1["R101"]
        r102 = (elt[1]*coef_ue1["R102"])/coef_ue1["R102"] 


def get_color(value):
 return 'green' if value > 10 else 'red'
    
colors = [get_color(val) for val in [10,20,15]]
plt.bar(['A','B','C'], [10,20,15], color=colors)
plt.show()