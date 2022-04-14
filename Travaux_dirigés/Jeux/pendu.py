import random

words=["ordinateur","moto","musique","jeuxvideo","groupe","télévision","guitare"]
random_word=random.choice(words)
_round=7
_lettersfound=""
_hiddenword=""

for l in random_word:
    _hiddenword += "_ "
    
print(">> Bienvenue dans le pendu ! <<")

while _round > 0:
    print("\n Mot à deviner :",_hiddenword)
    user_choice=input("\nChoisissez une lettre :")[0:1].lower()
    
    if user_choice in random_word:
        _lettersfound+=user_choice
        print("\nBien joué, vous avez trouvé une lettre !")
    else:
        _round-=1
        print("\nNope !  Il vous reste",_round,"tentatives.\n")
        if _round==0:
            print(" ==========Y= ")
        if _round<=1:
            print(" ||/       |  ")
        if _round<=2:
            print(" ||        0  ")
        if _round<=3:
            print(" ||       /|\ ")
        if _round<=4:
            print(" ||       /|  ")
        if _round<=5:                    
            print("/||           ")
        if _round<=6:
            print("==============\n")
           
    _hiddenword=""
    for x in random_word:
        if x in _lettersfound:
            _hiddenword += x + " "
        else:
            _hiddenword += "_ "
            
    if "_" not in _hiddenword:
        print(">>> Gagné ! <<<")
        break

print("\n  * Fin de la partie *  ")