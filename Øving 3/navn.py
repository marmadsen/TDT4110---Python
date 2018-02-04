fornavn = ['johan', 'eli', 'mats', 'lene', 'simon', 'inger', 'henrik', 'mari', 'per']
etternavn = ['Hag', 'Hag', 'Basmestad', 'Grimlavaag', 'Kleivesund', 'Fintenes', 'Svalesand', 'Molteby', 'Hegesen']


for i in range(len(fornavn)):
    navn = fornavn[i].title() +" "+ etternavn[i] #kunne prøvd .capitalize
    print(navn)

print("-----------------------")
for i in range(len(fornavn)):
    navn = fornavn[i].title() +" "+ etternavn[len(etternavn)-1-i]
    print(navn)

#Listene har 9 elementer og det "midterste" navnet vil bli likt begge veier

