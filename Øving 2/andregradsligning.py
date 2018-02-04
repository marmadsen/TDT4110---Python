import math

print("I dette programmet skal vi studere røtter av andregradspolynomer.")
print("Polynomet er på formen ax*x + bx + c = 0")

a = float(input("Skriv verdien på a: "))
b = float(input("Skriv verdien på b: "))
c = float(input("Skriv verdien på c: "))

d = math.pow(b,2) - 4 * a * c
null = 0



def root ():
    doubleRoot = (str(a)+'x*x + '+str(b)+'x + '+str(c)+' = 0 har en reell dobbeltrot.') 
    toReelle = (str(a)+'x*x + '+str(b)+'x + '+str(c)+' = 0 har to reelle løsninger.')
    imagRoot = (str(a)+'x*x + '+str(b)+'x + '+str(c)+' = 0 har to imaginære løsninger.')
    if d == null :
        print(doubleRoot)
    elif d < null :
        print(imagRoot)
    elif d > null :
        print(toReelle)

root()
#print(d)

#Hva hvis a, b, eller c er negativ eller null?
