import tkinter as tk
from tkinter import ttk

#[Jeremy] Afficher la grille
def affichageGrille(grille):
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

fenetre = tk.Tk()
fenetre.title("Morpion")
fenetre.geometry("600x600")

message = tk.Label(fenetre, text="Hey")
message.pack()

def button_clicked():
    print('buttttton')

bouton = ttk.Button(fenetre, text="clickk", command=button_clicked)
bouton.pack()

fenetre.mainloop()

