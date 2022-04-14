import random

def mini(l):  # recherche l'index de l'element qui a la plus petite valeure
    r = 0
    for i in range(len(l)):
        if l[r] > l[i]:
            r = i
    return r


def echange(l, i, j):  # echange les element des index i et j dans la liste l
    t = 0
    t = l[i]
    l[i] = l[j]
    l[j] = t
    return l


def rec_select(l):
    if len(l) == 1:
        return l
    else:
        l = echange(l, mini(l), 0)
        return [l[0]] + rec_select(l[1:])


list_random= [random.randint(-4, 50) for x in range(10)]
print(rec_select(list_random))
