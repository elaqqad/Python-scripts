# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 14:51:49 2014

@author: elaqqad1u
"""
import math 
import random
from Tkinter import *


''' Exercice 1,2,3 ________________________________________________________________________________________________'''
''' la definition des methodes modifier, distanc et seloigner _______________________________________________________'''
''' la methode seloigner permet l'objet personner de s'eloigner d'un autre ________________________________________'''
# la defintion de la classe personne
class personne:
  def __init__(self,a,b,c):
    self.x = a
    self.y = b
    self.etat= c
  def __str__(self):
    a='  sain'
    if a==1 :
        a='  malade'
    position="("+str(self.x)+","+str(self.y)+")"
    return position+a
  def modifier (self,d):
    x=random.random()
    y=random.random()
    self.x+=x*d-d/2
    self.y+=y*d-d/2
  def distance (self,other):
    return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)
  def seloigner (self,other,d):
    if self.x < other.x :
        if self.y <other.y :
               x=random.random()
               y=random.random()
               self.x+=-x*d/2
               self.y+=-y*d/2 
        else  :
               x=random.random()
               y=random.random()
               self.x+=-x*d/2
               self.y+=y*d/2
    else :
        if self.y <other.y :
               x=random.random()
               y=random.random()
               self.x+=x*d/2
               self.y+=-y*d/2 
        else  :
               x=random.random()
               y=random.random()
               self.x+=x*d/2
               self.y+=y*d/2 



'''la fonction permettant de passer à l'etape suivante ________________________________________________________________'''
def next_etape(population,rayon,delta,contagion) :
    # remplir le tableau des suciptibles d'etre malade
    suciptibles=[]
    for individu in population :
        if individu.etat==0 :
            T[individu]+=1
            for j in population :
                if individu.distance(j)<rayon :
                    suciptibles.append(j)
    #changement des etats des elements en tableux des suciptibles
    for individu in suciptibles :
        probab=random.random()
        if probab<contagion :
           individu.etat=0
    # mouvement de la population 
    for individu in population :
        individu.modifier(delta)
        
     
''' la fonction qui permet d'afficher une population ____________________________________________________________________'''
def affiche():
    can.delete('all')
    for i in population:        
        can.create_oval(int(200+400*i.x),int(200+400*i.y),
                                  int(200+400*i.x)+10,int(200+400*i.y)+10,
                                  fill='red' if not i.etat else 'green')  
''' les commandes _____________________________________________________________________________________________________'''
# commander affichage normale                                  
def suivant():
    next_etape(population,rayon,delta,contagion)
    affiche()
    
    
# commande affiche en tenant compte des voles   
def suivant_vol() :
    next_etape(population,rayon,delta,contagion)
    for i in range(vol) :
        n=random.randint(1,N)
        individu=population[n-1]
        individu.x=random.random()
        individu.y=random.random()
    affiche()
    
    
 # commande affiche en tenant compte des retablissements    
def retablissement() :
    next_etape(population,rayon,delta,contagion)
    for individu in population :
        if T[individu]>=periode :
            T[individu]==0
            individu.etat=1
    affiche()
    
 # commande affiche en tenant compte de la maladie mortels     
def mortelle() :
    next_etape(population,rayon,delta,contagion)
    for individu in population :
        if T[individu]>=periode_2 :
            population.remove(individu)
    affiche()
       

     
# commande affiche de sorte que les personnes sains se sauvent  
def se_sauver() :
    next_etape(population,rayon,delta,contagion)
    for individu in population :
        if T[individu]>=1 :
            for j in population :
                if T[j]==0 and j.distance(individu)<= 4*rayon:
                    j.seloigner(individu, delta)
    affiche()
 





''' L'interface graphique qui contient plusieurs botton chaque botton fait appelle à un module donne  '''


fen = Tk()
can = Canvas(fen,bg='dark gray', height=800,width=800)
b1=Button(fen, text='Quitte', command=fen.destroy)
b1.pack(side=RIGHT, padx=3, pady=3)
b2=Button(fen, text='normale', command=suivant)
b2.pack(side=LEFT, padx=3, pady=3)
b3=Button(fen, text='Suivant_vol', command=suivant_vol)
b3.pack(side=LEFT, padx=3, pady=3)
b4=Button(fen, text='Retablissement', command=retablissement)
b4.pack(side=LEFT, padx=3, pady=3)
b5=Button(fen, text='Mortelle', command=mortelle)
b5.pack(side=LEFT, padx=3, pady=3)
b6=Button(fen, text='Se sauver', command=se_sauver)
b6.pack(side=LEFT, padx=3, pady=3)
can.pack()


''' les intialisations _________________________________________________________________________________________'''
N = 1000              # le nombre des personnes
contagion = 0.1       # la probabilite de contagation
rayon = 0.05          # le rayon de contagation
delta = 0.01          # la constante de deplacement
periode=10            # La periode de retablisement 
periode_2=10          # la periode ou la personne malade devient mort
vol=20                # Le nombre de vols possibles
T={}                  # Ce dictionnaire contient le nombre d'etape de maladie pour tout individu 
# initialiser le tableau du population
population = [personne(random.random(),random.random(),1) for i in range(N)]
population[0].etat= 0
# initialiser le dictionnaire de nombre des etape passee sur un individu passe en cle 
for individu in population :
    T[individu]=0


''' test des premiers fonctions et methodes ____________________________________________________________________'''

print 'Affichage d une personne  -------------------------------------------------------------------------------'
individu= personne(3,5,1)
print (individu)

print 'Test de la methode modifier  ----------------------------------------------------------------------------'
individu= personne(30,50,1)
individu.modifier(10)
print (individu)

print 'Test de la methode distance  ----------------------------------------------------------------------------'
indinvidu_1=personne(0,0,1)
indinvidu_2=personne(4,3,0)
print indinvidu_1.distance(indinvidu_2)




affiche() 
fen.mainloop()