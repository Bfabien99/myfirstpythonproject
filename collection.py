# Collections: Tableaux, Listes, Tuples
# Tuple (): immutable -> Non modifiable
# Liste []: mutable -> Modifiable

# len() pour avoir la table d'un tableau
# .sort() pour ordonner un tableau

# tuple
groupe1 = ("rameaux", "sam", "affou", "kabore", "fabien")
""" 
for i in range(0, len(groupe1)):
    print("-->", groupe1[i]) 
"""
"""
for i in groupe2:
    print(i, "-->", len(i), " lettres")
"""

# liste
# .append() pour ajouter un element dans une liste
# del groupe2[1] supprime l'élément d'indice 1 du tableau
groupe2 = ["parfait", "anicet", "franck", "richard", "jean-philipe"]
nouvelle_personne = "yve"

groupe2.append(nouvelle_personne)
"""
for person in groupe2:
    print(person)
"""


def afficher_personnes(liste: list | tuple):
    i = 1
    for person in liste:
        print(i, "-", person)
        i += 1


afficher_personnes(groupe2)