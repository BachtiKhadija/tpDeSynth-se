print("*"*40,"Menu","*"*40)
print("6.taper 6\n7.Taper 7 \n10.taper 10")
choix=int(input("saisir votre choix : "))
if choix==6:
    age=int(input("votre age : "))
    print("vous etes majeur") if age>=18 else print("tu es mineur")
elif choix==7:
    nbr=int(input("saisir un nbr : "))
    print("pair") if nbr%2==0 else print("impair")
elif choix==10:
    prix=float(input("saisir un prix : "))
    if prix>=500:
        print("livraison gratuite !!! ")
else:
    print("choix invalide !!!!!!")
        
    
