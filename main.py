import grille_module as grille_mod
import joueurs_module as joueurs_mod
import tours_module as tours_mod
import choix_module as choix_mod
import verification_module as verif_mod
import affichage_module as affichage_mod

#[Jeremy] Intro du jeu

print("Bienvenue au Morpion!")

#Variable Globale
resultat = "Aucun"
joueurs = joueurs_mod.nom_joueurs()
joueur_actuel = 1   # Index du joueur en cours
grille = grille_mod.nouvelle_grille()    
tour = 0

while resultat == "Aucun":
    if tour == 0:
        affichage_mod.affichage_grille([[1,2,3], [4,5,6], [7,8,9]])
    joueur_actuel = tours_mod.tour_suivant(joueurs, joueur_actuel)
    tour += 1

    #Affiche une grille de présentation des numéro de case le 1er tour
    choix = choix_mod.choixCase(tour, grille, joueurs, joueur_actuel)
    if choix == False:
        print("Erreur de sélection de case du bot!")
    
    #[choix // 3][choix % 3] convertit le nombre de la case choisi en coordonnée
    #ex: 1 // 3 = 0, 1 % 3 = 1 => 0, 1
    grille[(choix - 1) // 3][(choix - 1) % 3] = joueurs[joueur_actuel][1]
   
    resultat = verif_mod.verifVainqueur(grille, tour, joueurs, joueur_actuel)
   
    #affichage_mod.affichage_grille(grille)
    affichage_mod.affichage_grille_tk(grille)


if resultat == "Gagné!":
    print(f"\nBravo {joueurs[joueur_actuel][0]}, vous avez Gagné!")
elif resultat == "Egalité!":
    print(f"\nC'est une égalité!")
else:
    print("Erreur!")