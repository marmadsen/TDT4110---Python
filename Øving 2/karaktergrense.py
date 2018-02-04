def main ():
    while True:
        try:
            poeng = int(input("Skriv inn antall poeng: "))
            print(poeng)
            poengtest(poeng)
            break
        except ValueError:
            print("Antall poeng må være et heltall.")

def poengtest (poeng):
    if 100 >= poeng >= 89:
        print("Du fikk karakteren A.")
    elif 88 >= poeng >= 77:
        print("Du fikk karakteren B.")
    elif 76 >= poeng >= 65:
        print("Du fikk karakteren C.")
    elif 64 >= poeng >= 53:
        print("Du fikk karakteren D.")
    elif 52 >= poeng >= 41:
        print("Du fikk karakteren E.")
    elif 40 >= poeng >= 0:
        print("Ser ut som det blir konting på deg...")
    else:
        print("Antall poeng du oppga er ukorekte.") #Hvordan kan jeg teste dette i main løkken?
main()



