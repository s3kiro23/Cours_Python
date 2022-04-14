## Afficher un triangle rectangle

def trianglerect(n) :
    if n == 1 :
        return "*"
    else:
        return trianglerect(n-1) + "\n" + n*"*"

print(trianglerect(4))