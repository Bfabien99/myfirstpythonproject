from art import *
# CONVERTISSEUR POUCE -> CM, CM -> POUCE
# Ma version ...


def demander_chiffre(question):

    print(question)
    reponse_str = input("choix: ")
    if reponse_str == "r":
        converter()
    if reponse_str == "q":
        tprint("BYE !")
        exit(0)
    try:
        reponse_int = float(reponse_str)

        if reponse_int >= 0:
            return reponse_int
        print(f"Entrer un chiffre supérieur à 0")
    except:
        print("Erreur: Entrer un chiffre")
    return demander_chiffre(question)


def pouce_cm():
    _valeur = demander_chiffre("Donner la valeur en pouces ; 'q' pour quitter ou 'r' pour revenir à l'accueil")
    print(_valeur, "pouces =", _valeur * 2.54, "cm")
    while _valeur:
        pouce_cm()


def cm_pouce():
    _valeur = demander_chiffre("Donner la valeur en cm ; 'q' pour quitter ou 'r' pour revenir à l'accueil")
    print(_valeur, "cm =", _valeur / 0.394, "pouces")
    while _valeur:
        cm_pouce()


def demander_convertisseur():

    reponse_str = input("Votre choix (1 ou 2): ")
    try:
        reponse_int = int(reponse_str)
        if 1 <= reponse_int <= 2:
            return reponse_int

        print(f"Faites un choix entre 1 et 2")
    except:
        print("Erreur: Entrer un chiffre")
    return demander_convertisseur()


def converter():
    print("Ce programme vous permet d'éffectuer des convers d'unités")
    print('''
    1 - Pouces vers cm
    2 - cm vers pouces
    ''')
    choix = demander_convertisseur()
    if choix == 1:
        tprint("pouces -> cm")
        pouce_cm()
    if choix == 2:
        tprint("cm -> pouces")
        cm_pouce()


converter()
# Fin ma version ...