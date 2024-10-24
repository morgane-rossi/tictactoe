import grille_module
import joueurs_module
import tour_module
import choix_module
import verification_module
import affichage_module

#[Jeremy] Intro du jeu

print("Bienvenue au Morpion!")

resultat = "Aucun"
joueurs = joueurs_module.nomJoueurs()
joueur_actuel = 1
grille = grille_module.newGrille()    
tour = 0

while resultat == "Aucun":
    joueur_actuel = tour_module.tourSuivant(joueurs, joueur_actuel)
    choix = int(choix_module.choixCase())
    grille[(choix - 1) // 3][(choix - 1) % 3] = joueurs[joueur_actuel][1]
    resultat = verification_module.verifVainqueur(grille)
    affichage_module.affichageGrille(grille)
if resultat == "Egalité!":
    print(f"\nC'est une égalité!")
else:
    print(f"\nBravo {joueurs[joueur_actuel][0]}, vous avez Gagné!")