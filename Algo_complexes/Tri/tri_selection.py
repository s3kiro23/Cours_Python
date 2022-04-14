
l=[1,5,8,7,69,5,4,2,58,6,87,1,12,65,74,89,65,4]

def mini(l):
	r=0
	for i in range(len(l)):
		if l[r]>l[i]:
			r=i
	return r

def echange(l,i,j):
	t =0
	t = l[i]
	l[i] = l[j]
	l[j] = t
	return l
				 
def selection(l):
	
	l_nontrie = 0
	while l_nontrie < len(l):
		m=mini(l[l_nontrie:])
		l=echange(l,l_nontrie,m+l_nontrie)
		l_nontrie +=1
		
	print(l)

selection(l)
