# EXERCICE FONCTIONS
# Tables de multiplication
#
#
# 1 x 4 = 4
# 2 x 4 = 8
# ...
# 10 x 4 = 40
#
# afficher_table_multiplication(n)
# min / max
# erreur : si min > max

def afficher_table_multiplication(_nombre, _min=1, _max=10):
    print('------- début du programme -------')
    if _min > _max:
        print(f"Erreur: La table de multiplacation ne peut commencer par {_min} et se terminer par {_max}")
    else:
        for i in range(_min, (_max+1)):
            print(f"-->> {i} x {_nombre} = {i*_nombre} <<--")
    print('------- fin du programme -------')


afficher_table_multiplication(2000, 1, 9)