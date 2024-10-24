import main

def tourSuivant(joueurs, joueur_actuel):
    main.tour += 1
    # Index du joueur en cours
    joueur_actuel = (joueur_actuel + 1) % len(joueurs)  # Passer au joueur suivant

    print(f"\nC'est au tour de {joueurs[joueur_actuel][0]} de jouer.")
    return joueur_actuel