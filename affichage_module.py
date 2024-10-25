#[Jeremy] Afficher la grille
def affichageGrille(grille):
    for x in range(len(grille)):
        for y in range(len(grille[x])):
            print(grille[x][y], end = "")
            #Evite une ligne verticale en trop
            if y % 3 != 2:
                print(" | ", end = "")
        #Evite une ligne horizontale en trop
        if x != len(grille) - 1:
            print("")
            print("---" * (len(grille)))