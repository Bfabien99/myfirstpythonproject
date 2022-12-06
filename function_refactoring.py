# Refactoring du code main.py
# recuperer les informations de la personne
def recuperer_infos_personne(_numero_personne: int):
    _nom = input(f"Nom de la personne {_numero_personne} : ")
    _age = input(f"Age de la personne {_numero_personne} : ")
    return _nom, int(_age)


# vérifier si la personne est majeure ou pas
def est_majeur(_age: int) -> bool:
    if _age <= 0:
        return False
    if _age >= 18:
        return True
    return False


# afficher les informations de la personne
def afficher_infos_personne(_numero_personne, _nom, _age: int):
    print(f"La personne {_numero_personne} est {_nom}, et son age est {_age}")
    if est_majeur(_age):
        print('Vous êtes majeur')
    else:
        print('Vous êtes mineur')


"""
recuperer et afficher les informations de la personne
en appellant les fonctions recuperer_infos_personne() et
afficher_infos_personne() 
"""


def recuperer_et_afficher_infos_personnes(_numero_personne):
    _nom, _age = recuperer_infos_personne(_numero_personne)
    afficher_infos_personne(_numero_personne, _nom, _age)


# Test
NOMBRE_DE_PERSONNES = 1
for i in range(NOMBRE_DE_PERSONNES):
    recuperer_et_afficher_infos_personnes(i+1)