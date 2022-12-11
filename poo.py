# Différence programmation impérative / objet
# impérative
"""
def demander_nom():
    _nom = input("Quel est ton nom ? ")
    return _nom


def demander_age():
    _age = input("Quel est ton age ? ")
    return _age


def afficher_info(_nom, _age):
    print(f"Tu t'appelles {_nom}, ton age est {_age} ans")


nom = demander_nom()
age = demander_age()

afficher_info(nom, age)
"""


# objet
class Personne:
    def __init__(self):
        self.nom = input("Quel est ton nom ?: ")
        self.age = input("Quel est ton age ?: ")

    def SePresenter(self):
        print("Je suis " + self.nom + " et j'ai " + self.age + " ans")

    def GetNom(self):
        print("Je m'appelle " + self.nom)

    def GetAge(self):
        print("J'ai " + self.age + " ans")

    def AutreFonction():  # méthode static
        print('Static')


personne1 = Personne()  # On créer une personne (on instancie la classe)
personne1.SePresenter()
personne1.GetNom()
personne1.GetAge()
Personne.AutreFonction()