# -*- coding: utf-8 -*-
"""
Created on Fri May 30 14:42:59 2014

@author: elaqqad1u
"""

class Noeud:
    # initialisation d'un Noeud
    def __init__(self, categorie, mot = None, successeurs = [], father=None):
        self.cate = categorie
        self.mot = mot
        self.succ = successeurs
        self.father=father
        
        
    def __str__(self):
        chaine=''
        if self.succ != []:
            chaine_fils=''
            for i in self.succ:
                chaine_fils+=str(i)+','
            chaine=self.cate+'(' +chaine_fils[:-1] +')'
        elif self.mot !=None :
            chaine='('+self.cate+':'+self.mot+')'
        else :
            chaine=self.cate
        return chaine
        
        
    def racine(self):
        if self.father==None :
            return self
        else :
            return self.father.racine()
            
            
    def nb_ancetres(self) :
         if self.father==None :
            return 0
         else :
            return 1+self.father.nb_ancetres()
            
            
    def phrase(self) :
        if self.mot!=None :
            return self.mot
        else :
            phra=''
            for n in self.succ :
                phra+=n.phrase()+' '
            return phra[:-1]
            
            
    def noeuds(self, cate) :
        table_neouds=[]
        if self.cate==cate :
            table_neouds.append(self)
        if self.mot == None :
            for n in self.succ:
                table_neouds+=n.noeuds(cate)
        return table_neouds
    def copie(self):
        if self.succ==[] :
            nouveau=Noeud(self.cate,self.mot,[],None)
            return nouveau
        else :
            succs=[]
            for n in self.succ :
                succs.append(n.copie())
            nouveau=Noeud(self.cate,self.mot,succs,None)
            for n in nouveau.succ :
                n.father=nouveau 
            return nouveau


''' des fonctions auxilières ---------------------------------------------------------------------------'''

# La fonction permettant l'affichage d'une liste de noeuds
def affichage( liste_noeuds) :
    return [ str(n) for n in liste_noeuds]
    

# la fonction permettant la lecture d'un fichier  
def read_file(fileName):
    f = open(fileName)
    l = f.readline()
    liste =[]
    for i in range(int(l)):
        args = f.readline().rstrip().split(" ")
        if len(args) == 1:
            liste.append(Noeud(args[0],None,[],None))
        else:
            liste.append(Noeud(args[0],args[1],[],None))
    for line in f:
        l1,l2 = line.split("->")
        liste[int(l2)].father=liste[int(l1)]
        liste[int(l1)].succ.append(liste[int(l2)])
    return liste[0]



# La fonction permettant le changement de deux noeuds de meme cate
def changer_noeuds(neud1, neud2,cate,n=0,m=0):
    les_neud1=neud1.noeuds(cate)
    les_neud2=neud2.noeuds(cate)
    if n>=len(les_neud1) :
        n=len(les_neud1)-1
    if m>=len(les_neud2) :
        m=len(les_neud2)-1    
    if n<0 or m<0 :
        print " l'une des phrase ne contient pas la categorie demende "
        return 
    tem= les_neud1[n].succ
    les_neud1[n].succ=les_neud2[m].succ
    les_neud2[m].succ=tem
    tem= les_neud1[n].mot
    les_neud1[n].mot=les_neud2[m].mot
    les_neud2[m].mot=tem 
    tem= les_neud1[n].father
    les_neud1[n].father=les_neud2[m].father
    les_neud2[m].father=tem     



# La fonction permettant le changement de deux noeud dans une meme phrase
def changer_noeuds_int(neud,cate,n=0,m=1): 
    les_neud=neud.noeuds(cate)
    if m<=n :
        t=n
        n=m
        m=(t==n)*(t+1)+ (t!=n)*t
        
    if  m>=len(les_neud):
        print " la phrase ne contient pa la categorie demande  "
        return 
    temp= les_neud[n].succ
    les_neud[n].succ=les_neud[m].succ
    les_neud[m].succ=temp    
    tem= les_neud[n].mot
    les_neud[n].mot=les_neud[m].mot
    les_neud[m].mot=tem
    tem= les_neud[n].father
    les_neud[n].father=les_neud[m].father
    les_neud[m].father=tem    


# La fonction qui return toutes les permutation possibles entre deux noeuds
def permutations(noeud1, noeud2):
    permuts=[(noeud1,noeud2)]
    cate=noeud1.cate
    les_neud=noeud2.noeuds(cate)
    if len(les_neud)!=0 :
        for k in range(len(les_neud)) :
            a=noeud1.copie()
            b=noeud2.copie()
            c=b.noeuds(cate)
            tem=a.succ
            a.succ=c[k].succ
            c[k].succ=tem
            tem=a.mot
            a.mot=c[k].mot
            c[k].mot=tem 
            tem=a.father
            a.father=c[k].father
            c[k].father=tem 
            permuts.append([a,b])
    if noeud1.succ !=[] :
        for k in range(len(noeud1.succ)):
            permuts_succ=permutations(noeud1.succ[k],noeud2)
            for n in permuts_succ :
                a=noeud1.copie()
                a.succ[k]=n[0]
                permuts.append([a,n[1]])
    return permuts
                
                
            
            
            
            
    
    
    
    










#___________________________________________________________________________________________________________

print '____________________________________________________________________________________________________'
print " Test de la classe et la methode d'affichage\n "       
n1=Noeud("NP", "Jean",[],None)
n2=Noeud("V", "dort",[],None)
n3=Noeud("S", None, [n1, n2],None)
n1.father=n3
n2.father=n3

print 'n1=Noeud("NP", "Jean") donne :          ', n1
print 'n2=Noeud("V", "dort") donne :           ', n2
print 'n3=Noeud("S", None, [n1, n2]) donne :   ', n3
print '\n\n'



#___________________________________________________________________________________________________________

print '____________________________________________________________________________________________________'
'''Test de l'affichage de la phrase correspondante a un noeud '''


print " Test la methode phrase\n" 
print 'n1.phrase() donne : ' ,n1.phrase()
print 'n2.phrase() donne : ' ,n2.phrase()
print 'n3.phrase() donne : ' ,n3.phrase()
print '\n\n'




#___________________________________________________________________________________________________________

print '____________________________________________________________________________________________________'
''' Test de la methode noeuds '''

print " Test de la methode noeuds : donnant les sous-noeuds dont la categorie est donnee \n" 
x1=n1.noeuds("NP")
x2=n2.noeuds("NP")
x3=n3.noeuds("NP")
print 'x1=n1.noeuds("NP") donne : ' , affichage(x1)
print 'x2=n2.noeuds("NP") donne : ' , affichage(x2)
print 'x3=n3.noeuds("NP") donne : ' , affichage(x3)
print '\n\n'

#___________________________________________________________________________________________________________

print '____________________________________________________________________________________________________'
''' Test de la methode racine() '''

print " Test de la methode racine() \n" 

print 'n1.racine donne : ' , n1.racine
print 'n2.racine donne : ' , n2.racine
print '\n\n'


#___________________________________________________________________________________________________________

print '____________________________________________________________________________________________________'
''' Test de la methode nb_ancetres '''

print " Test de la methode nb_ancetres \n" 

print 'n1.nb_ancetres donne : ' , n1.nb_ancetres()
print 'n2.nb_ancetres donne : ' , n2.nb_ancetres()
print '\n\n'



#___________________________________________________________________________________________________________

print '____________________________________________________________________________________________________'
print ' Test de la fonction lecture de fichier\n '
p1=read_file("p1.txt")
p2=read_file("p2.txt")
p3=read_file("p3.txt")
p4=read_file("p4.txt")
print 'voir la suite de compilation : \n\n'


#___________________________________________________________________________________________________________

print '____________________________________________________________________________________________________'
print ' 1-Test de la fonction __str__ pour les fichiers'
print 'p1= :',p1 
print 'p2= :',p2 
print 'p3= :',p3
print 'p4= :',p4
print '\n\n'


#___________________________________________________________________________________________________________

print '____________________________________________________________________________________________________'
print '2- Test de la fonction  phrase pour les fichiers'
print 'p1.phrase() donne : ' ,p1.phrase()
print 'p2.phrase() donne : ' ,p2.phrase()
print 'p3.phrase() donne : ' ,p3.phrase()
print 'p4.phrase() donne : ' ,p4.phrase()  
print '\n\n'



#___________________________________________________________________________________________________________

print '____________________________________________________________________________________________________'
print "3-Test de la methode noeuds  pour les fichiers avec la categorie 'SN' \n" 
x1=p1.noeuds("SN")
x2=p2.noeuds("SN")
x3=p3.noeuds("SN")
x4=p4.noeuds("SP")
x5=p2.noeuds("N")
print 'x1=p1.noeuds("SN") donne : ' , affichage(x1)
print 'x2=p2.noeuds("SN") donne : ' , affichage(x2)
print 'x3=p3.noeuds("SN") donne : ' , affichage(x3)
print 'x4=p4.noeuds("SP") donne : ' , affichage(x4)
print 'x5=p2.noeuds("N") donne  : ' , affichage(x4)
print '\n\n'

#___________________________________________________________________________________________________________

print '____________________________________________________________________________________________________'
print " Test de la methode racine: On s'interesse a la phrase 2 :\n\t",p2.phrase()
print ' Cherchons la racine de  la premiere composante de x5 et x2 :\n' 
print 'x5[0]= :', x5[0]
print 'x2[0]= :', x2[0] 
print '\n\n'
print 'x2[0].racine() donne  : \n ' , x2[0].racine()
print 'x5[0].racine() donne  : \n ' , x5[0].racine()
print '\n\n'
print 'x2[0].nb_ancetres() donne :' , x2[0].nb_ancetres()
print 'x5[0].nb_ancetres() donne :' , x5[0].nb_ancetres()
print '\n\n'


#___________________________________________________________________________________________________________

print '____________________________________________________________________________________________________'
print ' Test de la fonction changer_noeuds de deux phrases '
changer_noeuds(p1, p2,"SN",2,0)
changer_noeuds(p3, p4,"SN")
print '\n\n Apres changement de neouds \n '

print 'p1.phrase() donne : ' ,p1.phrase()
print 'p2.phrase() donne : ' ,p2.phrase()
print 'p3.phrase() donne : ' ,p3.phrase()
print 'p4.phrase() donne : ' ,p4.phrase()

#___________________________________________________________________________________________________________

print '____________________________________________________________________________________________________'
print " Test de la fonction qui permet d'echanger deux categorie d'une meme phrase \n "
print '**les phrases p1 et p2 avant changement des noeuds \n'
print 'p1.phrase() donne : ' ,p1.phrase()
print 'p2.phrase() donne : ' ,p2.phrase()

changer_noeuds_int(p1,"SN",2,3)
changer_noeuds_int(p2,"N",0,1)

print '\n\n**les deux  phrases p1, p2 apres changement\n \n '
print 'p1.phrase() donne : ' ,p1.phrase()
print 'p2.phrase() donne : ' ,p2.phrase()
changer_noeuds_int(p1,"SN",2,3)
changer_noeuds_int(p2,"N",0,1)
print '\n\n'

#___________________________________________________________________________________________________________

print '____________________________________________________________________________________________________'
print " Test de la fonction affichaons toutes les permutations possibles :\n  "
g=permutations(p1,p2)
for k in g :
    print k[0].phrase() , '\n\t', k[1].phrase()
