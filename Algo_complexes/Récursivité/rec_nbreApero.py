## Connaitre le nombre de tchin dans un apéro

def tchin(n) :
    if n == 2 :
        return 1
    else :
        return (tchin(n-1) + n) - 1

print(tchin(5))