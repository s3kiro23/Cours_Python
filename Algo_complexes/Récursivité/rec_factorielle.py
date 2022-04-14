### Factorielle

def factor(n):
    if n == 1:
        return 1
    else:
        s = n * factor(n-1)  
        return s
    
print(factor(5))