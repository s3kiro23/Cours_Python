## Avec récursivité

def recurse(l,u) :

    if l == [] :
        return 0
    if l[0] == u :
        return 1 + recurse(l[1:],u)
    else :
        return recurse(l[1:],u)

print(recurse([1,2,3,3,4,9,0,3,3,4],int(input("Saisissez votre valeur :"))))