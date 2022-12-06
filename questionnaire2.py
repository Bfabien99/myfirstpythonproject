# LES COLLECTIONS : PROJET QUESTIONNAIRE
#
# Partez de ce code source pour réaliser la version 2 du projet questionnaire
#
#############################################################################
# FORMATION COMPLÈTE "DÉVELOPPEUR PYTHON"
#
# Pour progresser en programmation et aller plus loin avec le langage Python,
# découvrez ma formation complète ici :
# https://codeavecjonathan.com/formations.html
#############################################################################
def demander_reponse_numerique_utilisateur(_min, _max):

    reponse_str = input(f"Votre réponse (entrer le numéro correspondant entre {_min}, {_max}): ")
    try:
        reponse_int = int(reponse_str)
        if _min <= reponse_int <= _max:
            return reponse_int

        print(f"Entrer un numéro entre {_min}, {_max}")
    except:
        print("Erreur: Entrer un chiffre")
    return demander_reponse_numerique_utilisateur(_min, _max)


def poser_question(_question: list | tuple):
    titre = _question[0]
    propositions = _question[1]
    vrai = _question[2]
    print("QUESTION")
    print("  " + titre)
    for i in range(len(propositions)):
        print(i+1, "-->", propositions[i])

    reponse_correct = False
    reponse = demander_reponse_numerique_utilisateur(1, len(propositions))
    if propositions[reponse-1] == vrai:
        print("Bonne réponse")
        reponse_correct = True
        return reponse_correct
    else:
        print("Mauvaise réponse")

    print()
    return reponse_correct


def lancer_questionnaire(_questionnaire: list | tuple):
    score = 0
    for i in range(len(_questionnaire)):
        if poser_question(_questionnaire[i]):
            score += 1
    print("Score final:", score, "/", len(_questionnaire))


question1 = ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris")
question2 = ("Quelle est la capitale de l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")

questionnaire = (question1, question2)
# poser_question(question1)
lancer_questionnaire(questionnaire)