class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def SePresenter(self):
        print("Bonjour, je m'appelle", self.nom, ", j'ai", self.age, "ans")


personne = Personne("Fabien", 30)
personne.SePresenter()