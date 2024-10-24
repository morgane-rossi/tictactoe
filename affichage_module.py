#[Jeremy] Afficher la grille

#Le modulos préviennent de creer des traits verticaux supplémentaires après les lignes (il n'en crée pas aprñs index 2, 5 etc)
#PAreil pour le dernier if qui évite un trait horizontal en trop
#La fonction print directement, il suffit de l'appeler pour afficher la grille: affichageGrille(grille)

def affichageGrille(grille):
    for x in range(len(grille)):
        for y in range(len(grille[x])):
            print(grille[x][y], end = "")
            if y % 3 != 2:
                print(" | ", end = "")
        if x != len(grille) - 1:
            print("")
            print("---" * (len(grille)))