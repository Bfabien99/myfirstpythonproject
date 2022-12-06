#   LES FONCTIONS : PROJET QUESTIONNAIRE
#
#   Question : Quelle est la capitale de la france ?
#   (a)
#   (b)
#   (c)
#   (d)
#
#   Votre réponse :
#   Bonne réponse / Mauvaise réponse

#   ...
#   Question : Quelle est la capitale de l'italie ?
#   ...
#

"""
def questionnaire():
    print("------- Début du programme -------")
    print("*Question 1: Quelle est la capitale de la Côte d'Ivoire ?")
    print("
    (a) Korogho
    (b) Boundiali
    (c) Man
    (d) Abidjan
    ")
    reponse = input("Réponse : ")
    if not reponse == "d":
        print("-->> 💥 Mauvaise réponse <<-- ")
    else:
        print("-->> ✅ Bonne réponse <<---")

    print("*Question 2: Quelle est la capitale de la France ?")
    print("
        (a) Troy
        (b) Paris
        (c) Man
        (d) Abidjan
        ")
    reponse = input("Réponse : ")
"""
"""
    if not reponse == "b":
        print("-->> 💥 Mauvaise réponse <<--")
    else:
        print("-->> ✅ Bonne réponse <<---")

    print("------- Fin du programme -------")

questionnaire()
"""


# poser_question(question, r1, r2, r3, r4, bonne_reponse)
def poser_question(question: str, bonne_reponse: str, r1="", r2="", r3="", r4="") -> str:
    global score
    print("------- Début du programme -------")
    print("*Question :", question)
    print("-->>> Choisir la lettre qui convient <<<--")
    if r1:
        print(r1)
    if r2:
        print(r2)
    if r3:
        print(r3)
    if r4:
        print(r4)

    reponse = input("Réponse : ")
    if not reponse == bonne_reponse:
        print("-->> 💥 Mauvaise réponse <<--")
    else:
        print("-->> ✅ Bonne réponse <<---")
        score += 1


score = 0
poser_question("Qui suis je ?", "c", "(a) je", "(b) qui", "(c) suis", "(d) ?")
poser_question("Qui suis je ?", "c", "(a) je", "(b) qui", "(c) suis", "(d) ?")
poser_question("Qui suis je ?", "c", "(a) je", "(b) qui", "(c) suis", "(d) ?")
print(f"-->>> Score : {score} <<<---")
print("------- Fin du programme -------")