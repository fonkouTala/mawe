# -*- coding: utf-8 -*-
from Tkinter import*
from tkMessageBox import*
root= Tk()
root.title('Appplication Gestion Structure')

def callback():
    if askyesno('Titre 1', 'Etes-vous sur de vouloir faire ça?'):
        root.destroy()
    else:
  

      showerror("Titre 2", "Revenons donc a l'acueil")


def back_to_home():
	canvas.delete("all")
	title_1= canvas.create_text(50, 50, font=('arial',50,'bold italic'), text="Application Gestion Structure", anchor='w')
	title_2= canvas.create_text(100, 150, font=('courier',50,'bold italic'), text="Welcome to", anchor='w')
	title_3= canvas.create_text(50, 200, font=('arial',40,'bold'), text="Garage la Reference", anchor='w')
	b1= Button(root, font=('Helvetica',18,'bold italic'), text="Gestion des Entreprises", command=next_screen1, activebackground ="red", activeforeground ="yellow", bg='dark green', fg='white', bd=5, anchor='w')
	canvas.create_window(300, 300, width=300, height=90, window=b1)
	b2= Button(root, font=('Helvetica',18,'bold italic'), text="Gestion des Utilisateurs", command=next_screen2, activebackground="red", activeforeground="yellow", bg='dark green', fg='white', bd=5, anchor='w')
	canvas.create_window(300, 400, width=300, height=90, window=b2)
	b3= Button(root, font=('Helvetica',18,'bold italic'), text="Gestion du Personnel", command=next_screen3, activebackground="red", activeforeground="yellow", bg='dark green', fg='white', bd=5, anchor='w')
	canvas.create_window(300, 500, width=300, height=90, window=b3)
	b4= Button(root, font=('Helvetica',18,'bold italic'), text="Gestion des Camions", command=next_screen4, activebackground="red", activeforeground="yellow", bg='dark green', fg='white', bd=5, anchor='w')
	canvas.create_window(900, 300, width=300, height=90, window=b4)
	b5= Button(root, font=('Helvetica',18,'bold italic'), text="Gestion des Depenses", command=next_screen5, activebackground="red", activeforeground="yellow", bg='dark green', fg='white', bd=5, anchor='w')
	canvas.create_window(900, 400, width=300, height=90, window=b5)
	b6= Button(root, font=('Helvetica',18,'bold italic'), text="Etat", command=next_screen6, activebackground="red", activeforeground="yellow", bg='dark green', fg='white', bd=5, anchor='w')
	canvas.create_window(900, 500, width=300, height=90, window=b6)
	boutton_quit= Button(root, font=('Helvetica',18,'bold italic'), text="Quitter", command=callback, activebackground="red", activeforeground="yellow", bg='dark green', fg='red', bd=5, anchor='w')
	canvas.create_window(600, 650, width=300, height=90, window=boutton_quit)
	
  
	


    

    

#bouttons back
def back_gestion_des_camions():
	canvas.delete("all")
	text= canvas.create_text(500, 50, text="Gestion des Camions", font=('Freestyle Script', 40))
	boutton1= Button(root, text="Enregistrement des Camions", command=enregistrement_des_camions, font=('Freestyle Script', 15), bg='white', fg='green')
	canvas.create_window(200, 200, width=300, height=90, window=boutton1)
	boutton2= Button(root, text="Objectifs de chaque Camions", command=objectifs_de_chaque_camions, font=('Freestyle Script', 15), bg='white', fg='green')
	canvas.create_window(600, 200, width=300, height=90, window=boutton2)
	boutton3= Button(root, text="Enregistrement des recettes de Camions", command=enregistrement_des_recettes_de_camions, font=('Freestyle Script', 15), bg='white', fg='green')
	canvas.create_window(250, 400, width=450, height=90, window=boutton3)
	boutton4= Button(root, text="Etat de chaque Camions", command=etat_de_chaque_camions, font=('Freestyle Script', 15), bg='white', fg='green')
	canvas.create_window(700, 400, width=300, height=90, window=boutton4)
	boutton5= Button(root, text="Back to home", command=back_to_home, font=('Freestyle Script', 20), bg='red')
	canvas.create_window(200, 600, width=300, height=90, window=boutton5)

 
def back_etat():
	canvas.delete("all")
	text= canvas.create_text(500, 50, text="Etat", font=('Freestyle Script', 40))
	boutton1= Button(root, text="Affichage des bulletins de paye", command=affichage_des_bulletins_de_paye, font=('Freestyle Script', 15), bg='white', fg='green')
	canvas.create_window(200, 200, width=350, height=90, window=boutton1)
	boutton2= Button(root, text="Affichage des Depenses", command=affichage_des_depenses, font=('Freestyle Script', 15), bg='white', fg='green')
	canvas.create_window(200, 300, width=300, height=90, window=boutton2)
	boutton3= Button(root, text="Affichage des pieces Achetes", command=affichage_des_pieces_achetes, font=('Freestyle Script', 15), bg='white', fg='green')
	canvas.create_window(200, 400, width=300, height=90, window=boutton3)
	boutton4= Button(root, text="Affichage des Camions", command=affichage_des_camions, font=('Freestyle Script', 15), bg='white', fg='green')
	canvas.create_window(700, 200, width=300, height=90, window=boutton4)
	boutton5= Button(root, text="Objectifs du Personnels", command=objectifs_du_personnel, font=('Freestyle Script', 15), bg='white', fg='green')
	canvas.create_window(700, 300, width=300, height=90, window=boutton5)
	boutton6= Button(root, text="Affichage des recettes", command=affichage_des_recettes, font=('Freestyle Script', 15), bg='white', fg='green')
	canvas.create_window(700, 400, width=300, height=90, window=boutton6)
	boutton7= Button(root, text="Affichage des differents ratiaux", command=affichage_des_differents_ratiaux, font=('Freestyle Script', 15), bg='white', fg='green')
	canvas.create_window(1150, 200, width=350, height=90, window=boutton7)
	boutton= Button(root, text="Back to Home", command=back_to_home, font=('Freestyle Script', 20), bg='red')
	canvas.create_window(200, 600, width=300, height=90, window=boutton)


	
#Toplevels
def next_screen1():
	canvas.delete("all")
	texte_1= canvas.create_text(500, 50, font=('arial',20,'bold italic'), text="Gestion des Entreprises")
	texte_2= canvas.create_text(300, 200, font=('arial',15,'italic'), text="Creation de l'entreprise:")
	texte_3= canvas.create_text(300, 300, font=('arial',15,'italic'), text="Modification de l'entreprise:")
	boutton= Button(root, text="Back to Home", command=back_to_home, font=('Freestyle Script', 20), bg='red')
	canvas.create_window(200, 600, width=300, height=90, window=boutton)
	entry1= Entry(root, bd=5, width=5)
	canvas.create_window(600, 200, width=300, height=50, window=entry1)
	entry2= Entry(root, bd=5, width=5)
	canvas.create_window(600, 300, width=300, height=50, window=entry2)


	def textvariable(text):
		entree.delete(0, END)
		entry.insert(0,text)

		return
        entree = Entry(root, textvariable=textvariable, width=30)
        entree.grid(row=1, column=3, pady=(100,50), padx=(200))
  

def next_screen2():
	canvas.delete("all")
  	texte_= canvas.create_text(500, 50, font=('arial',20,'bold italic'), text="Gestion des Utilisateurs")
	texte_1= canvas.create_text(300, 200, font=('arial',15,'bold italic'), text="Utilisateurs")
	boutton= Button(root, text="Back to Home", command=back_to_home, font=('Freestyle Script', 20), bg='red')
	canvas.create_window(200, 600, width=300, height=90, window=boutton)

   










def next_screen3():
	canvas.delete("all")
	texte_= canvas.create_text(500, 50, font=('arial',20,'bold italic'), text="Gestion du Personnel")
	boutton= Button(root, text="Back to Home", command=back_to_home, font=('Freestyle Script', 20), bg='red')
	canvas.create_window(200, 600, width=300, height=90, window=boutton)


 



def next_screen4():
	canvas.delete("all")
	text= canvas.create_text(500, 50, text="Gestion des Camions", font=('Freestyle Script', 40))
	boutton1= Button(root, text="Enregistrement des Camions", command=enregistrement_des_camions, font=('Freestyle Script', 15), bg='white', fg='green')
	canvas.create_window(200, 200, width=300, height=90, window=boutton1)
	boutton2= Button(root, text="Objectifs de chaque Camions", command=objectifs_de_chaque_camions, font=('Freestyle Script', 15), bg='white', fg='green')
	canvas.create_window(600, 200, width=300, height=90, window=boutton2)
	boutton3= Button(root, text="Enregistrement des recettes de Camions", command=enregistrement_des_recettes_de_camions, font=('Freestyle Script', 15), bg='white', fg='green')
	canvas.create_window(250, 400, width=450, height=90, window=boutton3)
	boutton4= Button(root, text="Etat de chaque Camions", command=etat_de_chaque_camions, font=('Freestyle Script', 15), bg='white', fg='green')
	canvas.create_window(700, 400, width=300, height=90, window=boutton4)
	boutton5= Button(root, text="Back to Home", command=back_to_home, font=('Freestyle Script', 20), bg='red')
	canvas.create_window(200, 600, width=300, height=90, window=boutton5)


def next_screen5():
	canvas.delete("all")
	text= canvas.create_text(500, 50, text="Gestion des Depenses", font=('Freestyle Script', 40))

	boutton= Button(root, text="Back to Home", command=back_to_home, font=('Freestyle Script', 20), bg='red')
	canvas.create_window(200, 600, width=300, height=90, window=boutton)

	



def next_screen6():
	canvas.delete("all")
	text= canvas.create_text(500, 50, text="Etat", font=('Freestyle Script', 40))
	boutton1= Button(root, text="Affichage des bulletins de paye", command=affichage_des_bulletins_de_paye, font=('Freestyle Script', 15), bg='white', fg='green')
	canvas.create_window(200, 200, width=350, height=90, window=boutton1)
	boutton2= Button(root, text="Affichage des Depenses", command=affichage_des_depenses, font=('Freestyle Script', 15), bg='white', fg='green')
	canvas.create_window(200, 300, width=300, height=90, window=boutton2)
	boutton3= Button(root, text="Affichage des pieces Achetes",command=affichage_des_pieces_achetes, font=('Freestyle Script', 15), bg='white', fg='green')
	canvas.create_window(200, 400, width=300, height=90, window=boutton3)
	boutton4= Button(root, text="Affichage des Camions", command=affichage_des_camions, font=('Freestyle Script', 15), bg='white', fg='green')
	canvas.create_window(700, 200, width=300, height=90, window=boutton4)
	boutton5= Button(root, text="Objectifs du Personnel", command=objectifs_du_personnel, font=('Freestyle Script', 15), bg='white', fg='green')
	canvas.create_window(700, 300, width=300, height=90, window=boutton5)
	boutton6= Button(root, text="Affichage des recettes", command=affichage_des_recettes, font=('Freestyle Script', 15), bg='white', fg='green')
	canvas.create_window(700, 400, width=300, height=90, window=boutton6)
	boutton7= Button(root, text="Affichage des differents ratiaux", command=affichage_des_differents_ratiaux, font=('Freestyle Script', 15), bg='white', fg='green')
	canvas.create_window(1150, 200, width=350, height=90, window=boutton7)
	boutton= Button(root, text="Back to Home", command=back_to_home, font=('Freestyle Script', 20), bg='red')
	canvas.create_window(200, 600, width=300, height=90, window=boutton)

#fenetres filles pour gestion des camions
def enregistrement_des_camions():
	canvas.delete("all")
	text= canvas.create_text(500, 50, text="Enregistrement des Camions", font=('Freestyle Script', 40))
	boutton= Button(root, text="Back", command=back_gestion_des_camions, font=('Freestyle Script', 20), bg='red')
	canvas.create_window(200, 600, width=300, height=90, window=boutton)

def objectifs_de_chaque_camions():
	canvas.delete("all")
	canvas.create_text(500, 50, text="Objectifs de chaque Camions", font=('Freestyle Script', 40))
	boutton= Button(root, text="Back", command=back_gestion_des_camions, font=('Freestyle Script', 20), bg='red')
	canvas.create_window(200, 600, width=300, height=90, window=boutton)
	

def enregistrement_des_recettes_de_camions():
	canvas.delete("all")
	canvas.create_text(600, 50, text="Enregistrement des recettes de Camions", font=('Freestyle Script', 40))
	boutton= Button(root, text="Back", command=back_gestion_des_camions, font=('Freestyle Script', 20), bg='red')
	canvas.create_window(200, 600, width=300, height=90, window=boutton)

def etat_de_chaque_camions():
	canvas.delete("all")
	canvas.create_text(500, 50, text="Etat de chaque camions", font=('Freestyle Script', 40))
	boutton= Button(root, text="Back", command=back_gestion_des_camions, font=('Freestyle Script', 20), bg='red')
	canvas.create_window(200, 600, width=300, height=90, window=boutton)


#fenetres filles pour Etat
def affichage_des_bulletins_de_paye():
	canvas.delete("all")
	canvas.create_text(500, 50, text="Affichage des bulletins de paye", font=('Freestyle Script', 40))
	boutton= Button(root, text="Back", command=back_etat, font=('Freestyle Script', 20), bg='red')
	canvas.create_window(200, 600, width=300, height=90, window=boutton)

def affichage_des_depenses():
	canvas.delete("all")
	canvas.create_text(500, 50, text="Affichage des Depenses", font=('Freestyle Script', 40))
	boutton= Button(root, text="Back", command=back_etat, font=('Freestyle Script', 20), bg='red')
	canvas.create_window(200, 600, width=300, height=90, window=boutton)

    

def affichage_des_pieces_achetes():
	canvas.delete("all")
	canvas.create_text(500, 50, text="Affichage des pieces Achetes", font=('Freestyle Script', 40))
	boutton= Button(root, text="Back", command=back_etat, font=('Freestyle Script', 20), bg='red')
	canvas.create_window(200, 600, width=300, height=90, window=boutton)

def affichage_des_camions():
	canvas.delete("all")
	canvas.create_text(500, 50, text="Affichage des Camions", font=('Freestyle Script', 40))
	boutton= Button(root, text="Back", command=back_etat, font=('Freestyle Script', 20), bg='red')
	canvas.create_window(200, 600, width=300, height=90, window=boutton)

def objectifs_du_personnel():
	canvas.delete("all")
	canvas.create_text(500, 50, text="Objectifs du Personnel", font=('Freestyle Script', 40))
	boutton= Button(root, text="Back", command=back_etat, font=('Freestyle Script', 20), bg='red')
	canvas.create_window(200, 600, width=300, height=90, window=boutton)

def affichage_des_recettes():
	canvas.delete("all")
	canvas.create_text(500, 50, text="Affichage des recettes", font=('Freestyle Script', 40))
	boutton= Button(root, text="Back", command=back_etat, font=('Freestyle Script', 20), bg='red')
	canvas.create_window(200, 600, width=300, height=90, window=boutton)

def affichage_des_differents_ratiaux():
	canvas.delete("all")
	canvas.create_text(500, 50, text="Affichage des differents ratiaux", font=('Freestyle Script', 40))
	boutton= Button(root, text="Back", command=back_etat, font=('Freestyle Script', 20), bg='red')
	canvas.create_window(200, 600, width=300, height=90, window=boutton)







#fenetre principale
canvas = Canvas(root, width =1400, height =745, bg = 'orange')
canvas.grid() 

title_1= canvas.create_text(50, 50, font=('arial',50,'bold italic'), text="Application Gestion Structure", anchor='w')
title_2= canvas.create_text(100, 150, font=('courier',50,'bold italic'), text="Welcome to", anchor='w')

title_3= canvas.create_text(50, 200, font=('arial',40,'bold'), text="Garage la Reference", anchor='w')

boutton1= Button(root, font=('Helvetica',18,'bold italic'), text="Gestion des Entreprises", command=next_screen1, activebackground ="red", activeforeground ="yellow", bg='dark green', fg='white', bd=5, anchor='w')
canvas.create_window(300, 300, width=300, height=90, window=boutton1)
boutton2= Button(root, font=('Helvetica',18,'bold italic'), text="Gestion des Utilisateurs", command=next_screen2, activebackground ="red", activeforeground ="yellow", bg='dark green', fg='white', bd=5, anchor='w')
canvas.create_window(300, 400, width=300, height=90, window=boutton2)

boutton3= Button(root, font=('Helvetica',18,'bold italic'), text="Gestion du Personnel", command=next_screen3, activebackground ="red", activeforeground ="yellow", bg='dark green', fg='white', bd=5, anchor='w')
canvas.create_window(300, 500, width=300, height=90, window=boutton3)

boutton4= Button(root, font=('Helvetica',18,'bold italic'), text="Gestion des Camions", command=next_screen4, activebackground ="red", activeforeground ="yellow", bg='dark green', fg='white', bd=5, anchor='w')
canvas.create_window(900, 300, width=300, height=90, window=boutton4)

boutton5= Button(root, font=('Helvetica',18,'bold italic'), text="Gestion des Depenses", command=next_screen5, activebackground ="red", activeforeground ="yellow", bg='dark green', fg='white', bd=5, anchor='w')
canvas.create_window(900, 400, width=300, height=90, window=boutton5)

boutton6= Button(root, font=('Helvetica',18,'bold italic'), text="Etat", command=next_screen6, activebackground ="red", activeforeground ="yellow", bg='dark green', fg='white', bd=5, anchor='w')
canvas.create_window(900, 500, width=300, height=90, window=boutton6)

boutton_quit= Button(root, font=('Helvetica',18,'bold italic'), text="Quitter", command=callback, activebackground ="red", activeforeground ="yellow", bg='dark green', fg='red', bd=5, anchor='w')
canvas.create_window(600, 650, width=300, height=90, window=boutton_quit)

root.mainloop()