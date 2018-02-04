i = 1
n = int(input("Skriv inn heltallet n: "))
a = 0
switch = True
while i < n:
    if switch:
        if a + i**2 > n:
            print("Resultat med n = ",n,": ",a, sep='')
            print("Antall ledd: ",i - 1, sep='')
            break
        a += i**2
        switch = False
        i += 1
    else:
        a -= i**2
        switch = True
        i += 1
    
    print(a)


#Prøv med -1^n triks
    

    
