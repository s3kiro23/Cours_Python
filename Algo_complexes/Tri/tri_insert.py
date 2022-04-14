l=[21,5,8,7,69,5,4,2,58,6,87,1,12,65,74,89,65,4]

def tri(l):
    for i in range(len(l)): #on parcourt la liste
        item = l[i]         #un élément de la liste
        j = i
        while j>0 and l[j-1] > item: #tant qu'on n'a pas atteint le début ou un élément plus petit
            l[j] = l[j-1]   #on décale l'élément trouvé vers la droite
            j=j-1
        l[j]=item
        print(l)
print(tri(l))