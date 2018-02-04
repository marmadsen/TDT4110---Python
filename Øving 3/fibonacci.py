k = int(input("Velg din k-verdi: "))
i = 0
fn_2 = 0
fn_1 = 1
fnsum = 1
liste = [0,1]
for i in range(2,k + 1):
    fn = fn_2 + fn_1
    fn_2 = fn_1
    fn_1 = fn
    fnsum += fn
    liste.append(fn)
    
print(i+1, '\t', fn, '\t', fnsum)

print(liste)

#Fikk ikke summen av k fibonaccitall til å fungere...
#Eventuelt bruk Binet's formel:
print("Binet's versjonen:")

fn_b = format((((1+(5**(1/2)))**k) - ((1-(5**(1/2)))**k))/((2**k)*(5**(1/2))), '.0f')
print(fn_b)
fn_b_sum = format((((1+(5**(1/2)))**(k+2)) - ((1-(5**(1/2)))**k))/((2**(k+2))*(5**(1/2))) - 1, '.0f')
print(fn_b_sum)
