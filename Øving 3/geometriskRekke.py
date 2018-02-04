
def main():
    print("dette programmet finner summen av en geometrisk rekke:")
    while True:
        try:
            n = int(input("Hva er din n?: "))
            tol = float(input("Hva er din toleranse?"))
            r = float(input("Skriv din r-verdi: "))
            if 1 > r and r > -1:
                break
            print("r må være et flyttall mellom 1 og -1.")
        except ValueError:
            print("n må være et heltall og toleranse et flyttall.")
    p = geo_utregning(n, tol, r)
    differens(p[0], p[1], n, r)

def geo_utregning(n, tol, r):
    i = 0
    ri = r**i
    rn = 0
    while ri > tol:
        ri = r**i
        i += 1
        rn += ri
    return rn, i

def differens(rn, i, n, r):
    grenseverdi = (1 - (r**(n + 1)))/(1 - r)
    diff = abs(grenseverdi - rn)
    print("Numerisk:", '\t', '\t', "Diff:", '\t'*3, "#Iterasjoner:")
    print(rn, '\t', diff, '\t', i)
    
main()
    
    
    
    
