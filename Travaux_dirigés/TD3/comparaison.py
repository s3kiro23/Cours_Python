l1=[1,2,3,4,5,6,7,8,9]
l2=[1,2,3,4,5,4,7,8,9]
t=True
i=1

if(len(l1)!=len(l2)):
	t=False
while(t and i < len(l1)):
	if l1[i]!=l2[i]:
		t = False
	i= i +1
if t :
	print("Les 2 listes sont identiques")
else:
	print("Les 2 listes sont différentes")