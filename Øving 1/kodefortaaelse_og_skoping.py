
'''
i main : 7 3
 ---> i swap : 3 7
i main : 7 3
 ---> i printglobals : 5 8
i main : 7 3
'''

x = 5
y = 8
#Lagrer x og y som globale variabler
def main (): #lager en funksjon kalt main
    x = 7       #Definerer x som en funksjonsvariabel
    y = 3       #Definerer Y som en funksjonsvariabel
    print ("i main :", x, y) #Printer verdiene x og y lagret som lokale variabler
    swap (x,y)              #caller funksjonen swap med variablene x og y
    print ("i main :", x, y) #Printer verdiene x og y lagret som lokale variabler
    printglobals ()         #caller funksjonen printgobals
    print ("i main :", x, y) #Printer verdiene x og y lagret som lokale variabler
def swap (x, y):            #definerer funksjonen swap
    x,y = y,x # Python triks for å bytte om to variabler .
    print (" ---> i swap :", x, y) #printer de ombyttede x og y verdiene
def printglobals ():                #definerer funksjonen printglobals
    print (" ---> i printglobals :", x, y) #printer de globale x og y verdiene
main ()                                 #kjører funksjonen main

'''
Programmet lager globale variabler x og y og kjører funksjonen main.
Main lager funkjsonsvariablene x og y og printer de en gang.
Så kjører den funksjonen swap, som bytter om x og y, kun i denne funksjonen, og printer de.
Main printer så de lokale x og y til den funksjonen.
Main caller funksjonen printglobals. Den printer de globale x og y.
Til slutt printer main de funkjsonsvariablene x og y.
'''
