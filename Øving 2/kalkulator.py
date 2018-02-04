def main(tall1, tall2):
    ov = operatorvelger()
    if ov == "+":
        print(format(pluss(tall1, tall2),',.6f'))
    elif ov == "-":
        print(format(minus(tall1, tall2),',.6f'))
    elif ov == "*":
        print(format(gange(tall1, tall2),',.6f'))
    else:
        print(format(dele(tall1, tall2),',.6f'))

def operatorvelger():
    operator = input("Hvilken operator ønsker du? [+,-,*,/]")
    if operator != "+" and (operator != "-") and (not operator == "*") and (not operator == "/"):
        operator = operatorvelger()
        return operator
    else:
        return operator

def pluss(tall1, tall2):
    return tall1 + tall2

def minus(tall1, tall2):
    return tall1 - tall2

def gange(tall1, tall2):
    return tall1 * tall2

def dele(tall1, tall2):
    return tall1 / tall2


main(float(input("Hva er det første tallet?")),float(input("Hva er det andre tallet?")))
