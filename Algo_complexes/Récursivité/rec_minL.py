## Minimum d'une liste

def mini(n) :

    if len(n) == 1 :
        return n[0]
    else:
        if n[0]<mini(n[1:]):
            return n[0]
        else:
            return mini(n[1:])

print (mini([1,3,2,5,10]))