import matplotlib.pyplot as plt
import numpy as npcoef
 #c == float(input("entrez votre note de R103 :"))] 
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

def calcul(coef_ue1) :
    notes = []
    a = float(input("entrez votre note de R101 :"))
    b = float(input("entrez votre note de R101 :"))
    for elt in range(len(note)) :
        r101 =(a*coef_ue1["R101"])/ coef_ue1["R101"]
        r102 = (b*coef_ue1["R102"])/ coef_ue1["R102"]
        notes.append(r101)
        notes.append(r102)
    return notes
        
        
    

        
#def get_color(value):
 #   return 'green' if value > 15 else 'red'
