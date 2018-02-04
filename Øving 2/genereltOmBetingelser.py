a = 5
b = int(input("Skriv inn et tall: "))

def maths() :
    summen = a + b
    produkt = a * b
    if summen > produkt:
        print(summen)
    elif summen < produkt:
        print(produkt)
    else:
        print("You don goofed.")

maths()

def math2EletricBoogalo () :
    maths2 = int(input("Hva er produktet 3 * 4 lik?: "))
    faktiskprodukt = 3 * 4
    if maths2 == faktiskprodukt:
        print("YOU WIN!")
    else:
        print("Back2skool scrub.")

math2EletricBoogalo()

#prøv del 2 med random tall
