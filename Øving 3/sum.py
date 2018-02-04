def forLogic():
    n = int(input("Hva er din N: "))
    i = 1
    x = 0
    for i in range(1,n):
        xi = 1/(i**2)
        x += xi
        i += 1
    print(x)

def whileLogic():
    n = int(input("Hva er din N: "))
    i = 1
    x = 0
    tol = 0.0001
    xi = 1
    while xi > tol:
        xi = 1/(i**2)
        x += xi
        i += 1
    print(x)

forLogic()

whileLogic()

            
        
