import grille_module
import joueurs_module
import tour_module
import choix_module
import verification_module
import affichage_module

#[Jeremy] Intro du jeu

print("Bienvenue au Morpion!")
resultat = "Aucun"
joueurs = joueurs_module.nomJoueurs()
joueurActuel = 1
grille = grille_module.newGrille()    
tour = 0

while resultat == "Aucun":
    joueurActuel = tour_module.tourSuivant(joueurs, joueurActuel)
    choix = int(choix_module.choixCase())
    grille[(choix - 1) // 3][(choix - 1) % 3] = joueurs[joueurActuel][1]
    resultat = verification_module.verifVainqueur(grille)
    affichage_module.affichageGrille(grille)
if resultat == "Egalité!":
    print(f"\nC'est une égalité!")
else:
    print(f"\nBravo {joueurs[joueurActuel][0]}, vous avez Gagné!")

# noms des joueurs(Moussa) 
def nomJoueurs():
    nombre_joueurs = int(input("Combien de joueurs ? "))
    joueurs = []
    for i in range(nombre_joueurs):
        nom = input(f"Entrez le nom du joueur {i+1} : ")
        symbole = input(f"Rentrez un symbole: ")
        joueurs.append([nom, symbole])
    return joueurs

def tourSuivant(joueurs, joueur_actuel):
    global tour
    tour += 1
    # Index du joueur en cours
    joueur_actuel = (joueur_actuel + 1) % len(joueurs)  # Passer au joueur suivant

    print(f"\nC'est au tour de {joueurs[joueur_actuel][0]} de jouer.")
    return joueur_actuel

   