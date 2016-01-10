#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author : el-aqqad mohamed
################################################################################
#la foction qui retourne les mots qui existe dans un fichier sous forme d'un 
# ensemble de mots
################################################################################
def construire_ensemble(mon_fichier) :
    f=open(mon_fichier, 'r')
    t=set()
    x='er'
    while x!='' :
        x=f.readline()
        if x[:len(x)-1] !='' :
            t.add(x[:len(x)-1])
    f.close()
    return t




################################################################################
#la foction qui prend en argument une liste de lettres et retourne le mot  
# constitue de ces lettres trié
################################################################################
def compose_mot(mot):
    return  [mot[i] for i in range(len(mot))]


################################################################################
# Cette fonction prend en argument deux listes de lettres trié et retourne 
# True si list1 est inclus dans list2 (en comptant les occurences), cette 
# fonction fournit la réponse au question : est ce que on peut obtenir les 
#list1 on suprimant des elements dans la list2
################################################################################
def inclus( list1,list2):
    i=0
    k=0
    for k in range(8) :
        if (list1[i]==list2[k]) :
            i=i+1
            if i==len(list1) :
                return True
    return False
    
            
    
            

################################################################################
#La fonction qui permat de tirer 8 lettres au hazard
################################################################################
def tirage(n) :
    foo=compose_mot('abcdefghijklmnopqrstuvwxyz')
    from random import choice
    t=list()
    for i in range(n) :
        t.append(choice(foo))
    return t


################################################################################
#La fonction qui associe à chaque lettre un point comme un dictionnaire
################################################################################
def dictio_des_points() :
    dictio={}
    for i in ['a','e','i','l','n','r','s','t','u','o'] :
        dictio[i]=1
    for i in ['d','g','m'] :
        dictio[i]=2
    for i in ['b','c','p'] :
        dictio[i]=3
    for i in ['f','h','v'] :
        dictio[i]=4
    for i in ['j','q'] :
        dictio[i]=8
    for i in ['k','w','x','y','z'] :
        dictio[i]=10
    return dictio
################################################################################
# La fonction qui calcul le score d'un mot 
################################################################################
def score(mot) :
     return  sum([dictio_des_points()[mot[i]] for i in range(len(mot))])
    
    
################################################################################
# La fonction qui return le mot de score maximal dans une liste 
################################################################################
def max_score(liste) :
    mot_max=''
    for mot in liste :
        if score(mot_max)<score(mot) :
            mot_max=mot
    return (mot_max, score(mot_max))
     
################################################################################
# La fonction scrable :
# On tire 8 lettres au hazard et on les trient
# on parcour les élément du dictionnaire (l'ensemble de mot) et chaque fois :
## On trie le mot
## On vois est ce que le mot peut être écrit avec les lettres tirer au hazard
################################################################################
def scrable(dictio) :
    lettres=tirage(8)
    print "Les lettres consideres sont :", lettres
    lettres.sort()
    exist=[]
    maxi=''
    for mot in dictio :
        mot_trie=list(mot)
        mot_trie.sort()
        if inclus(mot_trie,lettres) :
            exist.append(mot)
            if len(maxi)<len(mot) :
                maxi=mot
  
    print "La liste de tous les mots possible est: "
    print exist
    print "Le mot de longueur maximale possible est :",maxi
    print "La liste de tous les mots possible avec leur nombre de point est: "
    print zip (exist,[score(mot) for mot in exist])    
    print "Le mot pour lequel le nombre de point est maximal est ", max_score(exist)   
            
    

###############################################################################################
print 'test de la fonction "compose_mot(mot)"__________________________________________________'
print compose_mot('aemr')
print compose_mot('bdrxnde')
print compose_mot('bonjour')
###############################################################################################
print 'test de la fonction "inclus(list1,list2)"_______________________________________________'
print inclus(['a','b','e'], ['a','b','c','d','e','f','g','h'])          #Réponse : oui
print inclus(['a','b','e','e','h'], ['a','b','c','d','e','f','g','h'])  #Réponse :non
print inclus(['a','b','e','h','h'], ['a','b','c','d','e','e','h','h'])  #Réponse :oui
###############################################################################################
print 'test de la fonction "tirage(n)"_________________________________________________________'
print tirage(8)
print tirage(8)
print tirage(7)
###############################################################################################
print 'test de la fonction "dictio_des_points()"_______________________________________________'
print dictio_des_points()['j']
print dictio_des_points()['a']
print dictio_des_points()['x']
###############################################################################################
print 'test de la fonction "score(mot)"________________________________________________________'
print score('jamal')
print score('amalxw')
print score('xwwwxuyyy')
###############################################################################################
print 'test de la fonction "max_score(liste)"__________________________________________________'
print max_score(['et','te','le','il'])
print max_score(['nancy','non','bon'])
print max_score(['exemple','temple','me','ex','text'])






############### Test de la fonction principale scrable ########################################
print '________________________________________________________________________________________'
a=construire_ensemble('frenchssaccent.dic')
scrable(a)



################################################################################
################################################################################
################################################################################
#Changement de quelques fonctions pour utiliser le joker
################################################################################


print '--------------------------------------------------------------------------------------------'
################################################################################
# Principe: on parcourt les lettres de la  list1, si on trouve un lettre qui 
# contenu dans list2 on le supprime de la list2 et si on trouve un lettre qui 
# qui n'est pas contenu dans list2 on supprime le Joker s'il existe et on passe
# au lettre suivant, et à la fin on supprime la lettre  ajouté  pour le joker, 
# pour calculer le score ensuite, en clair la fonction return True ssi tout les 
# éléments de la list1 sont contenus dans la list2 à un lettre près
################################################################################

def inclus_joker( list1,list2):
    if len(list(list1))>=8 :
        return False
    lettre_sup=''
    l2=list2+['?']
    for lettre in list1 :
        if lettre in l2:
            l2.remove(lettre)
        elif '?' in l2 :
            l2.remove('?')
            lettre_sup=lettre
        else :
            return False
    if lettre_sup !='':
        list1.remove(lettre_sup)
    return True



print 'test de la fonction "inclus_joker(list1,list2)"_______________________________________________'
print inclus_joker(['a','b','e','x'],['a','b','c','d','e','f','g'])
print inclus_joker(['a','b','e','x','y'],['a','b','c','d','e','f','g'])            
print inclus_joker(['a','b','e','e'],['a','b','c','d','e','f','g'])
print inclus_joker(['a','f','h','h','e','f','g','b'],['a','b','c','d','e','f','h'])
l=['a','b','e','x']
j=['a','b','c','d','e','f','g']
print inclus_joker(l,j)
print l,j # modification de l 
################################################################################
# Le calcul de score doit être intégré dans la boucle de "parcourt du 
# dictionnaire de fichier" car on perd à chaque fois la lettre ajouté
################################################################################

def scrable_joker(dictio) :
    lettres=tirage(7)
    lettres=['q', 'o', 'r', 'l', 'z', 'n', 'b']
    print "Les lettres consideres sont :", lettres
    lettres.sort()
    exist=[]
    dictionnaire={}
    score_joker_mot=0
    mot_joker_max=''
    for mot in dictio :
        mot_trie=list(mot)
        mot_trie.sort()
        if inclus_joker(mot_trie,lettres) :
            exist.append(mot)
            dictionnaire[mot]=sum([dictio_des_points()[lettre] for lettre in mot_trie])
            if score_joker_mot < dictionnaire[mot] :
                score_joker_mot=dictionnaire[mot]
                mot_joker_max=mot
    print " La liste de tous les mots possible est: "
    print exist
    print " Le nombre de point pour chaque mot:"
    print dictionnaire
    print ' Le mot de score  maximal en utilisant le joker est:',(mot_joker_max,score_joker_mot)
    
############################### fonction principale ############################
print '\n\n Test de la fonction : scrable_joker() -----------------------------------------------------'
scrable_joker(a)
