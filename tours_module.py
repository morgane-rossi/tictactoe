def tourSuivant(joueurs, joueur_actuel, tour):
    tour += 1
    # Index du joueur en cours
    print(f"len(joueurs) = {len(joueurs)}")

    print(f"\n\nC'est au tour de {joueurs[joueur_actuel][0]} de jouer.")
    return joueur_actuel