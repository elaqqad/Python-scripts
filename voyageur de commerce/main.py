#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : el-aqqad mohamed


from Tkinter import *
from math import sqrt
import random
import os



################# la fonction qui permet d'afficher un trajet de violles #######

def affichertrajet(villes,couleur) :
    for i in range(len(villes)):
        fond.create_line(villes[i-1][1][0],villes[i-1][1][1],villes[i][1][0],villes[i][1][1],fill=couleur)
        fond.create_text(villes[i][1][0],villes[i][1][1]+10,text=villes[i][0],font="Arial 12 italic")






################## la fnction qui calcule la distanse d'un trajet ##############

def sommetrajet(villes):
    s=0
    for i in range(len(villes)):
        d=sqrt((villes[i-1][1][0]-villes[i][1][0])**2+(villes[i-1][1][1]-villes[i][1][1])**2)
        s=s+d
    return s




print('\ntest:sommetrajet(villes)_______________________________________________')
vils=[ ["carre1",[1,12]]  ,  ["carre2",[40,12]]  ,  ["carre3",[40,45]]  ,["carre4",[1,45]] ]
print(vils)
print(sommetrajet(vils))




#################### la fonstion qui echange deux villes dans un trajet ########

def echangerdeuxvilles(villes,i,j) :
    v=villes.pop(i)
    villes.insert(i, villes.pop(j-1))
    villes.insert(j, v) 
 
 
 
 
print('\ntest:echangerdeuxvilles(villes,i,j)____________________________________')   
t=[1,2,3,4]
print (t)
echangerdeuxvilles(t,1,2)
print (t) 



#################### la fonction, qui cree un ensemble de villes au hazard ##### 

def creervilleshazard(n) :
    villes=[]
    for i in range(n):
        x = random.randint(1,500)
        y= random.randint(1,500)  
        villes.append(['V'+str(i), [x,y]]) 
    return  villes



#################### la fonction qui optimize le trajet ########################


def optimizertrajet(villes) :
    for i in range(100*len(villes)) :
        i = random.randint(0,len(villes)-2)
        j = random.randint(0,len(villes)-2) 
        s1=sommetrajet(villes)
        echangerdeuxvilles(villes,i,j) 
        s2=sommetrajet(villes)
        if s1>s2 :
            echangerdeuxvilles(villes,min(i,j),max(i,j)) 




print('\n Test : creervilleshazard(10) et optimizertrajet(villes) _____________')
villes=creervilleshazard(10)
print (villes)
optimizertrajet(villes)
print (villes)


################### substituer une ligne en une listes de mot ##################



def substituer(ligne):
    l=[]
    t=''
    for i in range(len(ligne)):
        if (ligne[i]==' ' or ligne[i]=='\n') :
            if t!='' :
                l.append(t)
            t=''
        else :
            t=t+ligne[i]
    if t!='':
        l.append(t)
    return l



print('\n Test:substituer(ligne):  _____________________________________________')
print(substituer("123   234   34545 \n\n 432432"))



################### substituer une ligne en une listes de mot ##################




def substituer2(ligne):
    l=[]
    t=''
    for i in range(len(ligne)):
        if (ligne[i]==';' or ligne[i]=='\n') :
            l.append(t)
            t=''
        else :
            t=t+ligne[i]
    if t!='':
        l.append(t)
    return l
print('\n Test : substituer2(ligne): ___________________________________________')
print(substituer2("je;suis;un;voyageur;de;commerce ;    !;"))




###############################################################################
###############################################################################
# la fenetre principale 

racine=Tk()
fond=Canvas(racine, width=500, height=500, background='darkgray')
fond.pack()



################################################################################
# creation de la carte 
fichier = open("france_vect.txt", "r")
ligne='  '
while ligne!='':
    ligne=fichier.readline()
    if ligne=='' :
        break   
    x=substituer(ligne)
    fond.create_line(int(x[0]),int(x[1]),int(x[2]),int(x[3]),fill='green')
fichier.close()




################################################################################
# creation de l'ensemble de villes de la  France
fichier = open("villes.txt", "r")
ligne=' '
villes=[]
while ligne!='':
    ligne=fichier.readline()
    if ligne=='' :
        break   
    x=substituer2(ligne)
    if int(x[4])>150000 :
        villes.append([x[3],[int((float(x[8])-55638)/2373.64) , 500+int((-float(x[9])+6049646.90)/2373.64)]])
fichier.close()



################################################################################
# Affichage de l'optiomization du trajet de notre voyageur
################################################################################
print('\n---------------------------------------------------------------------')
print('-----------------------------------------------------------------------')
print('les villes considéré et leurs cordonnées:\n')
print (villes)
affichertrajet(villes,'blue')
optimizertrajet(villes)
affichertrajet(villes,'red')





racine.mainloop()
