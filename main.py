import ia_module as ia_mod
import affichage_module as affichage_mod

#[Morgane] Grille
#Grille en 3x3, 2d (liste dans liste)
def nouvelle_grille() :
    grille = [None] * 3
    for i in range(3):
        grille[i] = [""] * 3

    return grille

#[Moussa] Ajouter/saisir des joueurs
def nom_joueurs():
    est_valide = False
    while est_valide == False:
        nombre_joueurs = int(input("Combien de joueurs (1 ou 2) ? "))

        joueurs = []
        
        if nombre_joueurs > 0 and nombre_joueurs < 3:
            for i in range(nombre_joueurs):
                nom = input(f"Entrez le nom du joueur {i+1} : ")
                symbole = "" #["O", "X"] 
                
                while symbole != "O" and symbole != "X":    
                    symbole = (input(f"Choissisez un symbole (O ou X): "))
                    if symbole != "O" and symbole != "X": 
                        print("Symbole non disponible!")
                    if i != 0:
                        if symbole == joueurs[i-1][1]:
                            symbole = ""
                            print("Symbole déjà pris!")
                
                joueurs.append([nom, symbole])
                
                if nombre_joueurs == 1:
                    if joueurs[0][1] == "O":
                        joueurs.append(["Bot", "X"])
                    else: 
                        joueurs.append(["Bot", "O"]) 
            
            return joueurs
        
        else:
            print("Nombre de joueurs non pris en charge")   

def tour_suivant(joueurs, joueur_actuel):
    joueur_actuel = (joueur_actuel + 1) % len(joueurs)  # Passer au joueur suivant

    print(f"\n\nC'est au tour de {joueurs[joueur_actuel][0]} de jouer.")
    return joueur_actuel

def choixCase(grille, joueurs, joueur_actuel):
    #Boucle pour demander l'input tant que le joueur ne choisi pas une case valide
    choix_valide = False
    while choix_valide == False:
        if joueurs[1][0] == "Bot" and joueur_actuel == 1:
            return ia_mod.ia(grille, joueurs[1][1])
        else:
            choix = int(input('Choissisez une case: '))
        #Envoie une erreur si la case est invalide (non-occupé)
        if choix > 9 or choix < 1:
            print("Nombre invalide!")
        elif grille[(choix - 1) // 3][(choix - 1) % 3]:
            print("Case déjà joué!")
        else:
            return choix
      
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

    #Egalité si le nombre de coup = 9 (de 0 à 8) Se déclenche apres une vérification (peut gagner au dernier tour)
    if tour == 8:
        return "Egalité!"
    else:
        return "Aucun"

#[Jeremy] Afficher la grille
def affichage_grille(grille):
    for x in range(len(grille)):
        for y in range(len(grille[x])):
            if not grille[x][y]:
                print("-", end = "")
            else:
                print(grille[x][y], end = "")
            #Evite une ligne verticale en trop
            if y % 3 != 2:
                print(" | ", end = "")
        #Evite une ligne horizontale en trop
        if x != len(grille) - 1:
            print("")
            print("---" * (len(grille)))

#[Jeremy] Intro du jeu

print("Bienvenue au Morpion!")

#Variable Globale
resultat = "Aucun"
joueurs = nom_joueurs()
joueur_actuel = 1   # Détermine le joueur en cours (1er joueur = 0)
grille = nouvelle_grille()    
tour = 0

while resultat == "Aucun":
    #Premier tour, on affiche la grille avec les valeurs
    if tour == 0:
        affichage_grille([[1,2,3], [4,5,6], [7,8,9]])
    joueur_actuel = tour_suivant(joueurs, joueur_actuel)
    tour += 1

    #Affiche une grille de présentation des numéro de case le 1er tour
    choix = choixCase(grille, joueurs, joueur_actuel)
    if choix == False:
        print("Erreur de sélection de case du bot!")
    
    #[choix // 3][choix % 3] convertit le nombre de la case choisi en coordonnée
    #ex: 1 // 3 = 0, 1 % 3 = 1 => 0, 1
    grille[(choix - 1) // 3][(choix - 1) % 3] = joueurs[joueur_actuel][1]
   
    resultat = verifVainqueur(grille, tour, joueurs, joueur_actuel)
   
    affichage_grille(grille)
    #affichage_mod.affichage_grille_tk(grille, joueurs, joueur_actuel)


if resultat == "Gagné!":
    print(f"\nBravo {joueurs[joueur_actuel][0]}, vous avez Gagné!")
elif resultat == "Egalité!":
    print(f"\nC'est une égalité!")
else:
    print("Erreur!")