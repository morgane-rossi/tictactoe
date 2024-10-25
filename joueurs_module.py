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