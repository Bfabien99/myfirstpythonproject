class Personne:
    def __init__(self, nom: str, age: int, genre: bool):
        self.nom = nom
        self.age = age
        self.genre = genre

    def sePresenter(self):
        print("Bonjour, je m'appelle {}, j'ai {} ans".format(self.nom, self.age))
        e_optionnel = ""
        if self.genre:
            genre_str = "Homme"
        else:
            genre_str = "Femme"
            e_optionnel = "e"
        print("Genre : {}".format(genre_str))

        # genre_str = "Homme" if self.genre else "Femme"
        # e_optionnel = "" if self.genre else "e"

        if self.EstMajeur():
            print("Je suis Majeur" + e_optionnel)
        else:
            print("Je suis Mineur" + e_optionnel)

    def EstMajeur(self):
        return self.age >= 18


personne = Personne("Fabien", 24, True)
personne.sePresenter()