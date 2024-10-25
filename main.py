import grille_module
import joueurs_module
import tours_module
import choix_module
import verification_module
import affichage_module

#[Jeremy] Intro du jeu
#[choix // 3][choix % 3] convertit le nombre de la case choisi en coordonnée
#ex: 1 // 3 = 0, 1 % 3 = 1 => 0, 1

print("Bienvenue au Morpion!")

resultat = "Aucun"
joueurs = joueurs_module.nomJoueurs()
joueur_actuel = 1
grille = grille_module.newGrille()    
tour = 0
print(f"joueurs : {joueurs}")

while resultat == "Aucun":
    symbole = joueurs[joueurActuel][1]
    joueurActuel = tour_module.tourSuivant(joueurs, joueurActuel, tour)
    print(f"tour = {tour} - normalement fonction tourSuivant incrémente variable tour")
    choix_module.choixCase(symbole, grille, tour)
    print(f"symbole = {symbole}")
#    grille[(choix - 1) // 3][(choix - 1) % 3] = joueurs[joueurActuel][1]
# verifVainqueur(grille, tour, joueurs, joueur_actuel)
    resultat = verification_module.verifVainqueur(grille, tour, joueurs, joueurActuel)
    affichage_module.affichageGrille(grille)


if resultat == "Gagné!":
    print(f"\nBravo {joueurs[joueur_actuel][0]}, vous avez Gagné!")
elif resultat == "Egalité!":
    print(f"\nC'est une égalité!")
else:
    print("Erreur!")