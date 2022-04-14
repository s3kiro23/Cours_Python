## CAS USER VS PC ##

import random

def seek():
    count=0
    n= int(input("Entrez votre prix :"))
    numrd= random.choice(range(101))
    
    while n != numrd:
        if n < numrd:
            count+=1
            print("C'est plus !")
            n= int(input("Entrez votre prix :"))
        if n > numrd:
            count+=1
            print("C'est moins !")
            n= int(input("Entrez votre prix :"))
    else :
        n == numrd
        print("Bravo, vous avez trouvé le juste prix !")
        print("Votre score =",count)
        
seek()

## CAS PC VS USER ##

import random

def seek():
    p= int(input("Entrez un prix entre 1 et 100 :"))
    count=0
    l= list(range(101))
    numrd=-1

    while(numrd != p):
        numrd=random.choice(l)
        count+=1
        if(numrd < p):
            l=l[l.index(numrd):]
            print(numrd,"\nC'est plus !")
        if(numrd > p):
            l=l[:l.index(numrd)]
            print(numrd,"\nC'est moins !")

    print(numrd,"\n","\nKek World is mine !\nScore =",count)

seek() 