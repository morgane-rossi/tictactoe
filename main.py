#Test d'affichage de grille (Liste)
grid = ["1", "|", "2", "|", "3", "\n", "-", "-", "-", "-", "-", "\n", "4", "|", "5", "|", "6", "\n", "-", "-", "-", "-", "-", "\n", "7", "|", "8", "|", "9"]

#Boucle qui dessine la grille à partir de la liste
for x in range(len(grid)):
    print(grid[x], end= "")

#Code temporaire à changer (c'est juste un teste d'affichage)