class Personne:
    def __init__(self, nom:str, age:int, genre:bool):
        self.nom = nom
        self.age = age
        self.genre = genre

    def sePresenter(self):
        if self.genre:
            print("Bonjour, je m'appelle %s, j'ai %s ans" % self.nom % self.age)
            print("Genre : Homme")
            if self.EstMajeur():
                print("Je suis Majeur")
            else:
                print("Je suis Mineur")

        else:
            print("Bonjour, je m'appelle %s, j'ai %s ans" % self.nom % self.age)
            print("Genre : Femme")
            if self.EstMajeur():
                print("Je suis Majeure")
            else:
                print("Je suis Mineure")

    def EstMajeur(self):
        return self.age >= 18


personne = Personne("Fabien", 24)