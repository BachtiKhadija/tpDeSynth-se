nom,qte,prix="Souris",20,120.00
facture=f"{'='*10}COMMANDE{'='*10}\n{nom}|{qte}|{prix}\nStatus : Calculer avec succés"
print(facture);f=open("facture.txt","w")
f.write(facture)
print("saved !!!")
f.close()