# LISTES - EXERCICES :
# DEMANDER NOMS DE PERSONNES
# nom et age ->> input
# boucle infinie, sort quand le nom == "" => break

noms = []

"""
def demander_nom_personne():
    nom = input("Entrez un nom: ")
    while not nom == "":
        noms.append(nom)
        nom = input("Entrez un nom: ")

    for _nom in noms:
        print(_nom)

demander_nom_personne()
"""
while True:
    nom = input("Entrez un nom: ")
    if nom == "":
        break
    noms.append(nom)

noms.sort()
for _nom in noms:
    print(_nom)