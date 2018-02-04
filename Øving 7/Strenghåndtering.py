__author__ = 'Martin'

def compare(str1, str2):        # oppgave a
    if len(str1) == len(str2):  #sjekker lengde
        lik = True
        i = 0
        while lik == True and i < len(str1):      #sjekker tegn for tegn
            if str1[i] == str2[i]:                  #rewrite
                lik = True
                i += 1
            else:
                lik = False
    else:
        lik = False
    return lik


def reverse(string):
    revStr = ""
    j = 0
    while j < len(string):      #prov med for lokke med -1 i step
        revStr = string[j] + revStr
        j += 1
    return revStr

def palindrom(input):
    print(compare(input,reverse(input)))

str1 = "Hei pi deg"
str2 = "Hei pi deg"
str3 = "Hade."
str4 = "hade."
palStr = "abba"

def contain(str1, str2):
    for i in range(len(str1)-len(str2)+1):
        if str1[i:i + len(str2)] == str2:
            return i
    return -1

    

#print(compare(str1, str2))

#print(reverse(str3))

#palindrom(palStr)

print(contain("Hva?","k"))
