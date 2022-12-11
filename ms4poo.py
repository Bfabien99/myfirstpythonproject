class Personne:
    def __init__(self, _nom: str):
        self.nom = _nom

    def SePresenter(self):
        print("Bonjour, je suis une personne et je m'apelle " + self.nom)


noms = [input("nom de la personne 1 : "), input("nom de la personne 2 : "), input("nom de la personne 3 : ")]

liste = []
for nom in noms:
    liste.append(Personne(nom))

for personne in liste:
    print(personne.SePresenter())