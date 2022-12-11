class Personne:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age

    def SePresenter(self):
        print("Bonjour, je m'appelle", self.nom, ", j'ai", self.age, "ans")
        if self.EstMajeur():
            print("Je suis majeur")
        else:
            print("Je suis mineur")

    def EstMajeur(self):
        return self.age >= 18


personne = Personne("Fabien", 30)
personne.SePresenter()
