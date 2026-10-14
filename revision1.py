
#ceci est un commentaire monoligne 

"""
var a,b,som,prod:entier
Debut
  Ecrire "saisir la premiére valeur"
  lire a
  Ecrire "saisir la deuxiéme valeur"
  lire b
  som=a+b
  prod=a*b 
  Ecrire "la somme est ",som
  Ecrire "le produit est ",prod
Fin

"""
a=int(input("saisir la premiére valeur ")) 

print("a = ",a,"type de a ",type(a))

b=int(input("saisir la deuxiéme valeur "))
print("b = ",b,"type de b ",type(b))
som=a+b
prod=a*b 
print("la somme est ",som)
print("le produit est ",prod)
