#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : el-aqqad mohamed




###############################################################################
################les bibliotiques utlisés #######################################
from Tkinter  import *
from random   import *
from math     import *


################################################################################
################définition d'une cercle ########################################
def cercle(x, y, r, coul ='red'):
    can.create_oval(x-r, y-r, x+r, y+r, outline='red',fill=coul)
    
################################################################################    
################la figure pricipale  ###########################################
def figure():
    can.delete(ALL)
    # les variables globales dans la fonction et initialisation 
    global i
    global s
    i=0
    s=0
    # tracer plusieurs cercles concentriques :
    rayon = 180
    cercle(200, 200, 180, 'white')
    while rayon > 60:
        cercle(200, 200, rayon,'white')
        rayon -= 30
    cercle(200, 200, 60 , 'red')
    cercle(200, 200, 30,'white')
    # tracer les deux lignes (vert. et horiz.) :
    can.create_line(200, 0, 200, 400,fill='red',)
    can.create_line(0, 200, 400, 200, fill ='red') 
    # configurer les numéro des cercles 
    can.create_text(200,45, text="1",font=30,fill="red")    
    can.create_text(200,75, text="2",font=30 ,fill="red")
    can.create_text(200,105, text="3",font=30,fill="red")    
    can.create_text(200,135, text="4",font=30,fill="red")    
    can.create_text(200,165, text="5",font=30,fill="white")
    can.create_text(200,200, text="6",font=30,fill="red")    
    
    
    
################################################################################    
################la fonction tirer ##############################################   
def tirer():
        #variables globales
        global s # compteur du score
        global i #compteur de nombre de tirage
        # la contion pour tirer sinon message d'erreur
        if( i>=5) :
            can.delete(ALL)
            can.create_text(200,200,text='impossible!!,svp ,veillez recommancer'\
                            ,font='Arial 16',fill='green')
            return 0
        # générer un cercle aléatoire
        d=5 
        x,y = int(random()*400),int(random()*400)
        can.create_oval(x-d,y-d,x+d,y+d,fill='black')
        r=int(sqrt((x-200)**2+(y-200)**2)/30)
        #incrémanter les variables globales
        s=s+int(r<=6)*(6-r)
        i+=1
        # affichage du score 
        if(i==5):
            score(s)
            
            
################################################################################           
################la fonction qui définie le score et son afffichage##############        
def score(h):
    can.create_text(200,200,text='game over ,your score is  :',font='Arial 19',\
                    fill='blue')
    can.create_text(200,300,text=h,font='Arial 30',fill='blue')
       
       
################################################################################
################Programme principal ############################################
fen = Tk()
can = Canvas(fen, width =400, height =400, bg ='red')
can.pack(side =TOP, padx =5, pady =5)
b1 = Button(fen, text ='Quitter', command =fen.quit)
b1.pack(side =RIGHT, padx =3, pady =4)
figure()
b2 = Button(fen, text ='feu', command =tirer)
b2.pack(side =LEFT, padx =3, pady =3)
b3 = Button(fen, text ='recommencer', command =figure)
b3.pack( padx =3, pady =4)



fen.mainloop()
fen.destroy() 



################################################################################
###############fin du programme#################################################
