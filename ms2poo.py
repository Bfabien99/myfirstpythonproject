class Personne:
    def __init__(self, nom: str):
        self.nom = nom

    def SePresenter(self, age):
        print("Bonjour, je m'appelle {}, j'ai {} ans".format(self.nom, age))
        if self.EstMajeur():
            print("Je suis Majeur")
        else:
            print("Je suis Mineur")

    def EstMajeur(self):
        return age >= 18


personne1 = Personne("Jean")
personne2 = Personne("Emilie")

personne1.SePresenter(26)
personne2.SePresenter(18)