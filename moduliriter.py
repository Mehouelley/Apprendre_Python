#coding: utf-8

"""
un module en pythons est un fichier importer qui contient 
d es fonction pré définir exemple 
import math
pour importer un module on peut 
import <nom_module>
from <nom_module> import <nom_function>
from <nom_module> import *
mais avec la methode from on es plus obliger de fire 
math.sqrt on appele juste la fonction sqrt

on peut creer un dossier pour ranger les module dans ce cas l'appelation 
sera import <nom_dossier>.<nom_module> as <nom_module>
le as permet de renormer le nom dumodule
"""

import math
#import player
#from module.player import au_revoir
resultat=math.sqrt(100)
import module.player
print(resultat)
module.player.au_revoir()
#player.parler("Jason","salut")