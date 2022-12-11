class Personne:
    def __init__(self, _nom: str):
        self.nom = _nom

    def SePresenter(self):
        print("Bonjour, je suis une personne et je m'apelle " + self.nom)


nombre_de_personnes = 3
"""
noms = []

for i in range(nombre_de_personnes):
    noms.append(input("Entrer le nom de la personne {} : ".format(i+1)))


liste = []
for nom in noms:
    liste.append(Personne(nom))
"""
liste = []
for i in range(nombre_de_personnes):
    nom = input("Entrer le nom de la personne {} : ".format(i+1))
    liste.append(Personne(nom))

for personne in liste:
    personne.SePresenter()
