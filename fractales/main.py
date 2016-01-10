# -*- coding: utf-8 -*-
"""
Created on Fri Jun 06 14:32:55 2014

@author: elaqqad1u
"""

from Tkinter import *
from math import *


###############################################################################
#la foction qui retourne la chaine de caracrtère constitueé de 'F' et '+' et '-' 
# pour le flocon passage de niveau n aux niveau n+1
###############################################################################

def flocon_changer_niveau(chaine) :
    ch=''
    for car in chaine :
        if car=='F' :
            car='F+F--F+F'
        ch+=car
    return ch

################################################################################
#La fonction qui gener la chaine de caractère du flocon d'ordre n
###############################################################################
def flocon(n) :
    if n<0 :
        return ''
    flocon='F'
    for i in range(n):
        flocon=flocon_changer_niveau(flocon)
    return flocon

# Test  
print 'flocons________________________________________________________________________\n'
print 'n=0 :',flocon(0)
print 'n=1 :',flocon(1)
print 'n=2 :',flocon(2)
print '\n\n'





###############################################################################
#la foction qui retourne la chaine de caracrtère constitueé de 'F' , '+' ,'-', 
# '(' et ')' pour le premier arbre passage de niveau n aux niveau n+1
###############################################################################
def arbre_changer_niveau(chaine) :
    ch=''
    for car in chaine :
        if car=='F':
            car='F+(F)-F-(F)+F'
        ch+=car
    return ch


################################################################################
#La fonction qui gener la chaine de caractère de l'arbre d'ordre n
###############################################################################
def arbre(n) :
    if n<0 :
        return ''
    arbr='F'
    for i in range(n):
        arbr=arbre_changer_niveau(arbr)
    return arbr
 
# Test  
print 'Arbres________________________________________________________________________\n'  
print 'n=0 :',arbre(0)
print 'n=1 :',arbre(1)
print 'n=2 :',arbre(2)
print '\n\n'



###############################################################################
#la foction qui retourne la chaine de caracrtère constitueé de 'F' , '+' ,'-', 
# '(',')' et 'G' pour le deuxième arbre passage de niveau n aux niveau n+1
###############################################################################
def plante_changer_niveau(chaine) :
    ch=''
    for car in chaine :
        if car=='F' :
            car='G+(F)--(F)+GF'
        elif car=='G' :
            car='GG'
        ch+=car
    return ch
################################################################################
#La fonction qui gener la chaine de caractère de la plante d'ordre n
###############################################################################
def plante(n) :
    if n<0 :
        return ''
    pl='F'
    for i in range(n):
        pl=plante_changer_niveau(pl)
    return pl
    
# Test  
print 'plantes________________________________________________________________________\n'
print 'n=0 :',plante(0)
print 'n=1 :',plante(1)
print 'n=2 :',plante(2)
print '\n\n'


###############################################################################




################################################################################
# La fonction affiche:
# cette fonction prend en argument une figure (representant une fonction de type :
# flocon , arbre ou plante ) et un entier n et affiche la figure d'ordre n . 
## l'argument rotation correspont à l'angle de rotation , et l correspond a la 
## la longeur maximale (l est pris comme puissance de la base a=2 ou 3 pour eviter
## d'obtenir des nombre avec la virgule )
################################################################################

def affiche(n,figure,l,a,rotation=pi/5):
    x,y=400,800
    longueur=l/a**n
    dxf,dyf=0,-longueur
    #print n
    dxg,dyg=0.5*dxf,0.5*dyf
    angle=0
    t=[]
    can.delete('all')
    pl=figure(n)
    for k in pl :
       if k=='+' :
           angle+=-rotation
           dxf=longueur*sin(angle)
           dyf=-longueur*cos(angle)
           dxg,dyg=0.5*dxf,0.5*dyf
       elif k=='-' :
           angle+=rotation
           dxf=longueur*sin(angle)
           dyf=-longueur*cos(angle)
           dxg,dyg=0.5*dxf,0.5*dyf
       elif k=='(' :
           t.append((x,y))
       elif k==')' :
           (x,y)=t.pop()    
       elif k=='F' :
           can.create_line(x,y,x+dxf,y+dyf)     
           x=x+dxf
           y=y+dyf
       else :
           can.create_line(x,y,x+dxg,y+dyg)     
           x=x+dxg
           y=y+dyg 





################################################################################
#Les deux fonction qui affiche le flocon dans le canvas et egalement passer 
# passer entre les ordres du flocan j'ai limiter l'ordre à 7 ( car a partir
# de 7 on obtient pas de resultat convenable)
###############################################################################
def suivant_flocon():
    global configuration
    configuration[0]= (configuration[0]+1)%7
    affiche(configuration[0],flocon,729,3,pi/3)
def precedent_flocon():
    global configuration
    configuration[0]= (configuration[0]-1)%7
    affiche(configuration[0],flocon,729,3,pi/3)
    

################################################################################
#Les deux fonction qui affiche l'arbre 1 dans le canvas et egalement passer 
# passer entre les ordres du l'arbre j'ai limiter l'ordre à 8 ( car a partir
# de 8 on obtient pas de resultat convenable)
###############################################################################
def suivant_arbre():
    global configuration
    configuration[1]= (configuration[1]+1)%8
    affiche(configuration[1],arbre,729,3,pi/6)
def precedent_arbre():
    global configuration
    configuration[1]= (configuration[1]-1)%8
    affiche(configuration[1],arbre,729,3,pi/6)


################################################################################
#Les deux fonction qui affiche le plante dans le canvas et egalement passer 
# passer entre les ordres du plante j'ai limiter l'ordre à 9 ( car a partir
# de 9 on obtient pas de resultat convenable)
###############################################################################
def suivant_plante():
    global configuration
    configuration[2]= (configuration[2]+1)%9
    affiche(configuration[2],plante,768,2,pi/5)
def precedent_plante():
    global configuration
    configuration[2]= (configuration[2]-1)%9
    affiche(configuration[2],plante,768,2,pi/5)
    
    
    
'''     Le programme permetttant de creer la fenetre et les boutton et le canvas et 
leurs affichage , la methode grid permet de les organiser '''
 
fen = Tk()
can = Canvas(fen,bg='dark gray', height=800,width=800)
b_quitter=Button(fen, text='Quitter', command=fen.destroy)
b_flocon_sui=Button(fen, text='Flocon sui', command=suivant_flocon  )
b_flocon_pre=Button(fen, text='Flocon pre', command=precedent_flocon)
b_arbre_sui =Button(fen, text='Arbre sui' , command=suivant_arbre   )
b_arbre_pre =Button(fen, text='Arbre pre' , command=precedent_arbre )
b_plante_sui=Button(fen, text='Plante sui', command=suivant_plante  )
b_plante_pre=Button(fen, text='Plante pre', command=precedent_plante)
b_flocon_sui.grid(row =1, sticky =E)
b_arbre_sui.grid (row =2, sticky =E)
b_plante_sui.grid(row =3, sticky =E)
b_flocon_pre.grid(row =1, column =2)
b_arbre_pre.grid (row =2, column =2)
b_plante_pre.grid(row =3, column =2)
b_quitter.grid(row=4,column=1,columnspan=2)
can.grid(row =1, column =3, rowspan =4, padx =10, pady =5)
configuration =[0,0,0]
fen.mainloop()
