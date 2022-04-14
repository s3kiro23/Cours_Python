#Sans fonction

n= int(input("Entrez une valeur :"))
y=1

for i in range(1,n+1):
    y=y*i
    print(n,"!","=",y)

#Avec fonction
##Methode 1 : valeur spécifiée dans la boucle
    
def fact() :
	n= int(input("Entrez une valeur :"))
	y=1

	for i in range(1,n+1):
    		y=y*i
    		print(n,"!","=",y)
    
fact()

##Methode 2 : valeur spécifié hors de la boucle

def fact(n) :
    y=1
    for i in range(1,n+1):
        y=y*i
        print(n,"! =",y)

x= int(input("Entrez une valeur :"))
fact(x)