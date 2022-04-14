import random

print("---------- SHI FU MI -----------")
pi="pierre"
f="feuille"
c="ciseaux"
user_nbr_round= int(input("\nEn combien de manches ?"))
nbr_round=0
scorePL=0
scorecpu=0

while nbr_round < user_nbr_round:
    PL= input("\nPierre... Feuille... Ciseaux...")
    if PL == pi or PL == f or PL == c:
        print("-----------------------------------")
        cpu= random.choice([pi,f,c])
        nbr_round+=1
        print(cpu)
        if PL == cpu:
            print("\nMatch nul ! Manche",nbr_round,"sur", user_nbr_round)
        elif PL == pi and cpu == c:
            scorePL+=1
            print("\nLe joueur gagne ! Manche",nbr_round,"sur", user_nbr_round)
        elif PL == f and cpu == pi:
            scorePL+=1
            print("\nLe joueur gagne ! Manche",nbr_round,"sur", user_nbr_round)
        elif PL == c and cpu == f:
            scorePL+=1
            print("\nLe joueur gagne ! Manche",nbr_round,"sur", user_nbr_round)
        else:
            scorecpu+=1
            print("\nL'ordinateur gagne ! Manche",nbr_round,"sur", user_nbr_round)
        
if scorePL > scorecpu:
    print("\nBravo, tu as gagné la partie ! :)  Score =",scorePL,"à",scorecpu)
elif scorecpu > scorePL:
    print("\nPerdu, le CPU gagne la partie ! :(  Score =",scorecpu,"à",scorePL)
else:
    print("\nPartie fini sur une égalité   :/   Score =",scorePL,"à",scorecpu)