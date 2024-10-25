grille = [["X","O","O"],["","",""],["","",""]]
signe = "X"


def ia(grille, signe):
        
        
        
        
        
        #choisi une case dans l'ordre (la premiñre qui est disponible)
        for case_choisi in range(9):
            if not grille[case_choisi // 3][case_choisi % 3]:       #convertit le nombre de la case en coordonnée
                return case_choisi
            elif case_choisi == 8:
                return False



#print(ia(grille, signe))

test = [[0,0],[0,1],[0,2]]
test.remove([0,0])
print(test)