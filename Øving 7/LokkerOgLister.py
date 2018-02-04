__author__ = 'Martin'

def separate(numbers, threshold):
    smaller = []
    greater = []
    for i in numbers:
        if i < threshold:
            smaller.append(i)
        else:
            greater.append(i)

    return (smaller, greater)




def main():             #oppgave a
    a = [1, 3, 4, 5, 6]
    b = 4
    smaller, greater = separate(a, b)
    print(smaller)
    print(greater)

main()

def multiplication_table(n):            #oppgave 2
    matrise = []
    for i in range(1,n+1):
        rad = []
        for j in range(1,n +1):
            rad.append((j)*(i))
        matrise.append(rad)
    return matrise

print(multiplication_table(5))

def test():
    a = multiplication_table(5)
    output = ""
    for rad in a:
        for element in rad:
            output += "{:5d}".format(element)
        output += "\n"
    print(output)

test()