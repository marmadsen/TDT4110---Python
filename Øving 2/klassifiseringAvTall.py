def main():
    tall = input("Oppgi et tall:")
    if wholeNumber(tall) == 1:
        print("Dette er et heltall.")
    else:
        print("Dette er ikke et heltall.")
    if evenNumber(tall) == 1:
        print("Dette er et partall.")
    else:
        print("Dette er ikke et partall.")
    fortegn(tall)
    
    
    
def wholeNumber(tall):
    try:
        heltall = int(tall)
        heltall_tf = 1
    except ValueError:
        heltall_tf = 0
    return heltall_tf

def evenNumber(tall):
    eventest = float(tall)/2
    print(eventest)
    try:
        even = int(eventest)    #Her skjer det noe jævla rart.
        even_tf = 1
    except ValueError:
        even_tf = 0
    return even_tf

def fortegn(tall):
    if float(tall) < 0:
        print("Tallet er negativt.")
    else:
        print("Tallet er positivt.")
        

main()

    
