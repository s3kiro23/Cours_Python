#Sans fonction

solde=200
age= int(input("Entre ton âge :"))

for i in range(age):
    solde=solde+2*i
    print("Solde du compte en fonction de ton âge",i,"=",solde)

#Avec fonction

def solde() :
    n= int(input("Entre ton âge :"))
    a= 200

    for i in range(n) :
        a= a + 2*i
        print("Solde du compte en fonction de ton âge",i,":",a)
        
solde()