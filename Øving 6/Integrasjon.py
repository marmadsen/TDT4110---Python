__author__ = 'Martin'

import math

#f = math.sin(x)

def numIntegral(a, b, N):
    h = (b-a)/N
    i = 0
    sum = 0
    while i <= N:
        f_i = math.sin(i*h + h/2 + a) * h       #delsum
        sum += f_i
        i += 1
    print(sum)


def trapesMetode(a, b, N):
    h = (b-a)/N
    i = 1
    sum = 0
    while i <= N:
        f_i = (h/2)*(math.sin(h * i + a) + math.sin(h * (i - 1) + a))       #i-te leddet i summen
        sum += f_i
        i += 1
    print(sum)


def simpsons(a, b, N):
    h = (b-a)/N
    i = 1
    delsum = 0
    while i <= N/2:
        f_i = math.sin(h * (2*i - 2)) + 4*math.sin(h * (2*i -1)) + math.sin(h * (2*i)) #fant formel p wikipedia
        delsum += f_i
        i += 1
    areal = (h/3) * delsum
    print(areal)


print("Numerisk metode:")
numIntegral(0, math.pi, 100)
print("Trapesmetoden:")
trapesMetode(0, math.pi, 100)
print("Simpsons metode:")
simpsons(0, math.pi, 100)

