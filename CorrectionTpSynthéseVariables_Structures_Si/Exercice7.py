conso=float(input("saisir la consommation enKW : "))
if conso<=100:
    tarif=conso*0.80
elif conso<=300:
    tarif=0.80*100+(conso-100)*1.20
else:
    tarif=0.80*100+200*1.20+(conso-300)*1.50
    if conso>500:
        print("attention !!! ")
print(f"qte consommée : {conso}\ntarif : {tarif} DH")