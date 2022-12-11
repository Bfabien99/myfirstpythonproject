class Espece:
    ESPECE = "Espèce inconnue"

    def AfficherEspece(self):
        print("Espèce : " + self.ESPECE)


class Chat(Espece):
    ESPECE = "Animal"
    pass


class Personne(Espece):
    ESPECE = "Humain"  # variable de classe, une seule pour toutes les instances

    def __init__(self, nom: str = "", age: int = 0):
        self.nom = nom
        self.age = int(age)
        if nom == "":
            self.DemanderNom()

    def SePresenter(self):
        info_personne = "bonjour, je m'appelle {}".format(self.nom)
        if self.age <= 0:
            print(info_personne)
        else:
            age_personne = ", j'ai {} ans".format(self.age)
            print(f"{info_personne}{age_personne}")
            if self.EstMajeur():
                print("Je suis Majeur")
            else:
                print("Je suis Mineur")

    def DemanderNom(self):
        self.nom = input("Quel est ton nom ? : ")

    def EstMajeur(self):
        return self.age >= 18


Personne("Aline", 19).AfficherEspece()