#Import pour le bot et les better graphics
import ia_module as ia_mod
#import affichage_module as affichage_mod

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
    #On fait une boucle pour toujours demander la question, si l'utilisateur se trompe
    while est_valide == False:  
        nombre_joueurs = int(input("Combien de joueurs (1 ou 2) ? "))

        joueurs = []
        
        if nombre_joueurs > 0 and nombre_joueurs < 3:   #Si la valeur est 1 ou 2,
            #demander le nom de tout les joueurs
            #(range(nombre_joueur) = autant de fois qu'il y a de joueurs)
            for i in range(nombre_joueurs):     
                nom = input(f"Entrez le nom du joueur {i+1} : ")    
                
                symbole = "" #["O", "X"]                            
                while symbole != "O" and symbole != "X": #On demande aussi pour le symbole
                    symbole = (input(f"Choissisez un symbole (O ou X): "))
                    if symbole != "O" and symbole != "X": #si le symbole n'est pas bon, on redemande
                        print("Symbole non disponible!")
                    if i != 0:
                        if symbole == joueurs[i-1][1]: #ou alors si il est déjà pris par le joueur 1.
                            symbole = ""
                            print("Symbole déjà pris!")
                
                #Une fois qu'on a le nom et le symbole, on l'ajoute dans les joueurs
                joueurs.append([nom, symbole])

                #Ajoute le bot si l'option "1 joueur" est sélectionné 
                # (Oui, ca marche aussi si le joueur 2 rentre "Bot" en nom)
                if nombre_joueurs == 1:
                    if joueurs[0][1] == "O":
                        joueurs.append(["Bot", "X"])
                    else: 
                        joueurs.append(["Bot", "O"]) 
            
            return joueurs
        
        else:
            print("Nombre de joueurs non pris en charge")   

def tour_suivant(joueurs, joueur_actuel):
    joueur_actuel = (joueur_actuel + 1) % len(joueurs)  # Passer au joueur suivant. 
    # Revient au joueur 1 avec le modulo si c'est le dernier joueur

    print(f"\n\nC'est au tour de {joueurs[joueur_actuel][0]} de jouer.")
    return joueur_actuel

def choix_case(grille, joueurs, joueur_actuel):
    #Boucle pour demander l'input tant que le joueur ne choisi pas une case valide
    choix_valide = False
    while choix_valide == False:
        if joueurs[1][0] == "Bot" and joueur_actuel == 1:
            return ia_mod.ia(grille, joueurs[1][1], difficulte)
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

#resultat: pour connaitre l'issue de la partie. 
# On peut afficher un message personalisé avec des valeurs différentes 
# (while resultat == "Aucun" (ou "Partie en cours"))

def verif_vainqueur(grille, tour, joueurs, joueur_actuel):
 
    #1ème ligne: Vertical, 2ème ligne: Horizontal, 3ème ligne: 
    # Diagonal (haut-gauche à bas-droite), 
    # 4ème ligne: Diagonal(haut-droite à bas-gauche)
    solutions = [[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],
    [[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],
    [[0,0],[1,1],[2,2]],[[2,0],[1,1],[0,2]]]
    
    coords_symbole = []

    #Ajoutes toutes les coordonnes des cases contenant le symbole du joueur 
    # et les met dans une liste (coords_symbole)
    for x in range(len(grille)):
        coords_symbole += [[x, y] for y in range(len(grille[x])) if grille[x][y] == joueurs[joueur_actuel][1]]

    #Vérifie les cases gagnantes avec les positions déjà existantes 
    # du symbole qui a été joué
    #Code en commentaire pour retourner la valeur des cases gagnantes 
    # au lieu de "Gagné" (pour les éclairer par exemple)
    for x in range(len(solutions)):     #Prend la premiere solution:
        #caseGagnantes = []
        compteur = 0                    #(reset le compteur avant chaque 
                                        # nouvelle solutions vérifié),
        for y in coords_symbole:        #pour chaque coordonnée (d'un symbole dans la grille),
            for z in solutions[x]:      #vérifie si ces coordonnées font partie de la solution.
                if z == y:
                    #caseGagnantes += [z] 
                    compteur += 1
                #if len(caseGagnantes) == 3:
                if compteur == 3:       #Si les 3 coordonnes de la solution sont dans la grille, 
                                        # c'est que 3 symboles sont alignés!
                    #return caseGagnantes
                    return "Gagné!"

    #Egalité si le nombre de coup = 9 (de 0 à 8) 
    # Se déclenche apres une vérification (peut gagner au dernier tour)
    if tour == 9:
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
            # % 3 équivalent à  if(x) < 3
            # on crée  une sorte d'exception quand le modulo est égal à 2
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
if joueurs[1][0] == "Bot":
    difficulte = input("Choissisez la difficulté: (F)acile, [defaut](N)ormal, (W)arGames. -> ")
joueur_actuel = 1   # Détermine le joueur en cours (1er joueur = 0)
grille = nouvelle_grille()    
tour = 0

#Boucle de tour
while resultat == "Aucun":
    #Premier tour, on affiche la grille avec les valeurs
    if tour == 0:
        affichage_grille([[1,2,3], [4,5,6], [7,8,9]])
    joueur_actuel = tour_suivant(joueurs, joueur_actuel)
    tour += 1

    #Affiche une grille de présentation des numéro de case le 1er tour
    choix = choix_case(grille, joueurs, joueur_actuel)
    if choix == False:
        print("Erreur de sélection de case du bot!")
    
    #[choix // 3][choix % 3] convertit le nombre de la case choisi en coordonnée
    #ex: 1 // 3 = 0, 1 % 3 = 1 => 0, 1
    grille[(choix - 1) // 3][(choix - 1) % 3] = joueurs[joueur_actuel][1]
   
    resultat = verif_vainqueur(grille, tour, joueurs, joueur_actuel)
   
    affichage_grille(grille)


if resultat == "Gagné!":
    print(f"\nBravo {joueurs[joueur_actuel][0]}, vous avez Gagné!")
elif resultat == "Egalité!":
    print(f"\nC'est une égalité!")
else:
    print("Erreur!")