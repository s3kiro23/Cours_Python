###Epargne Bob

def epargneBob(n):
    if n == 0 :
        return 200
    else :
        return 1.02*epargneBob(n-1)

print(epargneBob(50))