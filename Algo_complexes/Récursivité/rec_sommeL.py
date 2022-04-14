## Avec une somme de liste

def sommel(l):
    if len(l) == 0:
        return 0
    else:
        return l[0] + sommel(l[1:])

l=[1,1,1,2,2,3]
print(sommel(l))