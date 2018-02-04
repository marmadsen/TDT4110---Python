import math

print("Her skal vi finne arealet til et tetraeder basert på en verdi h som ikke jeg vet hvor kommer fra...")

h = int(input("skriv din h-verdi her: "))

a = (3*h/math.sqrt(6))

area = (math.pow(a,2)) * (math.sqrt(3)) #evt. a**2

print("Arealet til tetraederet er:",format(area,'10.3f'))

volume = (math.sqrt(2) * math.pow(a,3))/(12)

print("Volumet til tetraederet er:",format(volume,'10.3f'))
