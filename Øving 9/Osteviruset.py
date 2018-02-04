__author__ = 'Martin'

cheeses = {
'cheddar':
('A235-4', 'A236-1', 'A236-2', 'A236-3', 'A236-5', 'C31-1', 'C31-2'),
'mozarella':
('Q456-9', 'Q456-8', 'A234-5', 'Q457-1', 'Q457-2'),
'gombost':
('ZLAFS55-4', 'ZLAFS55-9', 'GOMBOS-7', 'A236-4'),
'geitost':
('SPAZ-1', 'SPAZ-3', 'EMACS45-0'),
'port salut':
('B15-1', 'B15-2', 'B15-3', 'B15-4', 'B16-1', 'B16-2', 'B16-4'),
'camembert':
('A243-1', 'A234-2', 'A234-3', 'A234-4', 'A235-1', 'A235-2', 'A235-3'),
'ridder':
('GOMBOS-4', 'B16-3'),
}



#A234 til A235, B13 til B15, og C31 are infected, identify the types of cheese and print them
def infectedShelves(cheeses):
    infected = []
    for key in cheeses:
        for i in cheeses[key]:
            if i.split('-')[0] in ['A234','A235','B13','B14','B15','C31']:
            #if 'A234' in i or 'A235' in i or 'B13' in i  or 'B14' in i or 'B15' in i or 'C31' in i:
               if key not in infected:
                   infected.append(key)
    print('These cheeses are infected:')
    for i in infected:
        print(i)
    return infected

def cheeseToSell(infected):
    types = cheeses.keys()
    print("These cheeses can be sold:")
    for i in types:
        if i not in infected:
            print(i)



print(cheeses['port salut'])    #Oppgave a


#infectedShelves(cheeses)        #Oppgave b
#cheeseToSell(infectedShelves(cheeses))
