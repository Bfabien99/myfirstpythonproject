groupe1 = ("0", "1", "2", "3", "4")


def obtenir_informations():
    return "Melanie", 1  # retoune un tuple


def afficher_informations(_nom, _age):
    print(f"Informations: Nom : {_nom}, age: {_age}")


"""
nom, age = obtenir_informations()
afficher_informations(nom, age)
"""
infos = obtenir_informations()
# unpack du tuple
afficher_informations(*infos)  # * permet de parcourrir le tuple

# slice[start:stop:step]
"""
# start -> le point de départ
# stop -> le point d'arrêt
# step -> le saut
"""
for i in groupe1[::2]:
    print(i)  # 0, 2, 4
for i in groupe1[1:3]:
    print(i)  # 1, 2
for i in groupe1[0:4:3]:
    print(i)  # 0, 3
for i in groupe1[::-1]:
    print(i)  # inverse le tableau