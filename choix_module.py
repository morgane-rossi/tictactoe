import affichage_module
import ia_module

def choixCase(tour, grille, joueurs, joueur_actuel):
    #Affiche une grille de présentation des numéro de case le 1er tour
    if tour == 1:
        affichage_module.affichageGrille([[1,2,3], [4,5,6], [7,8,9]])

    #Boucle pour demander l'input tant que le joueur ne choisi pas une case valide
    choix_valide = False
    while choix_valide == False:
        if joueurs[1][0] == "Bot" and joueur_actuel == 1:
            return ia_module.ia(grille, joueurs[1][1])
        else:
            choix = int(input('\nChoissisez une case: '))
        #Envoie une erreur si la case est invalide (non-occupé)
        if choix > 9 or choix < 1:
            print("Nombre invalide!")
        elif grille[(choix - 1) // 3][(choix - 1) % 3]:
            print("Case déjà joué!")
        else:
            return choix
