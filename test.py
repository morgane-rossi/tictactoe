tableau_jeu = [
[" "," "," "],
[" "," "," "],
[" "," "," "] ]

def interface_tictactoe(tableau_jeu):

    print(" ", " ", "|", "1", "|", "2", "|", "3")
    print(" ", "-------------")
    print("A", " ", "|", (tableau_jeu[0][0]), "|", (tableau_jeu[0][1]), "|", (tableau_jeu[0][2]), "|")
    print("---------------")
    print("B", " ", "|", (tableau_jeu[1][0]), "|", (tableau_jeu[1][1]), "|", (tableau_jeu[1][2]), "|")
    print("---------------")
    print("C", " ", "|", (tableau_jeu[2][0]), "|", (tableau_jeu[2][1]), "|", (tableau_jeu[2][2]), "|")
    print(" ", "-------------")
    
def gagnant_oupas(tableau_jeu):
    
    if tableau_jeu[0][0] == tableau_jeu[1][1] == tableau_jeu[2][2] and tableau_jeu[0][0] in ["X","O"]:
        if tableau_jeu[0][0] == "X":
            print(f"{joueur1}, you won !")
        else: print(f"{joueur2}, you won !")
        return True
    elif tableau_jeu[0][2] == tableau_jeu[1][1] == tableau_jeu[2][0] and tableau_jeu[0][2] in ["X","O"]:
        if tableau_jeu[0][2] == "X":
            print(f"{joueur1}, you won !")
        else: print(f"{joueur2}, you won !")
        return True
    elif tableau_jeu[0][0] == tableau_jeu[1][0] == tableau_jeu[2][0] and tableau_jeu[0][0] in ["X","O"]:
        if tableau_jeu[0][0] == "X":
            print(f"{joueur1}, you won !")
        else: print(f"{joueur2}, you won !")
        return True
    elif tableau_jeu[0][1] == tableau_jeu[1][1] == tableau_jeu[2][1] and tableau_jeu[0][1] in ["X","O"]:
        if tableau_jeu[0][1] == "X":
            print(f"{joueur1}, you won !")
        else: print(f"{joueur2}, you won !")
        return True
    elif tableau_jeu[0][2] == tableau_jeu[1][2] == tableau_jeu[2][2] and tableau_jeu[0][2] in ["X","O"]:
        if tableau_jeu[0][2] == "X":
            print(f"{joueur1}, you won !")
        else: print(f"{joueur2}, you won !")
        return True
    elif tableau_jeu[0][0] == tableau_jeu[0][1] == tableau_jeu[0][2] and tableau_jeu[0][0] in ["X","O"]:
        if tableau_jeu[0][0] == "X":
            print(f"{joueur1}, you won !")
        else: print(f"{joueur2}, you won !")
        return True
    elif tableau_jeu[1][0] == tableau_jeu[1][1] == tableau_jeu[1][2] and tableau_jeu[1][0] in ["X","O"]:
        if tableau_jeu[1][0] == "X":
            print(f"{joueur1}, you won !")
        else: print(f"{joueur2}, you won !")
        return True
    elif tableau_jeu[2][0] == tableau_jeu[2][1] == tableau_jeu[2][2] and tableau_jeu[2][0] in ["X","O"]:
        if tableau_jeu[2][0] == "X":
            print(f"{joueur1}, you won !")
        else: print(f"{joueur2}, you won !")
        return True
    else:
        for ligne in tableau_jeu:
            for element in ligne:
                if element == " ":
                    return False

def interactions(tableau_jeu):
    tour_joueur = True
    while gagnant_oupas(tableau_jeu) == False:
            if tour_joueur:
                choix_position = input(f"{joueur1} (X), choisissez la position (A1, B2, C3...): ")
            else:
                choix_position = input(f"{joueur2} (O), choisissez la position (A1, B2, C3...): ")
                 


            positions = {
                "A1": (0, 0), "A2": (0, 1), "A3": (0, 2),
                "B1": (1, 0), "B2": (1, 1), "B3": (1, 2),
                "C1": (2, 0), "C2": (2, 1), "C3": (2, 2)
            }

            if choix_position in positions:
                x, y = positions[choix_position]

                if tableau_jeu[x][y] == " ":
                    tableau_jeu[x][y] = "X" if tour_joueur else "O"
                    tour_joueur = not tour_joueur
                else:
                    print("Case déjà prise, essayez une autre position.")
            else:
                print('Entrez une case existante (EX. A1, C3...)')
            interface_tictactoe(tableau_jeu)  
    

tour_joueur1 = True
tour_joueur2 = False
interface_tictactoe(tableau_jeu)
joueur1 = input("Joueur 1, entrez votre nom: ")
joueur2 = input("Joueur 2, entrez votre nom: ")


print("Bonjour,", joueur1, "c'est a vous de commencer !")

interactions(tableau_jeu)