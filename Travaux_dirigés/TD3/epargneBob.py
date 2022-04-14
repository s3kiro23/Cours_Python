#Sans Fonction

solde=200
t=0.02
interet=solde*t
année= int(input("Entrez le nombre d'années voulues :"))

for i in range(année):
    solde=solde+interet
    interet=solde*t
    print("Solde à l'année n +",i+1,":",solde)

#Avec fonction

def solde() :
    solde=200
    t=0.02
    interet=solde*t
    année = int(input("Entrez le nombre d'années voulue :"))

    for i in range(année) :
        solde=solde+interet
        interet=solde*t
        print("Solde à l'année n +",i+1,":",solde)

solde()