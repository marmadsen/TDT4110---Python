def main():
    print("Et program for å beregne nettopris på bil:")
    bil = input("Navn på bilen: ")
    brutto = float(input("Bruttopris på bilen [kr]: "))
    vekt = float(input("Vekt på bilen [kg]: "))
    hk = float(input("Antall hestekrefter på bilen [hk]: "))
    co2 = float(input("Antall gram Co2-utslipp på bilen [gram]: "))
    motorv = float(input("Motorvolum på bilen [liter]: "))
    nettopris(brutto, vekt, hk, co2, motorv)

def nettopris(brutto, vekt, hk, co2, motorv):
    vekt_p = brutto * vekt * 0.00034
    hk_p = brutto * hk * 0.00015
    co2_p = brutto * co2 * 0.004
    volum_p = 0.00055
    netto_p = brutto + vekt_p + hk_p + co2_p + volum_p
    print(format(netto_p,'.2f'))

main()
