def game():
    nombre_mystere = 5
    reponse = 0
    message = ""
    while not reponse == nombre_mystere:
        question = input("Quel est le nombre mystère ? ")

        try:
            reponse = int(question)
        except:
            print("Erreur: Saisir un nombre entier")
        else:
            if reponse > nombre_mystere:
                message = "C'est moins!"
            elif reponse < nombre_mystere:
                message = "C'est plus!"
            else:
                message = "Félicitations"
            print(message)
    return reponse

game()