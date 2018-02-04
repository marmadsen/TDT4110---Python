__author__ = 'Martin'

def countCoins(mynter):     #Teller antall mynter av hver type i en liste
    tyve = 0
    ti = 0
    fem = 0
    en = 0
    for i in range(len(mynter)):
        if mynter[i] == 20:
            tyve += 1
        elif mynter[i] == 10:
            ti += 1
        elif mynter[i] == 5:
            fem += 1
        elif mynter[i] == 1:
            en += 1
    result = [tyve, ti, fem, en]
    print(result)

def numCoins(liste):        #Gitt en liste med summer, gir kombinasjonen av minst mynter som gir summen
    antallMynt = []
    for i in range(len(liste)):
        li = []
        a = liste[i]
        b = a//20
        li.append(b)
        c = (a-20*b)//10
        li.append(c)
        d = (a - 20*b - 10*c)//5
        li.append(d)
        e = (a - 20*b - 10*c - 5*d)
        li.append(e)
        antallMynt.append(li)
    return antallMynt
    #print(antallMynt)

def weightCoins(myntFordeling, myntVekt):   #regner ut vekten av alle myntene fra numCoins
    delsum = 0
    for i in range(len(myntFordeling)):
        a = myntFordeling[i]
        for i in range(len(a)):
            weight = a[i]*myntVekt[i]
            delsum += weight
    print(round(delsum, 2))

def main():
    mynter = [20,10,5,20,1,1,20]
    countCoins(mynter)
    liste = [12,23,34,45,56,67,78,89,90,98,87,65,54,43,21]
    myntVekt = [9.9, 6.8, 7.85, 4.35]
    fordelingsVektor = numCoins(liste)
    print(fordelingsVektor)
    weightCoins(fordelingsVektor,myntVekt)

main()