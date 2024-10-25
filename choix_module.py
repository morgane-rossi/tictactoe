
import affichage_module
import tour_module


def choixCase(symbole, grille, tour):
    
import ia_module

def choixCase(tour, grille, joueurs, joueur_actuel):
    #Affiche une grille de présentation des numéro de case le 1er tour
    if tour == 1:
        affichage_module.affichageGrille([[1,2,3], [4,5,6], [7,8,9]])
    choix = "-1"

    # forcer le joueur à rentrer un nombre compris entre 1 et 9
    while not choix.isdigit()  or ( int(choix) <= 0 or int(choix) > 9) :
        choix = input('\nChoissisez une case: ')
    choix = int(choix)
    print("je continue")

    if choix == 1 :
        if not grille[0][0] :
            grille[0][0] = symbole
    elif choix == 2 :
        if not grille[0][1]:
            grille[0][1] = symbole
    elif choix == 3 :
        if not grille[0][2]:
            grille[0][2] = symbole
    elif choix == 4 :
        if not grille[1][0]:
            grille[1][0] = symbole
    elif choix == 5 :
        if not grille[1][1] :
            grille[1][1] = symbole
    elif choix == 6 :
        if not grille[1][2]:
            grille[1][2] = symbole
    elif choix == 7 :
        if not grille[2][0]:
            grille[2][0] = symbole
    elif choix == 8 :
        if not grille[2][1]:
            grille[2][1] = symbole
    elif choix == 9 :
        if not grille[2][2]:
            grille[2][2] = symbole

    #return choix

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
