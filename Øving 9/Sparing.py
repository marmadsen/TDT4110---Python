__author__ = 'Martin'

#V=A*(1+r/n)^nk
#V = end sum
#A = start sum
#r = interest per year in percent
#n = terms in a year
#k = number of years

def savings(A,r,k):
    n = 4
    rAdjust = r/100     #convert to decimal
    V = (A*(1 + rAdjust/n)**(n*k))
    Vformat = '%.2f' %V
    print('You have saved ',Vformat, ' by saving for ',k,' years with ',r,'% interest.', sep='')
    return Vformat

def annualSavings(A,r,k):
    n = 4
    annSav = []
    rAdjust = r/100     #convert to decimal
    for i in range(1,k+1):
        V = A*(1 + rAdjust/n)**(n*i)
        Vformat = '%.2f' %V
        annSav.append(Vformat)
    print(annSav)
    return annSav

def savingsNeeded(final,r,k):
    rAdjust = r/100
    actual = 0
    A = 1000
    while actual < final:
        actual = float(savings(A,r,k))
        A += 1000
    print('If you save ',A-1000,' for 20 years with 5% interest you will have more than ',final,'.',sep='')


def prettyShit(liste):
    n = 0
    for i in liste:
        n += 1
        if n == 10:
            print('Year:',n,4*' ','Sum:',i)
        else:
            print('Year:',n,5*' ','Sum:',i)


savings(6000,5,20)          #assignment a/b
annualSavings(1000,6,10)        #assignment c
prettyShit(annualSavings(1000,6,10))    #do not understand assignment d...
savingsNeeded(15000,5,20)           #assignment d



