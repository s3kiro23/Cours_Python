## Somme sur une liste

def sommel(n):
    if len(n) == 0:
        return 0
    else:
        return n[0] + sommel(n[1:])

print(sommel([1,4,5,6]))