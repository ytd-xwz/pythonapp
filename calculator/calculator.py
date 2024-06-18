résultat=0
    
def addition():
    b=int(input("(première valeur)"))
    print("+")
    c=int(input("(deuxième valeur)"))
    résultat=b+c
    print(résultat)

def difference():
    b=int(input("(première valeur)"))
    print("-")
    c=int(input("(deuxième valeur)"))
    résultat=b-c
    print(résultat)

def produit():
    b=int(input("(première valeur)"))
    print("*")
    c=int(input("(deuxième valeur)"))
    résultat=b*c
    print(résultat)

def division():
    b=int(input("(première valeur)"))
    print("/")
    c=int(input("(deuxième valeur)"))
    résultat=b/c
    print(résultat)

a=input("quelle est l'opération que tu veut faire?")
if a==("+"):
    addition()
if a==("-"):
    difference()
if a==("*"):
    produit()
if a==("/"):
    division()