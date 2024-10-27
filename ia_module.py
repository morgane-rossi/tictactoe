#import time
def ia(grille, signe):
    #Donne l'illusion de réfléchir
    #time.sleep(3)

    #1ème ligne: Vertical, 2ème ligne: Horizontal, 3ème ligne: Diagonal (haut-gauche à bas-droite), 4ème ligne: Diagonal(haut-droite à bas-gauche)
    solutions = [[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],
    [[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],
    [[0,0],[1,1],[2,2]],[[2,0],[1,1],[0,2]]]
    
    coords_symbole_ia = []
    coords_symbole_joueur = []

    #Répertorie ses propores symboles
    for x in range(len(grille)):
        coords_symbole_ia += [[x, y] for y in range(len(grille[x])) if grille[x][y] == signe]

    #Répertorie les symboles du joueur
    for x in range(len(grille)):
        coords_symbole_joueur += [[x, y] for y in range(len(grille[x])) if grille[x][y] != signe and grille[x][y]]

    #Vérifie si 2 symboles sont aligné et joue le 3eme
    def choix_case_ia(coords_symbole):
        for x in range(len(solutions)):     #Prend la premiere solution:
            #caseGagnantes = []
            compteur = 0                    #(reset le compteur avant chaque nouvelle solutions vérifié),
            for y in coords_symbole:          #pour chaque coordonnée (d'un symbole dans la grille),
                for z in solutions[x]:      #vérifie si ces coordonnées font partie de la solution.
                    if z == y:
                        #caseGagnantes += [z] 
                        compteur += 1
                    #if len(caseGagnantes) == 3:
                    if compteur == 2:       #Si les 2 coordonnes de la solution sont dans la grille, la 3eme coordonnée est gagnante!!
                        #return caseGagnantes
                        coord_a_jouer = [z for z in solutions[x] if z not in coords_symbole]    #Cherche la case qui complete une ligne
                        if not grille[coord_a_jouer[0][0]][coord_a_jouer[0][1]]: 
                            case_a_jouer = coord_a_jouer[0][0] * 3 + coord_a_jouer[0][1]    #Convertit les coords en nombre case
                            return case_a_jouer + 1
    
    def choix_simple():
    #choisi une case dans l'ordre (la premiere qui est disponible)
        for case_choisi in range(9):
            if not grille[case_choisi // 3][case_choisi % 3]:       
                return case_choisi + 1
            else:
                continue
        return False

    case_choisi = choix_case_ia(coords_symbole_ia)
    if case_choisi == None:
        case_choisi = choix_case_ia(coords_symbole_joueur)
        if case_choisi == None:
            return choix_simple() 
    return case_choisi
    


grille = [["O","X","O"],["","",""],["","X","O"]]
symbole = "O"               
print(ia(grille, symbole))
    
"""  
    #fallback
    if a == a:
        pass
"""



#print(ia(grille, signe))


"""
test = [[0,0],[0,1],[0,2]]
test.remove([0,0])
print(test)
"""