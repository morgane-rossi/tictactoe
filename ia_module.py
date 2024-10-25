#import time
def ia(grille, signe):
        #time.sleep(3)
        
        #choisi une case dans l'ordre (la premiere qui est disponible)
        for case_choisi in range(9):
            if not grille[case_choisi // 3][case_choisi % 3]:       
                return case_choisi + 1
            else:
                continue

        return False


#print(ia(grille, signe))

"""
test = [[0,0],[0,1],[0,2]]
test.remove([0,0])
print(test)
"""