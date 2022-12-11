class Chat:
    def __init__(self, nom_falcutatif: str = "inconnu"):
        self.nom = nom_falcutatif

    def SePresenter(self):
        print("Bonjour, je suis un chat et je m'apelle " + self.nom)


class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self):
        print("Bonjour, je suis une personne et je m'apelle " + self.nom)


chat1 = Chat()
chat2 = Chat("Garfield")

chat1.SePresenter()
chat2.SePresenter()

personne = Personne("Jean")
personne.SePresenter()