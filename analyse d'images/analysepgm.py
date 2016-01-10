#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : el-aqqad mohamed

from Tkinter import *
#from string import *
#from os import *

################################################################################
################################################################################
def creer_tableau_1D(l,valeur):
	t=[valeur]*l
	return t



################################################################################
#la creation d'une matrice de dimension l*h et contient une valeur par tout#####
################################################################################
def creer_matrice(h,l,valeur):
	t=creer_tableau_1D(h,valeur)
	for i in range(0,h):
		t[i]=creer_tableau_1D(l,valeur)
	return t
################################################################################
#creer un fichier à partir d'une matrice donnée et et lui attribue un nom ######
################################################################################
def creer_fichier_image(t,nom,max):
        h=len(t)   				                                # hauteur de l'image
	l=len(t[0])				                                # largeur de l'image
	fichier = open(nom,'wb')	                                        # crée le fichier texte
	largeur = str(l) 		                                        # transforme la valeur l en texte
	hauteur = str(h) 		                                        # transforme la valeur h en texte
	valmax = str(max)		                                        # transforme la valeur max en texte
	fichier.write('P5\n'+largeur+' '+hauteur+'\n'+valmax+'\n')              # écrit l'entête
	for i in range(h):
		for j in range(l):
			pix=t[i][j]			
                        fichier.write(chr(pix))      # la valeur du pixel est convertie en texte
	fichier.close()
	
	
################################################################################
# transformer un fichier P2 en une matrice et retourner cette matrice ##########
################################################################################
def lire_fichier_image(nom):
	f=open(nom,'rb')
	mode=f.readline()
	dim=f.readline()	
	t_dim=dim.split()
	largeur=int(t_dim[0])  
	hauteur=int(t_dim[1])
	t_image=creer_matrice(hauteur,largeur,0)	                        #creation da la matrice				
	f.readline()
	for i in range(hauteur):
		for j in range (largeur):
			t_image[i][j]=ord(f.read(1))
                        	
			
	f.close()
	return t_image
################################################################################
# inverser les couleurs noir et blanc d'une matrice et retourner le resultat####
################################################################################
def inverser_couleurs_matrice(t):
	l = len(t) 		                           
	h = len(t[0])
        t_image=creer_matrice(l,h,0)	                                        #creation da la matrice
	for i in range(h):
		for j in range (l): 
			t_image[j][i]=255-t[j][i]
	
        return t_image


################################################################################
#tronsposer une matrice donné et retourner la matrice transposé (faire rotation)
################################################################################
def transpose_matrice(t):
	l= len(t) 		                           
	h= len(t[0])
        t_image=creer_matrice(h,l,0)	                                        #creation da la matrice
	for i in range(h):
		for j in range (l): 
			t_image[i][j]=t[j][i]
	
        return t_image


################################################################################
#conteur d' une matrice donné et retourner la matrice du conteur
################################################################################
def contour_matrice(t):
	l= len(t) 		                           
	h= len(t[0])
        t_image=creer_matrice(l,h,0)	                                        #creation da la matrice
	for i in range(1,l-1):
		for j in range (1,h-1): 
			a=-t[i-1][j-1]-t[i][j-1]-t[i+1][j-1]-t[i-1][j]+8*t[i][j]-t[i+1][j]-t[i-1][j+1]-t[i][j+1]-t[i+1][j+1]
			a=min(255,a)
			t_image[i][j]=max(0,a)
					
        return t_image
################################################################################
#Embossage d' une matrice donné et retourner la matrice du conteur
################################################################################
def embossage_matrice(t):
	l= len(t) 		                           
	h= len(t[0])
        t_image=creer_matrice(l,h,0)	                                        #creation da la matrice
	for i in range(1,l-1):
		for j in range (1,h-1): 
			a=-2*t[i-1][j-1]-t[i][j-1]-t[i-1][j]+t[i+1][j]+t[i][j+1]+2*t[i+1][j+1]
			a=min(255,a)
			t_image[i][j]=max(0,a)
					
        return t_image
################################################################################
#inverser les couleurs R et V d'une image et l'enregestrer sous un nouveau nom##
################################################################################
def inverser_couleurs_image(nom):
        matrice=lire_fichier_image(nom)
        matrice_inverse=inverser_couleurs_matrice(matrice)
        fichier=open(nom,'rb')                                                  #ouverture du fichier
        mode=fichier.readline() 
        dim=fichier.readline()
        t_dim=dim.split()
        l=int(t_dim[0]) 
        h=int(t_dim[1])
        val_max=fichier.readline()
	fichier.close()
        creer_fichier_image(matrice_inverse,'inverse_'+nom,val_max)
	
################################################################################
#transposer une image et l'enregestrer sous un nouveau nom (transpose +nom) ####
################################################################################
def transpose_image(nom) :
        matrice=lire_fichier_image(nom)
        matrice_transpose=transpose_matrice(matrice)
        fichier=open(nom,'rb')                                                  #ouverture du fichier
        mode=fichier.readline() 
        dim=fichier.readline()
        t_dim=dim.split()
        l=int(t_dim[0]) 
        h=int(t_dim[1])
        val_max=fichier.readline()
        creer_fichier_image(matrice_transpose,'transpose_'+nom,val_max)
        fichier.close()	

################################################################################
#contour d' une image et l'enregestrer sous un nouveau nom (contour +nom) ######
################################################################################
def contour_image(nom) :
        matrice=lire_fichier_image(nom)
        matrice_contour=contour_matrice(matrice)
        fichier=open(nom,'rb')                                                  #ouverture du fichier
        mode=fichier.readline() 
        dim=fichier.readline()
        t_dim=dim.split()
        l=int(t_dim[0]) 
        h=int(t_dim[1])
        val_max=fichier.readline()
	fichier.close()	
        creer_fichier_image(matrice_contour,'contour_'+nom,val_max)
################################################################################
#l'embossage d' une image et l'enregestrer sous un nouveau nom (embossage +nom) 
################################################################################
def embossage_image(nom) :
        matrice=lire_fichier_image(nom)
        matrice_embossage=embossage_matrice(matrice)
        fichier=open(nom,'rb')                                                  #ouverture du fichier
        mode=fichier.readline() 
        dim=fichier.readline()
        t_dim=dim.split()
        l=int(t_dim[0]) 
        h=int(t_dim[1])
        val_max=fichier.readline()
	fichier.close()	
        creer_fichier_image(matrice_embossage,'embossage_'+nom,val_max)        
	
	
################################################################################
#les commandes des bottons #####################################################
################################################################################
def afficher():
        global photo,nom
        photo=PhotoImage(file=nom)
        item=can1.create_image(160,160,image=photo)
def inverser():
        global photo,nom
        inverser_couleurs_image(nom)
        photo=PhotoImage(file='inverse_'+nom)
        can1.create_image(160,160,image=photo)
def transposer():
        global photo,nom
        transpose_image(nom)
        photo=PhotoImage(file='transpose_'+nom)
        can1.create_image(160,160,image=photo)
def contour():
        global photo,nom
        contour_image(nom)
        photo=PhotoImage(file='contour_'+nom)
        can1.create_image(160,160,image=photo)
def contour1():
        global photo,nom
        contour_image(nom)
        inverser_couleurs_image('contour_'+nom)	
        photo=PhotoImage(file='inverse_contour_'+nom)
        can1.create_image(160,160,image=photo)
def embossage():
        global photo,nom
        embossage_image(nom)
        photo=PhotoImage(file='embossage_'+nom)
        can1.create_image(160,160,image=photo)
def embossage2():
        global photo,nom
        embossage_image(nom)
        inverser_couleurs_image('embossage_'+nom)	
        photo=PhotoImage(file='inverse_embossage_'+nom)
        can1.create_image(160,160,image=photo)
	
	
################################################################################
#Botton de validation de du texte entré par le calvier
################################################################################
def Verification():
        global nom
        nouveau=Motdepasse.get()
	if nouveau[-4:]=='.pgm':
		f=0
		try :
			
			
		        f=open(nouveau,'rb')
		        nom=nouveau
		        txt2.configure(text=' Image choisie :'+nom)
		        f.close()
		except :
			donothing()
			
	else :
		
	        donothing()     
	       
	
def donothing():
        filewin = Toplevel(fen1)
	chaine='Vous devez saisir un nom qui se termine par .pgm \n\
	et qui existe dans le même repertoire que le fichier sourse'
        butt = Button(filewin, text=chaine)
        butt.pack()

################################################################################
#creation de la fenetre et les botton et les convas...###########################
################################################################################            
fen1=Tk()
can1 = Canvas(fen1, width =400, height =400, bg ='ivory')
photo =PhotoImage(file ='Mines_gris.pgm')
can1.create_image(160, 160, image =photo)
nom='Smiley_gris.pgm'
txt1 = Label(fen1, text ='choisir le nom d\'une image')
txt2 = Label(fen1, text =' Image choisie :'+nom)
Motdepasse= StringVar()
entr1= Entry(fen1, textvariable= Motdepasse, bg ='bisque', fg='maroon')
entr1.focus_set()
Bouton = Button(fen1, text ='Valider', command = Verification)
b_afficher= Button(fen1, text='  afficher        ', command=afficher   )
b_inverse=  Button(fen1, text='  inverser RV  ', command=inverser      )
b_transpose=Button(fen1, text='  transpose    ', command=transposer    )
b_contour=Button(fen1, text='  contour     ', command=contour    )
b_contour1=Button(fen1, text='  contour1     ', command=contour1    )
b_embossage=Button(fen1, text=' embossage    ', command=embossage    )
b_embossage2=Button(fen1, text='embossage2', command=embossage2    )
b=          Button(fen1, text='  Quitter         ', command=fen1.quit )







################################################################################
#organisation de l'affichage des canvas et des botton avec la methode grid######
################################################################################
txt1.grid(row =1, sticky =E)
entr1.grid(row =2, sticky =E)
txt2.grid(row =3, sticky =E)
b_afficher.grid(row =4, sticky =E)
b_inverse.grid(row =5, sticky =E)
b_transpose.grid(row=6,sticky =E)
b_contour.grid(row=7,sticky =E)
b_contour1.grid(row=8,sticky =E)
b_embossage.grid(row=9,sticky =E)
b_embossage2.grid(row=10,sticky =E)
b.grid(row=11,sticky =E)
Bouton.grid(row=2,column=2)
can1.grid(row =1, column =3, rowspan =11, padx =10, pady =5)



###############démarrage :######################################################
fen1.mainloop()
fen1.destroy()	
