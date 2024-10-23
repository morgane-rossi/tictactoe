#[Morgane] Intro du jeu




#[Morgane] Grille




#[Moussa] Ajouter/saisir des joueurs
def demarrer_partie():
    nombre_joueurs = int(input("Combien de joueurs ? "))
    joueurs = []
    for i in range(nombre_joueurs):
        nom = input(f"Entrez le nom du joueur {i+1} : ")
        joueurs.append(nom)

    

    joueur_actuel=0  # Index du joueur en cours
    tour+=1
    print(f"C'est au tour de {joueurs[joueur_actuel]} de jouer.")
    joueur_actuel = (joueur_actuel + 1) % nombre_joueurs  # Passer au joueur suivant
    return joueur_actuel
demarrer_partie()







#[Jeremy] Vérification de fin de partie




#[Jeremy] Afficher la grille



