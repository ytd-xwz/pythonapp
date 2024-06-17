résultat=0
a=input("quelle est l'opération que tu veut faire?")
if a==("+"):
    b=int(input("(première valeur)"))
    print("+")
    c=int(input("(deuxième valeur)"))
    résultat=b+c
    print(résultat)
elif a==("-"):
    b=int(input("(première valeur)"))
    print("-")
    c=int(input("(deuxième valeur)"))
    résultat=b-c
    print(résultat)
elif a==("*"):
    b=int(input("(première valeur)"))
    print("*")
    c=int(input("(deuxième valeur)"))
    résultat=b*c
    print(résultat)
else:
    b=int(input("(première valeur)"))
    print("/")
    c=int(input("(deuxième valeur)"))
    résultat=b/c
    print(résultat)