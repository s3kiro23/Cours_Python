## Récursivité avec les puissances

def puissance(a,n):
    if n == 0:
        s = 1
    else:
        s = a* puissance(a, n-1)
        print(s)
    return s
    
print(puissance(10,4))

