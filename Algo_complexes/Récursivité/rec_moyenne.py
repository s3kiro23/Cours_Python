## Moyenne d'une liste

def average(n):
    if n == [] :
        return 0
    else :
        return (average(n[1:])*len(n[1:]) + n[0]) // len(n)

print(average([1,4,3,7,9]))