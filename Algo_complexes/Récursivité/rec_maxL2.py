## Maximum d'une liste

def maxi(n) :

    if len(n) == 1 :
        return n[0]
    else:
        if n[0]>maxi(n[1:]):
            return n[0]
        return maxi(n[1:])      

print(maxi([1,5,9,2,10]))