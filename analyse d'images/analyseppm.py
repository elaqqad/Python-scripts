#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : el-aqqad mohamed

from Tkinter import *
from string import *



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
	fichier = open(nom,'w')	                                                # crée le fichier texte
	largeur = str(l) 		                                        # transforme la valeur l en texte
	hauteur = str(h) 		                                        # transforme la valeur h en texte
	valmax = str(max)		                                        # transforme la valeur max en texte
	fichier.write('P6\n'+largeur+' '+hauteur+'\n'+valmax+'\n')              # écrit l'entête
	for i in range(h):
		for j in range(l):
			pix=t[i][j]			
                        fichier.write(chr(pix[0])+chr(pix[1])+chr(pix[2]))      # la valeur du pixel bleu est convertie en texte
	fichier.close()


################################################################################
# transformer un fichier P3 en une matrice et retourner cette matrice ##########
################################################################################
def lire_fichier_image(nom):
	f=open(nom,'rb')
	mode=f.readline()
	dim=f.readline()	
	t_dim=dim.split()
	largeur=int(t_dim[0])  
	hauteur=int(t_dim[1])
	t_image=creer_matrice(hauteur,largeur,0)	                        #creation da la matrice				
	coul=[0,0,0]
	f.readline()
	for i in range(hauteur):
		for j in range (largeur):
			for k in range(3):
                        	coul[k] = ord(f.read(1))
                        t_image[i][j]=[coul[0],coul[1],coul[2]]	
			
	f.close()
	return t_image


################################################################################
# inverser les couleurs vert et rouge d'une matrice et retourner le resultat####
################################################################################
def inverser_couleurs_matrice(t):
	l = len(t) 		                           
	h = len(t[0])
        t_image=creer_matrice(l,h,0)	                                        #creation da la matrice
	for i in range(h):
		for j in range (l): 
			t_image[j][i]=[t[j][i][1],t[j][i][0],t[j][i][2]]
	
        return t_image



################################################################################
#tronsposer une matrice donné et retourner la matrice transposé (faire rotation)
################################################################################
def transpose_matrice(t):
	l= len(t) 		                           
	h= len(t[0])
        t_image=creer_matrice(h,l,[0,0,0])	                                        #creation da la matrice
	for i in range(h):
		for j in range (l): 
			t_image[i][j]=[t[j][i][0],t[j][i][1],t[j][i][2]]
	
        return t_image

################################################################################
#conteur d' une matrice donné et retourner la matrice du conteur
################################################################################
def contour_matrice(t):
	l= len(t) 		                           
	h= len(t[0])
        t_image=creer_matrice(l,h,[0,0,0])	                                        #creation da la matrice
	for i in range(1,l-1):
		for j in range (1,h-1): 
			a=-t[i-1][j-1][0]-t[i][j-1][0]-t[i+1][j-1][0]-t[i-1][j][0]+8*t[i][j][0]-t[i+1][j][0]-t[i-1][j+1][0]-t[i][j+1][0]-t[i+1][j+1][0]
			b=-t[i-1][j-1][1]-t[i][j-1][1]-t[i+1][j-1][1]-t[i-1][j][1]+8*t[i][j][1]-t[i+1][j][1]-t[i-1][j+1][1]-t[i][j+1][1]-t[i+1][j+1][1]
			c=-t[i-1][j-1][2]-t[i][j-1][2]-t[i+1][j-1][2]-t[i-1][j][2]+8*t[i][j][2]-t[i+1][j][2]-t[i-1][j+1][2]-t[i][j+1][2]-t[i+1][j+1][2]
			a=min(255,a)
			b=min(255,b)
			c=min(255,c)
			t_image[i][j]=[max(0,a),max(0,b),max(0,c)]
					
        return t_image
################################################################################
#le filtre inverse 255-t pour chaque couleur
################################################################################
def filtre1_matrice(t):
	l= len(t) 		                           
	h= len(t[0])
        t_image=creer_matrice(l,h,0)	                                        #creation da la matrice
	for i in range(l):
		for j in range (h):
			a=255-(t[i][j][0])
			b=255-(t[i][j][1])
			c=255-(t[i][j][2])
			t_image[i][j]=[a,b,c]
					
        return t_image




################################################################################
#le filtre qui permet le repoussage d'une matrice
################################################################################
def repousser_matrice(t):
	l= len(t) 		                           
	h= len(t[0])
        t_image=creer_matrice(l,h,[0,0,0])	                                        #creation da la matrice
	for i in range(1,l-1):
		for j in range (1,h-1): 
			a=-2*t[i-1][j-1][0]-t[i][j-1][0]-t[i-1][j][0]+t[i][j][0]+t[i+1][j][0]+t[i][j+1][0]+2*t[i+1][j+1][0]
			b=-2*t[i-1][j-1][1]-t[i][j-1][1]-t[i-1][j][1]+t[i][j][1]+t[i+1][j][1]+t[i][j+1][1]+2*t[i+1][j+1][1]
			c=-2*t[i-1][j-1][2]-t[i][j-1][2]-t[i-1][j][2]+t[i][j][2]+t[i+1][j][2]+t[i][j+1][2]+2*t[i+1][j+1][2]
			a=min(255,a)
			b=min(255,b)
			c=min(255,c)
			t_image[i][j]=[max(0,a),max(0,b),max(0,c)]
					
        return t_image
################################################################################
#le filtre qui permet la detection des bords de l'image
################################################################################
def bord_matrice(t):
	l= len(t) 		                           
	h= len(t[0])
        t_image=creer_matrice(l,h,[0,0,0])	                                        #creation da la matrice
	for i in range(1,l-1):
		for j in range (1,h-1): 
			a=t[i][j-1][0]+t[i-1][j][0]-4*t[i][j][0]+t[i+1][j][0]+t[i][j+1][0]
			b=t[i][j-1][1]+t[i-1][j][1]-4*t[i][j][1]+t[i+1][j][1]+t[i][j+1][1]
			c=t[i][j-1][2]+t[i-1][j][2]-4*t[i][j][2]+t[i+1][j][2]+t[i][j+1][2]
			a=min(255,a)
			b=min(255,b)
			c=min(255,c)
			t_image[i][j]=[max(0,a),max(0,b),max(0,c)]
					
        return t_image
################################################################################
#le filtre qui rend l'image flou
################################################################################
def flou_matrice(t):
	l= len(t) 		                           
	h= len(t[0])
        t_image=creer_matrice(l,h,[0,0,0])	                                        #creation da la matrice
	for i in range(1,l-1):
		for j in range (1,h-1): 
			a=t[i-1][j-1][0]+t[i][j-1][0]+t[i+1][j-1][0]+t[i-1][j][0]+t[i][j][0]+t[i+1][j][0]+t[i-1][j+1][0]+t[i][j+1][0]+t[i+1][j+1][0]
			b=t[i-1][j-1][1]+t[i][j-1][1]+t[i+1][j-1][1]+t[i-1][j][1]+t[i][j][1]+t[i+1][j][1]+t[i-1][j+1][1]+t[i][j+1][1]+t[i+1][j+1][1]
			c=t[i-1][j-1][2]+t[i][j-1][2]+t[i+1][j-1][2]+t[i-1][j][2]+t[i][j][2]+t[i+1][j][2]+t[i-1][j+1][2]+t[i][j+1][2]+t[i+1][j+1][2]
			a=min(255,a)
			b=min(255,b)
			c=min(255,c)
			t_image[i][j]=[max(0,a),max(0,b),max(0,c)]
					
        return t_image
################################################################################
#le filtre qui permet de contraster l'image
################################################################################
def contraster_matrice(t):
	l= len(t) 		                           
	h= len(t[0])
        t_image=creer_matrice(l,h,[0,0,0])	                                        #creation da la matrice
	for i in range(1,l-1):
		for j in range (1,h-1): 
			a=-0*t[i-1][j-1][0]-t[i][j-1][0]-0*t[i+1][j-1][0]-t[i-1][j][0]+5*t[i][j][0]-t[i+1][j][0]-0*t[i-1][j+1][0]-t[i][j+1][0]-0*t[i+1][j+1][0]
			b=-0*t[i-1][j-1][1]-t[i][j-1][1]-0*t[i+1][j-1][1]-t[i-1][j][1]+5*t[i][j][1]-t[i+1][j][1]-0*t[i-1][j+1][1]-t[i][j+1][1]-0*t[i+1][j+1][1]
			c=-0*t[i-1][j-1][2]-t[i][j-1][2]-0*t[i+1][j-1][2]-t[i-1][j][2]+5*t[i][j][2]-t[i+1][j][2]-0*t[i-1][j+1][2]-t[i][j+1][2]-0*t[i+1][j+1][2]
			a=min(255,a)
			b=min(255,b)
			c=min(255,c)
			t_image[i][j]=[max(0,a),max(0,b),max(0,c)]
					
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
#detecter le contour de l' image et l'enregestrer sous un nouveau nom 
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
        creer_fichier_image(matrice_contour,'contour_'+nom,val_max)
        fichier.close()
################################################################################
#le repoussage de l'image 
################################################################################
def repousser_image(nom) :
        matrice=lire_fichier_image(nom)
        matrice_contour=repousser_matrice(matrice)
        fichier=open(nom,'rb')                                                  #ouverture du fichier
        mode=fichier.readline() 
        dim=fichier.readline()
        t_dim=dim.split()
        l=int(t_dim[0]) 
        h=int(t_dim[1])
        val_max=fichier.readline()
        creer_fichier_image(matrice_contour,'repousser_'+nom,val_max)
        fichier.close()
################################################################################
#la detection des bord d'une image
################################################################################
def bord_image(nom) :
        matrice=lire_fichier_image(nom)
        matrice_contour=bord_matrice(matrice)
        fichier=open(nom,'rb')                                                  #ouverture du fichier
        mode=fichier.readline() 
        dim=fichier.readline()
        t_dim=dim.split()
        l=int(t_dim[0]) 
        h=int(t_dim[1])
        val_max=fichier.readline()
        creer_fichier_image(matrice_contour,'bord_'+nom,val_max)
        fichier.close()
################################################################################
#l'image flou
################################################################################
def flou_image(nom) :
        matrice=lire_fichier_image(nom)
        matrice_contour=flou_matrice(matrice)
        fichier=open(nom,'rb')                                                  #ouverture du fichier
        mode=fichier.readline() 
        dim=fichier.readline()
        t_dim=dim.split()
        l=int(t_dim[0]) 
        h=int(t_dim[1])
        val_max=fichier.readline()
        creer_fichier_image(matrice_contour,'flou_'+nom,val_max)
        fichier.close()
################################################################################
#augmenter le contrast de l'image
################################################################################
def contraster_image(nom) :
        matrice=lire_fichier_image(nom)
        matrice_contour=contraster_matrice(matrice)
        fichier=open(nom,'rb')                                                  #ouverture du fichier
        mode=fichier.readline() 
        dim=fichier.readline()
        t_dim=dim.split()
        l=int(t_dim[0]) 
        h=int(t_dim[1])
        val_max=fichier.readline()
        creer_fichier_image(matrice_contour,'contraster_'+nom,val_max)
        fichier.close()
################################################################################
#Inverser l'imafe sous l'effet de 255-t ####
################################################################################
def filtre1_image(nom) :
        matrice=lire_fichier_image(nom)
        matrice_contour=filtre1_matrice(matrice)
        fichier=open(nom,'rb')                                                  #ouverture du fichier
        mode=fichier.readline() 
        dim=fichier.readline()
        t_dim=dim.split()
        l=int(t_dim[0]) 
        h=int(t_dim[1])
        val_max=fichier.readline()
        creer_fichier_image(matrice_contour,'filtre1_'+nom,val_max)
        fichier.close()




################################################################################
#les commandes des  bottons ####################################################
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
def filtre1():
        global photo,nom
        filtre1_image(nom)
        photo=PhotoImage(file='filtre1_'+nom)
        can1.create_image(160,160,image=photo)
def repousser():
        global photo,nom
        repousser_image(nom)
        photo=PhotoImage(file='repousser_'+nom)
        can1.create_image(160,160,image=photo)	
def bord():
        global photo,nom
        bord_image(nom)
        photo=PhotoImage(file='bord_'+nom)
        can1.create_image(160,160,image=photo)
def flou():
        global photo,nom
        flou_image(nom)
        photo=PhotoImage(file='flou_'+nom)
        can1.create_image(160,160,image=photo)
def contraster():
        global photo,nom
        contraster_image(nom)
        photo=PhotoImage(file='contraster_'+nom)
        can1.create_image(160,160,image=photo)	
def Verification():
        global nom
        nom=Motdepasse.get()
        txt2.configure(text=' Image choisie :'+nom)
def contour_filtre1():
	global photo,nom
	contour_image(nom)
	nom1='contour_'+nom
        filtre1_image(nom1)
        photo=PhotoImage(file='filtre1_'+nom1)
        can1.create_image(160,160,image=photo)	
def Verification():
        global nom
        nouveau=Motdepasse.get()
	if nouveau[-4:]=='.ppm':
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
		print 'thla'     
	       
	
def donothing():
        filewin = Toplevel(fen1)
	chaine='vous devez enter un nom qui se termine par .ppm \n\
	et qui existe dans le même repertoire que le fichier sourse'
        butt = Button(filewin, text=chaine)
        butt.pack()


################################################################################
#cration de la fenetre et les botton et le convas...###########################
################################################################################            
fen1=Tk()
can1 = Canvas(fen1, width =400, height =400, bg ='ivory')
photo =PhotoImage(file ='Mines-256-couleurs.ppm')
can1.create_image(160, 160, image =photo)
nom='Mines-256-couleurs.ppm'
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
b_filtre1=Button(fen1, text='  filtre1     ', command=filtre1   )
b_filtre1_contour=Button(fen1, text='  contour2     ', command=contour_filtre1 )
b_contraster=Button(fen1, text='  contraster     ', command=contraster  )
b_flou=Button(fen1, text='  flou     ', command=flou  )
b_bord=Button(fen1, text='  bord     ', command= bord  )
b_repousser=Button(fen1, text='  repousser     ', command=repousser  )
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
b_repousser.grid(row=8,sticky =E)
b_filtre1_contour.grid(row=9,sticky =E)
b.grid(row=11,sticky =E)
b_contraster.grid(row=10,sticky =E)
b_bord.grid(row=6,column=2)
b_flou.grid(row=4,column=2)
b_filtre1.grid(row=5,column=2)
Bouton.grid(row=2,column=2)
can1.grid(row =1, column =3, rowspan =11, padx =10, pady =5)



###############démarrage :######################################################
fen1.mainloop()
fen1.destroy()
##################fin###########################################################
