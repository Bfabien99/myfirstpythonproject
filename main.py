# Refactorisations
def affiche_info(_nom, _age, _taille=0):
    print()
    print("Tu t'appelles " + str(_nom) + " et tu as " + str(_age) + " ans")
    print(f"Tu auras {_age + 1} ans dans un an")

    if _age < 10:
        print("Vous êtes enfant")
    elif _age > 60:
        print("Vous êtes vieux")
    elif _age == 17:
        print("Vous êtes presque majeur")
    elif 12 <= _age < 18:
        print("Vous êtes adolescant")
    elif _age == 18:
        print("Vous êtes tout juste majeur : Félicitation")
    elif _age > 18:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")

    # afficher la taille
    if not _taille == 0:
        print("Votre taille : %s m" % _taille)


def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est ton nom ? ")

    return reponse_nom


def demander_age():
    age_int = 0
    while age_int == 0:
        age_str = input("Quel est ton âge ? ")

        try:
            age_int = int(age_str)
        except:
            print("ERROR: Vous devez entrer un nombre pour l'âge")

    return age_int


# On demande le nom de la personne
# nom = demander_nom()

# On demande l'âge de la personne
# age = demander_age()

# On affiche les infos de la personne de la personne
# affiche_info(nom, age)

NB_PERSONNES = 1
# La boucle for
for i in range(0, NB_PERSONNES):
    nom = "personne" + str(i+1)
    age = demander_age()
    affiche_info(nom, age)