## Comparaison de deux listes

def compare(m,n):
    if m == [] and n == [] :
        return True
    elif len(m) != len(n) :
        return False
    elif m[0] != n[0] :
        return False
    else :
        return compare(m[1:],n[1:])

print(compare([1,2,3,5,7,9,5],[1,2,3,5,7,9]))