## Avec une sommme

def somme(n):
    if n == 0:
        s = 1
    else:
        s = n + somme(n-1)
        return s
print(somme(5))