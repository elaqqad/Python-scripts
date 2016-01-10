#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : el-aqqad mohamed


from Tkinter import *
import random
import time
from time import sleep


##################################################################################
#les initialisations:
#****** voisindesactive=1 : signifie que lorsque on clic sur un botton rien ne se produit
#****** choisir,jouer signifient qu'on pas encore choisi aucune partie et on a pas encore decider de jouer
#****** le nombre de clic est au debut nul
voisindesactive=1
choisir=0
jouer=0
nombreclic=0
dictionnaire={(1,0,0,0,1):[(0,0),(0,1)],(0,1,0,1,0):[(0,0),(0,3)],(1,1,1,0,0):[(0,1),],
              (0,0,1,1,1):[(0,3),],(1,0,1,1,0):[(0,3),],(0,1,1,0,1):[(0,0), ],(1,1,0,1,1):[(0,2), ]}  




################################################################################
# la fonction jouer : lorsque on clic sur le boutton jouer alors on active le jeu 
# s'il est deja desactive et dans l'autre cas on le desactive en ameliorant les 
# condition sur le temps et le nombre de clic
def Jouer() :
    global jouer ,choisir ,nombreclic,maintenant          
    bchoisir.config(text='Choisir configuration')
    choisir=0
    if jouer==0 :
        jouer=1
        nombreclic=0
        bjouer.config(text='Arreter le jeu')
        reset_chrono()
        lancer_chrono()    
            
            
    else :
        jouer=0
        bjouer.config(text='Jouer')
        lscore.config(text='Nombres de clics:'+str(nombreclic))
        stoper_chrono()

# la fonction qui permet d'effacer toute les modification sur les bottons
def effacer():
    for i in range(5):
        for j in range(5) :
            reseau[i][j].config(bg='white'  ) 

# la fonction qui permet de changer la couleur d'un bouton
def changercouleur(x) :
    if reseau[x[0]][x[1]].cget('bg')=='white'   :
        reseau[x[0]][x[1]].config(bg='red')
    else :
        reseau[x[0]][x[1]].config(bg='white'  ) 

# La fonction suivant parmet de choisir une configuration des boutons soit aleatoirement soit
# soit manuellemnt et les conditions ajoutees ont pour but d'ameliorer le choix de la configuration
# par exemple on a pas le droit de choisir une configuration si le jeu est active

def choisir_config() :
    global choisir,jouer,v,nombreclic
    c=v.get()
    if jouer==0 :
        if choisir==1 :
            messagetoplevel2()
            bchoisir.config(text='Choisir configuration')
            choisir=0
        else:
            if c==0:
                messagetoplevel1()
            elif c==1:
                effacer()
                choisir=1
                bchoisir.config(text='Cliquez sur ok')
            else :
                effacer()
                t=[]
                for i in range(5):
                    for j in range(5) :
                        t.append((i,j))
                x=random.choice(range(1,25))
                for l in range(x):
                    f=random.choice(t)
                    t.remove(f)
                    changercouleur(f)
    else :
        messagetoplevel3()
        jouer=0
        bjouer.config(text='Jouer')
        lscore.config(text='Nombres de clics:'+str(nombreclic))
        stoper_chrono()
        
        
        
# cette fonction permet de changer l'etat lorsque on clic sur un bouton , suivant deux cas si on est dans le 
# manuel alors on change l'etat du button sur lequel on a clique et on est dans le jeu alors on change 
# l'etat de tout les voisin de ce bouton
def changeretat(event) :
    global choisir,jouer,nombreclic
    frm1.focus_set()
    num=numbutton(event.widget)
    if choisir==1 and jouer==0:
        changercouleur(num)
    elif jouer==1 and choisir==0:
        for x in voisinage(num[0],num[1]) :
            changercouleur(x)
        nombreclic+=1
        lscore.config(text='Nombres de clics:'+str(nombreclic))
      
      
# le voisinage d'un boutton  
def voisinage(i,j):
    t=[(i,j),]
    if i-1>=0 :
        t.append((i-1,j))
    if i+1<5 :
        t.append((i+1,j))
    if j-1>=0 :
        t.append((i,j-1))
    if j+1<5 :
        t.append((i,j+1))
    return t


# la fonction qui nous donne le numero d'un botton donne , utilisable pour traiter
# l'evenement <Bouton-1>
def numbutton(b):
    for i in range(5):
        for j in range(5):
            if b==reseau[i][j] :
                return (i,j)




# affichages de quelques messages dans la boite de dialogue
def messagetoplevel1():
    chaine='Vous devez choisir un mode de creation de la configuration\n - manuel: vous selectionnez les boutons \
    manellemnet \n- Aleatoire: On choisi une configuration aleatoire : \n\n'
    lboitededialogue.config(text=chaine)
def messagetoplevel2():
    chaine='Votre partie a ete bien choisie \n\n'
    lboitededialogue.config(text=chaine)
def messagetoplevel3():
    chaine='Vous avez quitter le jeu \n\n'
    lboitededialogue.config(text=chaine)
    effacer()
    
    
    
  
# elle retourne la matrice corespendante a l'etat des bouttons sous forme d'un dictionnaire   
def matrice():
    x={}
    for i in range(5):
        for j in range(5):
            x[(i,j)]=int(reseau[i][j].cget('bg')=='red'  )
    return x
     
 
 
     
# Cette permet d'afficher "clic here" sur un bouton donne par ses indices et bloque le programme
# pendant 1 seconde et reprend en effaçant le message affiche , utilisable pour afficher la solution
# poour notre jeu
def clic_here(i,j):
    global nombreclic
    nombreclic=nombreclic+1
    reseau[i][j].config(text='clic here')
    lscore.config(text='Nombres de clics:'+str(nombreclic))
    fen.update()
    sleep(1)
    reseau[i][j].config(text='')
    fen.update() 
    
    
    
    
    
# Cette fonction permet la resolution du jeu  et une affichage lente de la solution 
# et affichage de temp néssaissaire et du nombre cde clic et de affirme si la solution existe 
# j'essaye de decompose cette fonction mais tjs un peut difficile parceque y a pas de repetition
def solution() :
    global nombreclic
    nombreclic=0
    reset_chrono()
    lancer_chrono() 
    lboitededialogue.config(text='je veux essaye, voila faut suivre les clic')
    for i in range(4):
        for j in range(5):
            if matrice()[(i,j)]==1: 
                clic_here(i+1,j)
                for x in voisinage(i+1,j) :                  
                    changercouleur(x)
    x= (matrice()[(4,0)],matrice()[(4,1)],matrice()[(4,2)],matrice()[(4,3)],matrice()[(4,4)])
    if dictionnaire.has_key(x):
        lboitededialogue.config(text='Voila ,je suis un programme fort et j ai trouve \n la solution meme s elle complexe')
        for d in dictionnaire[x] :
            clic_here(d[0],d[1])
            for r in voisinage(d[0],d[1]) :
                changercouleur(r)        
        for i in range(4):
            for j in range(5):
                if matrice()[(i,j)]:
                    clic_here(i+1,j)
                    for r in voisinage(i+1,j) :
                        changercouleur(r)
        x= (matrice()[(4,0)],matrice()[(4,1)],matrice()[(4,2)],matrice()[(4,3)],matrice()[(4,4)])
        if dictionnaire.has_key(x):
            for d in dictionnaire[x] :
                clic_here(d[0],d[1])
                for r in voisinage(d[0],d[1]) :
                    changercouleur(r)        
            for i in range(4):
                for j in range(5):
                    if matrice()[(i,j)]:
                        clic_here(i+1,j)
                        for r in voisinage(i+1,j) :
                            changercouleur(r) 
    elif x==(0,0,0,0,0):
        lboitededialogue.config(text='Voila ,je suis un programme fort et j ai trouve la solution facilement ')
    else :
        lboitededialogue.config(text="j'ai essaye mais,Maleureusement la solution n'existe pas")
    stoper_chrono()



#################################################################################
# les fonctions suivantes sont totalement independantes et servenent a l'affichage du temp ou
# bien le compte-a-rebour


def lancer_chrono():
    global depart,flag
    flag=1
    depart = time.time()
    top_horloge()

def stoper_chrono():
    global flag
    flag=0

def reset_chrono():
    global depart
    depart = time.time()

def top_horloge():
    global depart,flag
    y=time.time()-depart    
    minutes = time.localtime(y)[4]
    secondes = time.localtime(y)[5]
    if flag :
        ltemp.configure(text = "temp  : %i min %i sec " %(minutes,secondes))
    fen.after(1000,top_horloge)
             





#################################################################################
# la vue 
################################################################################
# Fenetre principale       
fen = Tk()
fen.title("Jeu de lights out ")
fen.geometry("580x380")
v = IntVar()

# la Frame qui va contenir les boutons
frm1 = Frame(fen,bd=10)
reseau = []
for i in range( 5):
    ligne=[]
    for j in range(5) :
        btn = Button(frm1, width=10,height=3, image=None,bg='white')
        btn.bind("<Button-1>" ,changeretat)
        btn.grid(row=i, column=j)
        ligne.append(btn)
    reseau.append(ligne)
frm1.grid(row=1,column=1)


# la Frame qui va continire les options 
frm2= Frame(fen,bd=10)
bjouer = Button(frm2,width=20,height=2, text='Jouer',bg='green', command=Jouer)
bjouer.grid(row=1,column=1,columnspan=2)
lscore = Label(frm2,width=20,height=2, text='Nombres de clics:00')
lscore.grid(row=2,column=1,columnspan=2)
ltemp = Label(frm2,width=20,height=2, text='Temps                  :00')
ltemp.grid(row=3,column=1,columnspan=2)
bchoisir =Button(frm2,width=20,height=2, text='Choisir configuration',bg='green', command=choisir_config)
bchoisir.grid(row=4,column=1,columnspan=2)
Radiobutton(frm2, text="Manuel", variable=v, value=1).grid(row=5,column=1)
Radiobutton(frm2, text="Aléatoire", variable=v, value=2).grid(row=5,column=2)
beffacer = Button(frm2,width=20,height=2, text='Effacer',bg='green', command=effacer)
beffacer.grid(row=6,column=1,columnspan=2)
bsolution = Button(frm2,width=20,height=2, text='solution',bg='green', command=solution)
bsolution.grid(row=7,column=1,columnspan=2)
bquitter = Button(frm2,width=20,height=2, text='Quitter',bg='green', command=fen.quit)
bquitter.grid(row=8,column=1,columnspan=2)
frm2.grid(row=1,column=2)


# la Frame 3 : pour afficher la boite de dialogue
frm3= Frame(fen)
lboitededialogue=Label(frm3, text="vous choisissez une configuration initiale et c'est parti!")
lboitededialogue.pack()
frm3.grid(row=2,column=1,columnspan=2)


############### lancement du la fenetre ########################################
fen.mainloop()
fen.destroy()
