"""
les fonctions

# afficher une valeur, un message
print()

# recevoir une valeur
input()

# retourne la longueur d'une chaîne de caractère
len()
"""


def est_majeur(_age):
    if _age <= 0:
        return False
    if _age >= 18:
        return True
    return False


def afficher_infos_personne(_nom="", _age=0):
    if _nom == "":
        print(f"Vous n'avez pas donné de nom")
        return
    if _age == 0:
        print(f"Vous n'avez pas donné d'âge")
        return

    print(f"Ton nom est {_nom}, ton age est {_age} ans")
    print(f"Ton nom comporte {len(_nom)} caractères")
    if est_majeur(_age):
        print('Vous êtes majeur')
    else:
        print('Vous êtes mineur')


print("Début du programme")
age = 0
nom = "zz"
afficher_infos_personne(nom, age)

print("Fin du programme")