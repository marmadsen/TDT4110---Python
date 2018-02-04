print("Summen av tallene fra 1 til 100:")
total = 0
for i in range(101):
   total += i

print(total)

totalProd = 1
x = 1
while totalProd <= 1000:
    totalProd *= x
    x += 1

print("Produktet av tallene fra 1 til x, stopper når produktet > 1000:")
print(totalProd)

def question():
    svar = input("Hva er 8 + 2?: ")
    while svar != "10":
        print("Svaret er feil, prøv igjen!")
        svar = input("Hva er 8 + 2?: ")
        #question()
        #break
    print("Riktig svar!")

question()
