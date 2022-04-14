## Avec un max d'une liste

def maxi(l):
    if len(l) == 1:
        return l[0]
    else:
        if(l[0]>maxi(l[1:])):
            return l[0]
        else:
            return maxi(l[1:])
l=[1,4,4,8,5,9,10,54,98,7,5,6,25,44,3]
print(maxi(l))