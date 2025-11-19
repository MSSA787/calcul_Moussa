import matplotlib.pyplot as plt
import numpy as np
 #c == float(input("entrez votre note de R103 :"))] 

def calcul(coef_ue1) :
    notes = []
    a = float(input("entrez votre notes de R101 :"))
    a1 = float(input("entrez le coef R101 :"))
    b = float(input("entrez votre notes de R102 :"))
    b1 = float(input("entrez le coef de R102 :"))
    for elt in range(len(notes)) :
        r101 = (a*a1)/ a1
        r102 = (b*b1)/ b1
        note.append(r101)
        note.append(r102)
    return notes
        
        
#def get_color(value):
 #   return 'green' if value > 10 else 'red'
    
# colors = [get_color(val) for val in [10,20,15]
#plt.bar(['A','B','C'], [10,20,15], color=colors)
#plt.show

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

r101 =(elt[0]*coef_ue1["R101"])/ coef_ue1["R101"]
        r102 = (elt[1]*coef_ue1["R102"])/coef_ue1["R102"] 