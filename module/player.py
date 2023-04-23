#coding: utf-8
"""
Module pour les joueur
"""
def parler(personnage ,message):
    print("{}: {}".format(personnage,message))

def au_revoir():
    print("au revoir")

if __name__=="__main__":
    print("module player")
    
    parler("Jason","salut")
    au_revoir() 