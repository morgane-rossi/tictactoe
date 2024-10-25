import tkinter as tk
from tkinter import ttk

def affichage_grille_tk(grille, joueurs, joueur_actuel):
    fenetre = tk.Tk()
    fenetre.title("Morpion")
    fenetre.geometry("600x600")

    fenetre.columnconfigure(0, weight = 1)
    fenetre.columnconfigure(1, weight = 1)
    fenetre.columnconfigure(2, weight = 1)

    def button_u_l_clicked():
        bouton_u_l.config(text = joueurs[joueur_actuel][1])
    def button_u_c_clicked():
        bouton_u_c.config(text = joueurs[joueur_actuel][1])
    def button_u_r_clicked():
        bouton_u_r.config(text = joueurs[joueur_actuel][1])
    
    def button_c_l_clicked():
        bouton_c_l.config(text = joueurs[joueur_actuel][1])
    def button_c_c_clicked():
        bouton_c_c.config(text = joueurs[joueur_actuel][1])
    def button_c_r_clicked():
        bouton_c_r.config(text = joueurs[joueur_actuel][1])

    def button_b_l_clicked():
        bouton_b_l.config(text = joueurs[joueur_actuel][1])
    def button_b_c_clicked():
        bouton_b_c.config(text = joueurs[joueur_actuel][1])
    def button_b_r_clicked():
        bouton_b_r.config(text = joueurs[joueur_actuel][1])
        

    bouton_u_l = ttk.Button(fenetre, text="1", command=button_u_l_clicked)
    bouton_u_l.place(x=0, y=0, width=100, height=100)
    bouton_u_c = ttk.Button(fenetre, text="2", command=button_u_c_clicked)
    bouton_u_c.place(x=0, y=100, width=100, height=100)
    bouton_u_r = ttk.Button(fenetre, text="3", command=button_u_r_clicked)
    bouton_u_r.place(x=0, y=200, width=100, height=100)

    bouton_c_l = ttk.Button(fenetre, text="4", command=button_c_l_clicked)
    bouton_c_l.place(x=100, y=0, width=100, height=100)
    bouton_c_c = ttk.Button(fenetre, text="5", command=button_c_c_clicked)
    bouton_c_c.place(x=100, y=100, width=100, height=100)
    bouton_c_r = ttk.Button(fenetre, text="6", command=button_c_r_clicked)
    bouton_c_r.place(x=100, y=200, width=100, height=100)

    bouton_b_l = ttk.Button(fenetre, text="7", command=button_b_l_clicked)
    bouton_b_l.place(x=200, y=0, width=100, height=100)
    bouton_b_c = ttk.Button(fenetre, text="8", command=button_b_c_clicked)
    bouton_b_c.place(x=200, y=100, width=100, height=100)
    bouton_b_r = ttk.Button(fenetre, text="9", command=button_b_r_clicked)
    bouton_b_r.place(x=200, y=200, width=100, height=100)

    fenetre.mainloop()
