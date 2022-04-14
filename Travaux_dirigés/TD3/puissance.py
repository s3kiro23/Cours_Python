#Avec la méthode 'For in'

x= int(input("Entrez votre valeur :"))
n= int(input("Entrez votre valeur :"))
a=1

for i in range(n):
    a=a*x
    print(x,"^",i,"=",a)

#Avec la méthode 'While'

x= int(input("Entrez votre valeur :"))
n= int(input("Entrez votre valeur :"))
r=1
i=0

while(i < n):
    r=r*x
    i=i+1
    print(x,"^",i+1,"=",a)


##Avec Fonction

def puissance(a,b) :
    r=1
    i=0
    while i < b :
        r=r*a
        i=i+1
    print(a,"^",b,"=",r)    
    return r
        
x= int(input("Entrez votre valeur"))
y= int(input("Entrez votre valeur"))
t=puissance(x,y)
print(t)