#[Morgane] Grille
#Grille en 3x3, 2d (liste dans liste)
def nouvelle_grille() :
    grille = [None] * 3
    for i in range(3):
        grille[i] = [""] * 3

    return grille