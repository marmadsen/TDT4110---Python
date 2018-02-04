def main():
    truthvalue = compareNr(float(input("Skriv tall 1: ")), float(input("Skriv tall 1: ")))
    if truthvalue == 1:
        print("Disse tallene er like.")
    else:
        print("Disse tallene er ikke like.")

def compareNr(tall1, tall2):
    if tall1 <= tall2 and tall1 >= tall2:
        sammeNr = 1
    else:
        sammeNr = 2
    return sammeNr

main()

