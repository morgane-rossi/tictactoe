#[Jeremy] Vérification de fin de partie

#resultat: pour connaitre l'issue de la partie. On peut afficher un message personalisé avec des valeurs différentes (while resultat == "Aucun" (ou "Partie en cours"))

def verifVainqueur(grille, tour, joueurs, joueur_actuel):
 
    #1ème ligne: Vertical, 2ème ligne: Horizontal, 3ème ligne: Diagonal (haut-gauche à bas-droite), 4ème ligne: Diagonal(haut-droite à bas-gauche)
    solutions = [[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],
    [[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],
    [[0,0],[1,1],[2,2]],[[2,0],[1,1],[0,2]]]
    
    valeur_teste = []

    #Ajoutes toutes les coordonnes des cases contenant le symbole du joueur et les met dans une liste (valeurTeste)
    for x in range(len(grille)):
        valeur_teste += [[x, y] for y in range(len(grille[x])) if grille[x][y] == joueurs[joueur_actuel][1]]

    #Vérifie les cases gagnantes avec les positions déjà existantes du symbole qui a été joué
    #Code en commentaire pour retourner la valeur des cases gagnantes au lieu de "Gagné" (pour les éclairer par exemple)
    for x in range(len(solutions)):
        #caseGagnantes = []
        compteur = 0
        for y in valeur_teste:
            for z in solutions[x]:
                if z == y:
                    #caseGagnantes += [z] 
                    compteur += 1
                #if len(caseGagnantes) == 3:
                if compteur == 3:
                    #return caseGagnantes
                    return "Gagné!"

    #Egalité si le nombre de coup = 9 (de 0 à 8) Se déclenche aprñs une vérification (peut gagner au dernier tour)
    if tour == 9:
        return "Egalité!"
    else:
        return "Aucun"