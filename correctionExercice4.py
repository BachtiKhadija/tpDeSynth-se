#Question1
"""age=int(input("saisir votre age : "))
if age>=18:
    print("vous avez l'accés !!!")
else:
    print("Tu es toujours mineur !!!")"""
#***********************************************Question2 ******************************************
#[10,20] => range(10,21)  => [10,21[
#a apparentient a [10,20]
#a in range(10,21)
"""moy=float(input("saisir la moyenne : "))
if moy in range(10,21):
    print("tu es admis")
else:
    print("tu es non admis")"""
    
#***********************************************Question3 ******************************************    
"""x=int(input("saisir un nombre : "))

if x in range(0,1000000):
    print(f"{x} est positif ou nul")
else:
    print("{} est negatif".format(x))  """

#n=int(input("saisir un nombre : "))

"""if n%2==0:
    print(f"{n} est pair ")
else:
    print("{} est impair".format(n)) """
    
#print(f"{n} est pair ") if n%2==0 else print("{} est impair".format(n)) 
##***********************************************Question6 ******************************************  
"""note,disc=float(input("note : ")),float(input("note : "))

if note>=10 and disc<=5:
    print("message")"""
nbr=int(input("saisir un nbr : "))
if nbr in range(1,11) or nbr==20:
    print("OK !!!")
else:
    print("Error !!!")