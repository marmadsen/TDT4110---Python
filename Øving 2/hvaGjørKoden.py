'''
x = 2
y = input (’Skriv inn et tall ")
    z = x // y
print (z)
'''

# x og y kalles for variabler
#fikset kode:

x = 2
y = int(input("Skriv inn et tall: "))
z = x // y
print (z)


a = 2
b = 3
if (b<a or not b%a): #hvis b er mindre enn a eller større enn b modulo a 
    b = a+b          #Så er b = a+b
else:
    a = a*b          #hvis ikke så er a = a*b
print("a: ",a) #her skriver den 6
print("b: ",b) #her skriver den 3
