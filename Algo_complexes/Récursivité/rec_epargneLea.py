### Epargne Lea

def epargneLea(n):
    if n == 0:
        return 200
    else:
        return 2*n + epargneLea(n-1)

print(epargneLea(5))