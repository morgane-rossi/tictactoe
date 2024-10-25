
import affichage_module
import tour_module


def choixCase(symbole, grille, tour):
    
import ia_module

def choixCase(tour, grille, joueurs, joueur_actuel):


    #Boucle pour demander l'input tant que le joueur ne choisi pas une case valide
    choix_valide = False
    while choix_valide == False:
        if joueurs[1][0] == "Bot" and joueur_actuel == 1:
            return ia_module.ia(grille, joueurs[1][1])
        else:
            choix = int(input('Choissisez une case: '))
        #Envoie une erreur si la case est invalide (non-occupé)
        if choix > 9 or choix < 1:
            print("Nombre invalide!")
        elif grille[(choix - 1) // 3][(choix - 1) % 3]:
            print("Case déjà joué!")
        else:
            return choix
