#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : el-aqqad mohamed





###### les bibliotiques utlisés ################################################
import os, sys
from Tkinter  import *
from random   import *
from math     import *




################# définition d'une cercle ######################################
def cercle(i,j, coul ='red'):
    can.create_oval(40*i,40*j, 40*(i+1), 40*(j+1), outline=coul,fill=coul)




################################################################################
################# définition d'une rectangle:dessine_case ######################
def dessin_case(i,j, coul ='black'):
    can.create_rectangle(40*i,40*j, 40*(i+1), 40*(j+1), outline=coul,fill=coul)
    
    
    
################################################################################    
################# la figure principale :damier #################################
def damier():
    for i in range(10):
        for j in range(10):
            if(i+j)%2==0 :
                dessin_case(i,j)    
            
            
                
                
################################################################################                
################# la contunue d'une case: trois valeurs possibles ##############   
def case_couleur(i,j):
    global  damier_tableau
    return  damier_tableau[10*i+j]




################################################################################
################# la fonction poser_pion: ######################################
def poser_pion(i,j,coul):
    cercle(i,j,coul)
    
    
    
################################################################################
################# fonction principale du jeu:joueur 1  #########################
def jouer1():
    global a
    global b
    global message
    if not(partie_finie()):
        r = int(random()*100)
        if damier_tableau[r]==1 :
                message='tour de joueur 1'
                return 0    
        else :
            if damier_tableau[r]==0 :
                poser_pion(int(r/10),r%10,'red')
                damier_tableau[r]=2
                a+=1
            desactiv1()
            activ2() 
            message='tour de joueur 2'
            widget.configure(text=message)
            wid.configure( text='joueur1: '+ str(a) +'        joueur2:' +str(b))
    else :
        if(b==25):
            message='Partie terminee:les verts gagnent'
        else     :
            message='Partie terminee:les rouges gagnent'
        widget.configure(text=message,font=('Arial','12','bold'),fg='red') 
        desactiv1()
    
    
    
###############################################################################
################# fonction principale du jeu:joueur 2 #########################        
def jouer2():
    global a
    global b 
    global message
    if not(partie_finie()):
        r = int(random()*100)
        if damier_tableau[r]==2 :
                message='tour de joueur 2'
                return 0    
        else: 
            if damier_tableau[r]==0 :
                poser_pion(int(r/10),r%10,'green')
                b+=1
                damier_tableau[r]=2
            
            desactiv2()
            activ1()  
            message='tour de joueur 1'
            widget.configure(text=message)
            wid.configure( text='joueur1: '+str(a) +'        joueur2:' +str(b))
    else :
        if(b==25):       
            message='Partie terminee:les verts gagnent'
        else     :
            message='partie terminee:les rouges gagnent'
        widget.configure(text=message,font=('Arial','14','bold'),fg='green')
        desactiv2()
        
        
        
################################################################################
####################fonction de l'activation des bouton#########################
################################################################################
def desactiv1():
    b1["state"] = "disabled"
def desactiv2():
    b2["state"] = "disabled"
def activ1():
    b1["state"] = "active"
def activ2():
    b2["state"] = "active"
def partie_finie():
    return  a==25 or b==25






################################################################################
###########################programme principale#################################
################################################################################
message='Hello, commancez'
a=0
b=0
damier_tableau=[0  for i in range(100)]
fen = Tk()
can = Canvas(fen, width =400, height =400, bg ='white')
can.pack(side =TOP, padx =5, pady =5)
bot = Button(fen, text ='Quitter', command =fen.quit)
bot.pack(side =RIGHT, padx =3, pady =4)
b1 = Button(fen, text ='joueur 1', command =jouer1)
b1.pack(side =RIGHT, padx =3, pady =4)
b2 = Button(fen, text ='joueur 2', command =jouer2)
b2.pack(side =RIGHT, padx =3, pady =4)
damier()
widget = Label(None, text= message)
widget.pack(side=TOP)
wid = Label(None , text='joueur1: '+ str(a) +'        joueur2:' + str(b) )
wid.pack(side=TOP)
fen.mainloop()
fen.destroy()    
