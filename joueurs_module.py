#[Moussa] Ajouter/saisir des joueurs
def nomJoueurs():
    nombre_joueurs = 2 #int(input("Combien de joueurs ? "))
    
    """
    class joueurs:
        def __init__(self, nom, symbole):
            self.nom = nom
            self.symbole = symbole
    """

    joueurs = []
        
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
    
    return joueurs