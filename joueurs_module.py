#[Moussa] Ajouter/saisir des joueurs
def nomJoueurs():
    nombre_joueurs = 2 #int(input("Combien de joueurs ? "))
    joueurs = []
    for i in range(nombre_joueurs):
        nom = input(f"Entrez le nom du joueur {i+1} : ")
        symbole = ["O", "X"] #input(f"Rentrez un symbole: ")
        joueurs.append([nom, symbole[i]])
    return joueurs