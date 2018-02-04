def main():
    nok = int(input("Hvor mange NOK har du?"))
    valuta = valutaVelger()
    output = penger(nok, valuta, stedVelger(), tidVelger())
    print("Du får da:",format(output, ',.2f')+valuta)
      
def penger(nok, valuta, sted, tid):
    pengerUt = 0
    if tid == "Nå":
        if sted == "Bank":
            if valuta == "EUR":
               pengerUt = (nok / 8.7) * 0.95
            elif valuta == "GBP":
               pengerUt = (nok / 11.9) * 0.95
            else:
                pengerUt = (nok / 0.14) * 0.95  
        else:
            if valuta == "EUR":
               pengerUt = (nok / 8.7) * 0.9
            elif valuta == "GBP":
               pengerUt = (nok / 11.9) * 0.9
            else:
                pengerUt = (nok / 0.14) * 0.9
    else:
        if sted == "Bank":
            if valuta == "EUR":
               pengerUt = (nok / 9.1) * 0.95
            elif valuta == "GBP":
               pengerUt = (nok / 12.5) * 0.95
            else:
                pengerUt = (nok / 0.15) * 0.95  
        else:
            if valuta == "EUR":
               pengerUt = (nok / 9.1) * 0.9
            elif valuta == "GBP":
               pengerUt = (nok / 12.5) * 0.9
            else:
                pengerUt = (nok / 0.15) * 0.9
    return pengerUt
               
def valutaVelger():
    valuta = input("Hvilken valuta vil du veksle til? [EUR/GBP/RUB?]")
    if valuta == "EUR":
        print("Du vil veksle fra NOK til EUR.")
    elif valuta == "GBP":
            print("Du vil veksle fra NOK til GBP.")
    elif valuta == "RUB":
            print("Du vil veksle fra NOK til RUB.")
    else:
        valuta = valutaVelger()
    return valuta

def stedVelger():
    sted = input("Hvor vil du veksle pengene? [Bank/Flyplass?]")
    if sted == "Bank":
        print("Du har valgt å veksle i bank.")
    elif sted == "Flyplass":
        print("Du har valgt å veksle på flyplass.")
    else:
        sted = stedVelger()
    return sted

def tidVelger():
    tid = input("Når vil du veksle pengene dine? [Nå/Senere?]")
    if tid == "Nå":
        print("Du vil veksle pengene nå.")
    elif tid == "Senere":
        print("Du vil veksle pengene senere.")
    else:
        tid = tidVelger()
    return tid

main()
