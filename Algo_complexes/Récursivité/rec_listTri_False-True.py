##Vérifier si une liste est triée

def l_tri(n) :
    
    if len(n) == 1 :
        return True
    elif n[0] > n[1] :
        return False
    else :
        return l_tri(n[1:])

print(l_tri([1,2,7,9,100,25,67]))