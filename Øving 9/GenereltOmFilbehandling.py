__author__ = 'Martin'

def generateNumbers(file):      #write 1-100 in a file
    f = open(file,'w')
    for i in range(1,101):
        f.write(str(i)+'\n')
    f.close()


def compareNumbers(file):       #checks if the generated numbers are correct
    f = open(file,'r')
    i = 1
    for line in f:
        if int(line.rstrip('\n')) != i:
            print('ERROR')
            #print(int(line.rstrip('\n')))
            #print(i)
        else:
            print('SUCCESS')
            #print(int(line.rstrip('\n')))
            #print(i)
        i += 1

def ReadWrite(file):        #User can choose to read or write in a file
    print('Do you want to write to a file or read from it?')
    answer = input(print('Input W to write to file, R to read from file'))         #Hvorfor skriver denne None?
    if answer == 'W':
        f = open(file,'w')
        toWrite = input(print('What do you want to write?'))
        f.write(toWrite)
        f.close()
    elif answer == 'R':
        f = open(file,'r')
        for line in f:
            print(line)
        f.close()
    else:
        print('Error occurred, try again:')
        answer = input(print('Input W to write to file, R to read from file'))



#generateNumbers('numbers.txt')      #oppgave a

#compareNumbers('numbers.txt')       #oppgave b

ReadWrite('filbehandling.txt')

