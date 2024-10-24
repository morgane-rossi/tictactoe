import main
import affichage_module

def choixCase():
    if main.tour == 1:
        affichage_module.affichageGrille([[1,2,3], [4,5,6], [7,8,9]])
    choix = input('\nChoissisez une case: ')
    return choix