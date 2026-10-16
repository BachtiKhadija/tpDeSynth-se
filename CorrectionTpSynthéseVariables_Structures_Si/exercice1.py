nom,prix,qte,disponible="clavier",249.90,12,True
#**********************************question1
#print("nom :",nom,"- typde de nom : ",type(nom))#sep=" " end=\n
#print(f"nom = {nom} - type de nom = {type(nom)}")
#print("nom = {0} - type de nom = {1}".format(nom,type(nom)))
#question 2 et 3
stock=prix*qte
#print(f"nom : {nom} ** prix : {prix} ** qte: {qte} ** pht : {stock}")
#question4 
prix_promo=prix*.85
print(f"prixPromo: {prix_promo}",f"type :{type(prix_promo)}",end="*"*5)
print(f"qte: {qte}",f"type :{type(qte)}",end="*"*5);print(f"disponible: {disponible}",f"type :{type(disponible)}")