__author__ = 'Martin'

import random



def pick(numbers,n): #Velger 10 tall fra numbers
    picked = []
    i = 0
    while i < n:
        a = random.randint(0,len(numbers)-1)
        #print(a)
        b = numbers.pop(a)                      #Hvorfor failer dette? FIKK FIKSA DET
        picked.append(b)
        i += 1
    return picked


def compList(myGuess, valgt, start, slutt):
    slice = valgt[start:slutt]
    likeTall = set(slice).intersection(myGuess)         #felles elementer i de 2 listene
    #
    return likeTall


def premie(retteTall, tillegsTall):     #Bestemmer premie
    premie = 0
    if retteTall == 4 and tillegsTall == 1:
        #print("Du vant 45kr.")
        premie = 45
    elif retteTall == 5:
        #print("Du vant 90kr.")
        premie = 90
    elif retteTall == 6:
        #print("Du vant 3385kr.")
        premie = 3385
    elif retteTall == 6 and tillegsTall == 1:
        #print("Du vant 102 110kr.")
        premie = 102110
    elif retteTall == 7:
        #print("Du vant 2 749 455kr.")
        premie = 2749455
    #else:
        #print("Beklager, ingen gevinst.")
    return premie

def main():
   numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
   myGuess = [4, 6, 9, 10, 19, 20, 31]
   valgt = pick(numbers,10)
   #print(valgt)
   retteTall = len(compList(myGuess, valgt, 0, 7))
   tillegsTall = len(compList(myGuess, valgt, 7,10))
   #print("Du har ", retteTall, " rette og ", tillegsTall, " tillegstall riktig.", sep='')
   return premie(retteTall, tillegsTall)


def sim():
    forbruk = 0
    premie = 0
    for i in range(1,1000000):
        forbruk += 45
        premie += main()
    print("Premie:", premie)
    print("Forbruk:", forbruk)
    print("Netto:", premie - forbruk)
#main()

sim()