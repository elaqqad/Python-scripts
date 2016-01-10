# -*- coding: utf-8 -*-
"""
Created on Fri May 23 14:53:42 2014

@author: elaqqad1u
"""



'''Exercice 1 : Definition de la classe Noeud '''


class Noeud:
    # initialisation d'un Noeud
    def __init__(self, categorie, mot = None, successeurs = []):
        self.x = categorie
        self.y = mot
        self.z = successeurs
        
    # la definition de la methode str()    
    def __str__(self):
        chaine=''
        if self.z != []:
            chaine_fils=''
            for i in self.z:
                chaine_fils+=str(i)+','
            chaine=self.x+'(' +chaine_fils[:-1] +')'
        elif self.y !=None :
            chaine='('+self.x+':'+self.y+')'
        else :
            chaine=self.x
        return chaine
        
    # la definition de la methode phrase
    def phrase(self) :
        if self.y!=None :
            return self.y
        else :
            phra=''
            for n in self.z :
                phra+=n.phrase()+' '
            return phra[:-1]
    #la deffinition de la methode noeuds 
    def noeuds(self, cate) :
        table_neouds=[]
        if self.x==cate :
            table_neouds.append(self)
        if self.y == None :
            for n in self.z :
                table_neouds+=n.noeuds(cate)
    
        return table_neouds
            
'''  une fonction permettant d'afficher une liste  de noeuds'''    
def affichage( liste_noeuds) :
    return [ str(n) for n in liste_noeuds]

print "____________________________________________________________________________________________________________" 
 
print " Test de la classe et la methode d'affichage\n "       
n1=Noeud("NP", "Jean",[])
n2=Noeud("V", "dort",[])
n3=Noeud("S", None, [n1, n2])
print 'n1=Noeud("NP", "Jean") donne :          ', n1
print 'n2=Noeud("V", "dort") donne :           ', n2
print 'n3=Noeud("S", None, [n1, n2]) donne :   ', n3



print "\n\n__________________________________________________________________________________________________________"
'''Exercice 2 : test de l'affichage de la phrase correspondante a un noeud '''


print " Test la methode phrase\n" 
print 'n1.phrase() donne : ' ,n1.phrase()
print 'n2.phrase() donne : ' ,n2.phrase()
print 'n3.phrase() donne : ' ,n3.phrase()




print "\n\n__________________________________________________________________________________________________________"
'''Exercice 4 : test de la methode noeuds '''



print " Test de la methode noeuds : donnant les sous-noeuds dont la categorie est donnee \n" 
x1=n1.noeuds("NP")
x2=n2.noeuds("NP")
x3=n3.noeuds("NP")
print 'x1=n1.noeuds("NP") donne : ' , affichage(x1)
print 'x2=n2.noeuds("NP") donne : ' , affichage(x2)
print 'x3=n3.noeuds("NP") donne : ' , affichage(x3)



print "\n\n__________________________________________________________________________________________________________"
''' Exercice 5 :la fonction qui prend un fichier en parametre et return le noeud corespondant'''


def read_file(fileName):
    f = open(fileName)
    l = f.readline()
    liste =[]
    for i in range(int(l)):
        args = f.readline().rstrip().split(" ")
        if len(args) == 1:
            liste.append(Noeud(args[0],None,[]))
        else:
            liste.append(Noeud(args[0],args[1],[]))
    for line in f:
        l1,l2 = line.split("->")
        liste[int(l1)].z.append(liste[int(l2)])
    return liste[0]



print ' Test de la fonction lecture de fichier\n '
p1=read_file("p1.txt")
p2=read_file("p2.txt")
p3=read_file("p3.txt")
p4=read_file("p4.txt")

print 'p1.phrase() donne : ' ,p1.phrase()
print 'p2.phrase() donne : ' ,p2.phrase()
print 'p3.phrase() donne : ' ,p3.phrase()
print 'p4.phrase() donne : ' ,p4.phrase()




print "\n\n_________________________________________________________________________________________________________"
'''Exercice 5: Une fonction permettant de changer deux  noeuds de categorie cate dont le numero est n et m respectivement
dans le tableau donnant les sous-noeud de neud1 et noeud2'''   



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
    temp= les_neud1[n].z
    les_neud1[n].z=les_neud2[m].z
    les_neud2[m].z=temp
    tem= les_neud1[n].y
    les_neud1[n].y=les_neud2[m].y
    les_neud2[m].y=tem   



print ' Test de la fonction changer_noeuds de deux phrases '
changer_noeuds(p1, p2,"SN",2,0)
changer_noeuds(p3, p4,"SN")
print '\n\n Apres changement de neouds \n '

print 'p1.phrase() donne : ' ,p1.phrase()
print 'p2.phrase() donne : ' ,p2.phrase()
print 'p3.phrase() donne : ' ,p3.phrase()
print 'p4.phrase() donne : ' ,p4.phrase()

print "\n\n_________________________________________________________________________________________________________"
'''Exercice 6 :Etant donne un noeud contenant une categorie aux moins deux fois alors cette fonction permet d'echanger les sous noeuds 
de categorie cate et de numero n et m  '''

def changer_noeuds_int(neud,cate,n=0,m=1): 
    les_neud=neud.noeuds(cate)
    if m<=n :
        t=n
        n=m
        m=(t==n)*(t+1)+ (t!=n)*t
        
    if  m>=len(les_neud):
        print " la phrase ne contient pa la categori demande  "
        return 
    temp= les_neud[n].z
    les_neud[n].z=les_neud[m].z
    les_neud[m].z=temp    
    tem= les_neud[n].y
    les_neud[n].y=les_neud[m].y
    les_neud[m].y=tem   


changer_noeuds(p1, p2,"SN",2,0)
changer_noeuds(p3, p4,"SN")

print " Test de la fonction qui permet d'echanger deux categorie d'une meme phrase \n "
print '**les phrases p1 et p2 avant changement des noeuds \n'
print 'p1.phrase() donne : ' ,p1.phrase()
print 'p2.phrase() donne : ' ,p2.phrase()

changer_noeuds_int(p1,"SN",2,3)
changer_noeuds_int(p2,"N",0,1)

print '\n\n**les deux  phrases p1, p2 apres changement\n \n '
print 'p1.phrase() donne : ' ,p1.phrase()
print 'p2.phrase() donne : ' ,p2.phrase()



    






















