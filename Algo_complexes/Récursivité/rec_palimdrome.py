## Afficher si le mot saisi est un palindrome ou non

def palin(n) :
    
    if n == [] or len(n) <= 1 :
        return True
    elif n[0] != n[-1] :
        return False
    else : 
        return palin(n[1:-1])

print(palin(input("Saisissez votre mot :")))