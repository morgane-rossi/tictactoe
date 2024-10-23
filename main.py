#Test d'affichage de grille (Liste)
#grid = ["1", "|", "2", "|", "3", "\n", "-", "-", "-", "-", "-", "\n", "4", "|", "5", "|", "6", "\n", "-", "-", "-", "-", "-", "\n", "7", "|", "8", "|", "9"]




valeurGrille = [""] * 9
print(valeurGrille)

for x in range(9):
    caseJoueur1 = int(input("Choissisez la case: "))
    valeurGrille[caseJoueur1-1] = "O"

#affichage de la grille
def affichageGrille(valeurGrille):
    grille = []

    for x in range(9):
        grille += valeurGrille(x)
        if x == 8:
            break
        if x % 3 == 2:
            #grille += "\n__________\n"
            grille += "\n----------\n"
        else:
            grille += " | "

    for x in grille:
        print(x, end = "")

#Boucle qui dessine la grille à partir de la liste
#for x in range(len(grid)):
#    print(grid[x], end= "")

#Code temporaire à changer (c'est juste un teste d'affichage)
