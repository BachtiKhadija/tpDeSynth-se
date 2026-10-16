age,carte=int(input("age ? ")),input("cart ?  ")
if carte=="123456A" and age>=16:
    print("autorisé")
elif age>=16 and not(carte=="123456A"):
    print("renouvle ta carte !!!")
else:
    print("non autorisé !!!")
    