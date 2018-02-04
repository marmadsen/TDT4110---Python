__author__ = 'Martin'

import random

def centerMass(liste):      #oppgave a
    R = 0
    j = 0.5
    M = 0
    for masse in liste:
        R += masse*j
        j += 1
        M += masse
    r_cm = R/M
    return r_cm

def randomListe(n):     #oppgave b
    randListe = []
    for i in range(0,n):
        a = random.uniform(0,10)
        randListe.append(a)
    print(randListe)
    return randListe

print(centerMass([1]))
print(centerMass([1,1]))
print(centerMass([1,1,1]))
print(centerMass([3,1,3]))
print(centerMass([1,2,3,4]))

print(centerMass(randomListe(15)))






