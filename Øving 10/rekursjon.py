__author__ = 'Martin'
import math
#a) sum of all numbers from 1 to n

def sum_rek(n):
    # INPUT: positive number
    # OUTPUT: sum of numbers
    if n == 1:
        return 1
    else:
        return n + sum_rek(n-1)

def main_a():
    t = int(input("Write a whole number:"))
    print('sum of all numbers from 1 to', t, '=', sum_rek(t))

#main_a()

#b) smallest number in a list

def list_rek(list):
    if len(list) == 0:
        return "empty list"
    elif len(list) == 1:
        return list[len(list)-1]
    else:
        list_min = list_rek(list[:(len(list)-1)])
        if list_min < list[len(list)-1]:
            return list_min
        else:
            return list[len(list)-1]


def main_b():
    t = [-4,6,6,9,5,7,3]
    print('minste element i liste er', list_rek(t))

main_b()



#c) sin x
#sin(x) = 3sin(x/3) - 4sin^3(x/3)
# and sin(x) == 1 if x < 0.01

def sin_rek(n,tolerance):
    if n < tolerance:
        #sin(n) = n
        return 3*(n/3) - 4*((n/3)**3)
    else:
        x = sin_rek(n/3,tolerance)
        return 3*x - 4*(x**3)

def main_c():
    print(sin_rek(math.pi/2,0.001))

main_c()



