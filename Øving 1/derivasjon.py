import math
print("Dette programmet deriver sin(x) numerisk")

x = float(input("Skriv din x verdi: "))

a = float(input("Skriv grunntallet i din h-verdi: "))
b = float(input("Skriv eksponenten din (husk minus!):"))

h = pow(a,b)

def main():
    f1 = math.sin(x)
    f2 = math.sin(x + h)
    numDer = (f2 - f1)/h
    print("Den numeriske deriverte av sin("+str(x)+") er:",format(numDer, '.2f'))

print(h)
print(x)

main()

    
