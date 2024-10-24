import main

#[Jeremy] Vérification de fin de partie

#valeur temporaire pour faire des tests. A effacer une fois créer ailleurs
#resultat: pour connaitre l'issue de la partie. On peut afficher un message personalisé avec des valeurs différentes (while resultat == "Aucun" (ou "Partie en cours"))

def verifVainqueur(grille):
 
    #1ème ligne: Vertical, 2ème ligne: Horizontal, 3ème ligne: Diagonal (haut-gauche à bas-droite), 4ème ligne: Diagonal(haut-droite à bas-gauche)
    solutions = [[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],
    [[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],
    [[0,0],[1,1],[2,2]],[[2,0],[1,1],[0,2]]]
    
    valeurTeste = []

    #Ajoutes toutes les coordonnes des cases contenant le symbole du joueur et les met dans une liste (valeurTeste)
    for x in range(len(grille)):
        valeurTeste += [[x, y] for y in range(len(grille[x])) if grille[x][y] == main.joueurs[main.joueurActuel][1]]

    #Vérifie les cases gagnantes avec les positions déjà existantes du symbole qui a été joué
    #Code en commentaire pour retourner la valeur des cases gagnantes au lieu de "Gagné" (pour les éclairer par exemple)
    for x in range(len(solutions)):
        #caseGagnantes = []
        compteur = 0
        for y in valeurTeste:
            for z in solutions[x]:
                if z == y:
                    #caseGagnantes += [z] 
                    compteur += 1
                #if len(caseGagnantes) == 3:
                if compteur == 3:
                    #return caseGagnantes
                    return "Gagné"

    #Egalité si le nombre de coup = 9 (de 0 à 8) Se déclenche aprñs une vérification (peut gagner au dernier tour)
    if main.tour == 8:
        return "Egalité!"
    else:
        return "Aucun"