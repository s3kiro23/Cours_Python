import random

def swap(liste, i, j):  # echange les element des index i et j dans la liste l

    tmp = liste[i]
    liste[i] = liste[j]
    liste[j] = tmp
    return liste


def triBubble(l):
    if len(l) == 1:
        return l
    else:
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                l = swap(l, i, i+1)
        return triBubble(l[:-1]) + [l[-1]]

list_random = [random.randint(-3,101) for x in range(10)]
print(list_random,"\n")
print(triBubble(list_random))
