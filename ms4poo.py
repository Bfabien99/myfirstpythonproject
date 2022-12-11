class Personne:
    def __init__(self, _nom: str):
        self.nom = _nom

    def SePresenter(self):
        print("Bonjour, je suis une personne et je m'apelle " + self.nom)


noms = []
i = 1
while True:
    nom = input("Entrer le nom de la personne {} : ".format(i))
    if nom == "":
        break
    i += 1
    noms.append(nom)

liste = []
for nom in noms:
    liste.append(Personne(nom))

for personne in liste:
    personne.SePresenter()
