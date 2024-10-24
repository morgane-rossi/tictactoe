#[Morgane] Grille
#Grille en 3x3, 2d (liste dans liste)
def newGrille() :
    grille = [None] * 3
    for i in range(3):
        grille[i] = ["-"] * 3

    return grille

#[Moussa] Ajouter/saisir des joueurs
def nomJoueurs():
    nombre_joueurs = 2 #int(input("Combien de joueurs ? "))
    joueurs = []
    for i in range(nombre_joueurs):
        nom = input(f"Entrez le nom du joueur {i+1} : ")
        symbole = ["O", "X"] #input(f"Rentrez un symbole: ")
        joueurs.append([nom, symbole[i]])
    return joueurs

def tourSuivant(joueurs, joueur_actuel):
    global tour
    tour += 1
    # Index du joueur en cours
    joueur_actuel = (joueur_actuel + 1) % len(joueurs)  # Passer au joueur suivant

    print(f"\nC'est au tour de {joueurs[joueur_actuel][0]} de jouer.")
    return joueur_actuel

def choixCase():
    if tour == 1:
        affichageGrille([[1,2,3], [4,5,6], [7,8,9]])
    choix = input('\nChoissisez une case: ')
    return choix

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
        valeurTeste += [[x, y] for y in range(len(grille[x])) if grille[x][y] == joueurs[joueurActuel][1]]

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
    if tour == 8:
        return "Egalité!"
    else:
        return "Aucun"

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

#[Jeremy] Intro du jeu

print("Bienvenue au Morpion!")

resultat = "Aucun"
joueurs = nomJoueurs()
joueurActuel = 1
grille = newGrille()    
tour = 0

while resultat == "Aucun":
    joueurActuel = tourSuivant(joueurs, joueurActuel)
    choix = int(choixCase())
    grille[(choix - 1) // 3][(choix - 1) % 3] = joueurs[joueurActuel][1]
    resultat = verifVainqueur(grille)
    affichageGrille(grille)
if resultat == "Egalité!":
    print(f"\nC'est une égalité!")
else:
    print(f"\nBravo {joueurs[joueurActuel][0]}, vous avez Gagné!")