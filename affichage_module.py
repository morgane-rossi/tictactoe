import tkinter as tk
from tkinter import ttk
#import main

class affichage_grille_tk():
    def __init__(self, grille, joueurs, joueur_actuel):
        self.fenetre = tk.Tk()
        self.fenetre.title("Morpion")
        self.fenetre.geometry("600x600")

        self.fenetre.columnconfigure(0, weight = 1)
        self.fenetre.columnconfigure(1, weight = 1)
        self.fenetre.columnconfigure(2, weight = 1)

    def button_clicked(self):
        print(self)

            #grille[0][0] = joueurs[joueur_actuel]
            #bouton_u_l.config(text = grille[0][0])
            #bouton_u_l.config(text = joueurs[joueur_actuel][1])            

        bouton_u_l = ttk.Button(self.fenetre, text="1", command=self.button_clicked)
        bouton_u_l.place(x=0, y=0, width=100, height=100)
        bouton_u_c = ttk.Button(self.fenetre, text="2", command=self.button_u_c_clicked)
        bouton_u_c.place(x=0, y=100, width=100, height=100)
        bouton_u_r = ttk.Button(self.fenetre, text="3", command=self.button_u_r_clicked)
        bouton_u_r.place(x=0, y=200, width=100, height=100)

        bouton_c_l = ttk.Button(self.fenetre, text="4", command=self.button_c_l_clicked)
        bouton_c_l.place(x=100, y=0, width=100, height=100)
        bouton_c_c = ttk.Button(self.fenetre, text="5", command=self.button_c_c_clicked)
        bouton_c_c.place(x=100, y=100, width=100, height=100)
        bouton_c_r = ttk.Button(self.fenetre, text="6", command=self.button_c_r_clicked)
        bouton_c_r.place(x=100, y=200, width=100, height=100)

        bouton_b_l = ttk.Button(self.fenetre, text="7", command=self.button_b_l_clicked)
        bouton_b_l.place(x=200, y=0, width=100, height=100)
        bouton_b_c = ttk.Button(self.fenetre, text="8", command=self.button_b_c_clicked)
        bouton_b_c.place(x=200, y=100, width=100, height=100)
        bouton_b_r = ttk.Button(self.fenetre, text="9", command=self.button_b_r_clicked)
        bouton_b_r.place(x=200, y=200, width=100, height=100)

        self.fenetre.mainloop()
"""
def nom_joueurs_lb():
    est_valide = False
    while est_valide == False:  #Pour toujours demander si l'input retourne une erreur
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
                
                #Ajoute le bot si l'option "1 joueur" est sélectionné (Oui, ca marche aussi si le joueur 2 rentre "Bot" en nom)
                if nombre_joueurs == 1:
                    if joueurs[0][1] == "O":
                        joueurs.append(["Bot", "X"])
                    else: 
                        joueurs.append(["Bot", "O"]) 
            
            return joueurs
        
        else:
            print("Nombre de joueurs non pris en charge") 

def tour_suivant(joueurs, joueur_actuel):
    joueur_actuel = (joueur_actuel + 1) % len(joueurs)  # Passer au joueur suivant. Revient au joueur 1 avec le modulo si c'est le dernier joueur

    print(f"\n\nC'est au tour de {joueurs[joueur_actuel][0]} de jouer.")
    return joueur_actuel

print("Bienvenue au Morpion!")

#Variable Globale
resultat = "Aucun"
joueurs = nom_joueurs_lb()
"""
joueurs = [["test", "O"],["testttt", "X"]]
"""
if joueurs[1][0] == "Bot":
    difficulte = input("Choissisez la difficulté: (F)acile, [defaut](N)ormal, (W)arGames. -> ")
"""
joueur_actuel = 1   # Détermine le joueur en cours (1er joueur = 0)
grille = [["","",""],["","",""],["","",""]]
"""
tour = 0

#Boucle de tour
while resultat == "Aucun":
    #Premier tour, on affiche la grille avec les valeurs
    joueur_actuel = tour_suivant(joueurs, joueur_actuel)
    tour += 1

    #Affiche une grille de présentation des numéro de case le 1er tour
    choix = choixCase(grille, joueurs, joueur_actuel)   #Variable/button name to distingush each buttons
    if choix == False:
        print("Erreur de sélection de case du bot!")
    
    #[choix // 3][choix % 3] convertit le nombre de la case choisi en coordonnée
    #ex: 1 // 3 = 0, 1 % 3 = 1 => 0, 1
    grille[(choix - 1) // 3][(choix - 1) % 3] = joueurs[joueur_actuel][1]
   
    resultat = main.verifVainqueur(grille, tour, joueurs, joueur_actuel)
   
    affichage_grille_tk(grille, joueurs, joueur_actuel) #fusion this with choix

if resultat == "Gagné!":
    print(f"\nBravo {joueurs[joueur_actuel][0]}, vous avez Gagné!") #label
elif resultat == "Egalité!":
    print(f"\nC'est une égalité!")                                  #label
else:
    print("Erreur!")                                                #label
"""



affichage_grille_tk(grille, joueurs, joueur_actuel)
