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
    if tour == 0:
        affichage_module.affichageGrille([[1,2,3], [4,5,6], [7,8,9]])
    joueur_actuel = tours_module.tour_suivant(joueurs, joueur_actuel)
    tour += 1
    #Affiche une grille de présentation des numéro de case le 1er tour
    choix = choix_module.choixCase(tour, grille, joueurs, joueur_actuel)
    if choix == False:
        print("Erreur de sélection de case du bot!")
    grille[(choix - 1) // 3][(choix - 1) % 3] = joueurs[joueur_actuel][1]
    resultat = verification_module.verifVainqueur(grille, tour, joueurs, joueur_actuel)
    affichage_module.affichageGrille(grille)


if resultat == "Gagné!":
    print(f"\nBravo {joueurs[joueur_actuel][0]}, vous avez Gagné!")
elif resultat == "Egalité!":
    print(f"\nC'est une égalité!")
else:
    print("Erreur!")