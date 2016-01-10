# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 14:51:49 2014

@author: elaqqad1u
"""

import random
from Tkinter import *
from math import *
from time import sleep




###############################################################################
# La Classe Noeud définie à partir d'un nombre i , avec la methode d'affichage
###############################################################################
class Noeud:
    def __init__(self,i):
        self.label = i
        self.succ = []
    def __str__(self) :
        return str("%s[%s]"%(self.label,",".join(map(str,self.succ))))
     
# Test de la première classe :Noeud        
print '\n Test de la classe Noeud'
N1=Noeud(1)
N2=Noeud(2)
N3=Noeud(3)
N3.succ.append(N1)
N3.succ.append(N2)
print " L'affichage de N1=",N1
print " L'affichage de N2=",N2
print " L'affichage de N3=",N3
print "\n\n"
###############################################################################
# La Classe Vecteur définie avec deux réels (les cordonnées) à laquelle on  
# l'associe plusieurs methodes : str(),norme(),homothetie(),...
###############################################################################        
class Vecteur:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s,%s)" % (self.x,self.y)

    def norme(self):
        return sqrt(self.x*self.x+self.y*self.y)

    def homothetie(self,c):
        return Vecteur(self.x * c, self.y * c)

    def __add__(self,other):
        return Vecteur(self.x+other.x, self.y + other.y)


# Test de la deuxième classe :Vecteur        
print '\n Test de la classe Vecteur'
v1=Vecteur(1 ,2)
v2=Vecteur(4,-7)
v3=v1+v2
print " v1=Vecteur(1 ,2) donne v1=",v1
print " v2=Vecteur(4,-7) donne v2=",v2
print " v3=v1+v2         donne v3=",v3
print " v1.norme()               =",v1.norme()
print " v2.homothetie(-1)        =",v2.homothetie(-1)
print "\n\n"



###############################################################################
#la foction qui retourne le graphe de divisibilité d'un itervalle d'entier [2,n+3]
# avec n un parametre fournie en argument.
###############################################################################
def graphe_divisibilite(n) :
    t=[]
    for i in xrange(2,n+4) :
        t.append(Noeud(i))
    for i in xrange(2,n+4) :
        k=1
        while k*i<n+4 :
            t[i-2].succ.append(t[k*i-2])
            k=k+1
    return t




###############################################################################
# La foction qui retourne la force electromgnetique entre deux vecteurs passés
# en argument.
###############################################################################

def force_electromagnetique(vect1,vect2,t=1) :
    global q
    if t==0 :
        q=200
    l=sqrt((vect1.x-vect2.x)**2 +(vect1.y-vect2.y)**2)+1
    return Vecteur(q*(vect1.x-vect2.x)/l**3 ,q*(vect1.y-vect2.y)/l**3)
    
# Test de la fonction :force_electromagnetique(vect1,vect2)      
print '\n Test de la fonction :force_electromagnetique(vect1,vect2)'
v1=Vecteur(1 ,2)
v2=Vecteur(4,-7)
print " force_electromagnetique(v1,v2)=",force_electromagnetique(v1,v2,0)
print "\n\n"



###############################################################################
# La foction qui retourne la force du au ressort entre deux vecteurs passés
# en argument.
###############################################################################
def force_ressort(vect1,vect2,t=0) :
    global L,k
    if t==0:
        L,k=40,0.08
    l=1+sqrt((vect1.x-vect2.x)**2 +(vect1.y-vect2.y)**2)
    constante=k*(L-l)
    return Vecteur(constante*(vect1.x-vect2.x)/l ,constante*(vect1.y-vect2.y)/l)

# Test de la fonction :force_ressort(vect1,vect2)
print '\n Test de la fonction : force_ressort(vect1,vect2)'
v1=Vecteur(1 ,2)
v2=Vecteur(4,-7)
print " force_ressort(v1,v2) = ",force_ressort(v1,v2,0)
print "\n\n"



###############################################################################
# La foction qui retourne les positions et les vitesses des elements d'un graphe
# aprés avoir appliquer les forces electromagnitique,ressort rt celles de frottement
# a tout ses noeuds avec (g,pos,vit) initiales.
###############################################################################
def appliquer_forces(g,pos,vit):
    resultantes={n:Vecteur() for n in g}
    for n in g:
        for m in n.succ:
            resultantes[n]+=force_ressort(pos[n],pos[m])
    for n in g:
        for m in g:
            resultantes[n]+=force_electromagnetique(pos[n],pos[m])
    for n in g:
        resultantes[n]+=vit[n].homothetie(-0.002) 
    vitesses={n:vit[n]+resultantes[n] for n in g}
    position={n:pos[n]+resultantes[n] for n in g}
    return (position,vitesses)
# Le test de cette fonction sera effectué dans l'interface graphique   


###############################################################################
# La foction qui affiche le movement des Noeuds du graphe suite au forces appliquer
# sur les noeuds  on affiche 400 mouvement infinitésimale à chaque etape et on peut 
# appuyer sur suivant pour afficher les 400 mvts siuvantes
###############################################################################
def stabilise(g):
    global pos,L,q
    global vit,temp
    i=0
    while i<400 :  
        (pos,vit)=appliquer_forces(g,pos,vit)
        dessine(g,pos)
        sleep(temp)
        i+=1
    

###############################################################################
# La foction qui permet de dessiner un graphe en lui passant le grahe et les positions
# des neouds en paramètres.
###############################################################################    
def dessine(g,pos):
    can.delete("all")
    for n in g:
        for m in n.succ:
            can.create_line(pos[n].x,pos[n].y,pos[m].x,pos[m].y)
    for n in g:
        can.create_oval(pos[n].x-10,pos[n].y-10,pos[n].x+10,pos[n].y+10,fill='red')
        can.create_text(pos[n].x,pos[n].y,text=str(n.label))
    can.update()


###############################################################################
# La foction principale
###############################################################################
if __name__ == '__main__':
    # creation de graphe de divisibilité avec les positions
    g=graphe_divisibilite(8)
    pos = {n : Vecteur(300+200*(random.random()-0.5),300+200*(random.random()-0.5)) for n in g}
    vit = {n : Vecteur(30*(random.random()-0.5),30*(random.random()-0.5)) for n in g}
    
    # initialisation des parametres du problème
    L=40
    q=400
    k=0.04
    temp=0.001
    
    # creation de l'interface graphique
    fen = Tk()
    can = Canvas(fen,bg='dark gray', height=600,width=600)
    b1=Button(fen, text='Quitte', command=fen.destroy)
    b1.pack(side=RIGHT, padx=3, pady=3)
    b2=Button(fen, text='Suivant', command=lambda: stabilise(g))
    b2.pack(side=LEFT, padx=3, pady=3)
    dessine(g,pos)
    can.pack()
    
    # affichage de la fenetre
    fen.mainloop()
