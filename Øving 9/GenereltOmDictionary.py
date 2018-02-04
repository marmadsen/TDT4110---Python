__author__ = 'Martin'


fam = {}

def familie(fam):
    print('We will add your penis to a dictionary')
    familyType = input(print('Write all the types of family members you want to add, separated with comma')).split(",")
    print(familyType)
    for i in familyType:
        names = input(print('Write all names of your '+i+'(s), separated with comma',sep='')).split(",")
        fam[i] = names
    print(fam)


    #while True:
        #fam[input(print("Type of family"))] = input(print("Name"))
        #answer = input(print('Do you want to continue adding family? [y/n]'))
        #if answer == 'n':
            #break
        #elif answer == 'y':
            #continue
        #else:
            #print('invalid input.')
            #answer = input(print('Do you want to continue adding family? [y/n]'))
    #print(fam)

familie(fam)