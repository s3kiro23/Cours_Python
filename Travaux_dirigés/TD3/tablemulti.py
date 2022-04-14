##Sans fonction

n= int(input("Entrez un chiffre :"))
r=0
a=9

for i in range(1,a+1):
    r=n*i
    print(n,"x",i,"=",r)

##Avec fonction
###Méthode 1 

def table() :
    n= int(input("Entrez un chiffre :"))
    r=0
    a=9

    for i in range(1,a+1):
        r=n*i
        print(n,"x",i,"=",r)
        
table()

###Methode 2

def table(n) :
    r=0
    a=9
    for i in range(1,a+1):
        r = n*i
        print(n,"x",i,"=",r)
        
x= int(input("Entrez une valeur :"))
table(x)