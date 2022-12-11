class Personne:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = int(age)

    def SePresenter(self):
        print("Bonjour, je m'appelle {}, j'ai {} ans".format(self.nom, self.age))
        if self.EstMajeur():
            print("Je suis Majeur")
        else:
            print("Je suis Mineur")

    def EstMajeur(self):
        return self.age >= 18


personne1 = Personne("Jean", 26)
personne2 = Personne("Emilie", 18)

personne1.SePresenter()
personne2.SePresenter()