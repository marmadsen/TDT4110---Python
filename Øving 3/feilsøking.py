debug = False

def mult():
    tall1 = int(input("Skriv tall 1: "))
    tall2 = int(input("Skriv tall 2: "))
    if debug == True:
        print("Tallene som multipliseres er ",tall1," og ",tall2,".", sep='')
    print(tall1 * tall2)

mult()
