l=[1,5,8,7,69,5,4,2,58,6,87,1,12,65,74,89,65,4]

def swap(l):

    for i in range(len(l)):
        for j in range(len(l)-1-i):
            if l[j+1] < l[j]:
                tmp = l[j]
                l[j] = l[j+1]
                l[j+1] = tmp
        print(l[:len(l)-1-i])
    return l
print(swap(l))