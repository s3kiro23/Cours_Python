#Sans fonction

n= input("Entrez votre mot de passe :")
mdp= "zaire"
count=3

while n != mdp and count > 0:
    count-=1
    print("Erreur de mot de passe ! - Tentative restante =",count+1)
    n= input("Entrez votre mot de passe :")

if n == mdp:
        print("Bienvenue dans votre espace !")

else:
    print("Accès verrouillé ! - Contactez un admin.")


#Avec fonction

def login() :
    mdp= "zaire"
    count=3
    a= input("Entrez votre mot de passe:")
    
    while a != mdp and count > 0 :
        count=count-1
        print("Mauvais mdp - Tentative restante =",count+1)
        a= input("Entrez votre mot de passe:")
 
    if a == mdp :
        print("Bienvenue dans votre espace personnel")
   
    else :
        print("Accès verrouillé - Contactez un admin")

login()