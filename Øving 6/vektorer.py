def getVector():        #lager en vektor fra input, og konverterer fra string til floats
    a = input("Skriv dine 3 verdier for vektoren separert med komma:")
    vec1 = a.split(',')
    for i in range(len(vec1)):
        vec1[i] = float(vec1[i])
    print(vec1)
    return(vec1)


def skalar(vec1, skal):     #skalarprodukt
    vec2 = []
    for i in range(len(vec1)):
        vec2.append(vec1[i]*skal)
    print("vec2 =", vec2)
    return(vec2)

def lengde(vec1, vec2, skal):       #Lengden av vektor1 før og etter skalering
    vec1Len = (vec1[0]**2 + vec1[1]**2 + vec1[2]**2)**0.5       #gjør generell
    vec2Len = (vec2[0]**2 + vec2[1]**2 + vec2[2]**2)**0.5
    print("Lengden av vec1", vec1Len)
    print("Lengden av vec1 skalert med", skal, ":", vec2Len)
    print("Forholdet mellom de to lengdene er:", vec1Len/vec2Len)

def innerprod(vec1, vec2):      #dotprodukt av to vektorer
    y = 0
    for i in range(len(vec1)):      #feilmelding for ikke like lange vektorer
        x = (vec1[i]*vec2[i])
        y += x
    print(y)

def main():
    print("Vec1 =")
    vec1 = getVector()
    skal = float(input("Skriv din skalar her:"))
    vec2 = skalar(vec1, skal)
    lengde(vec1, vec2, skal)
    print("Indreproduktet av vec1 og vec2 =")
    innerprod(vec1, vec2)
    print("vec4 =")
    vec4 = getVector()
    print("Indreproduktet av vec1 og vec4 =")
    innerprod(vec1, vec4)




main()


