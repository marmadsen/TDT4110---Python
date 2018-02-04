__author__ = 'Martin'

import math

def ducci(liste):
    i = 0
    ducciListe = []
    while i in range(0,len(liste)):
        if i == len(liste) - 1:
            j = 0
            ducciListe.append(math.fabs(liste[j]-liste[i]))
        else:
            j = i + 1
            ducciListe.append(math.fabs(liste[j]-liste[i]))
        i += 1
    return ducciListe
        

def test(liste):
    li = ducci(liste)
    compare = []
    while li != compare:
        compare = li
        li = ducci(li)
        print(li)


test([10,8,12,15,5,7,43,21])



