#coding:UTF-8
"""
les variables en pythons  : doivent commencer par une lettre
                            ne contient pas des caractere speciaux 
                            ne contient pas d'espace
                            peut utiliser des underscore(_)
                        
types de variable standars : entier numerique (int)
                             nombre flotant (float)
                             chaine de caractere (str)
                             boleen(bool)
                             autres (liste,dictionnaire, tuple, etc ...)

Fonctions vues : print("")-> afficher du texte
                 input("")-> lire au clavier
                 type()   -> retourne le type d'une donnees , variable etc 
                 int(),float(),str(),bool() -> "caster" une donner 
                 str.format()-> formater une chaine de caractere
"""
#declaration des variables
#declarer une variable entier numerique
AgePersonne=12
#declarer une variable chaine de caractere
AgePersonne2="25"
#AgePersonne2=int(AgePersonne2)
AgePersonne3=AgePersonne + int(AgePersonne2)
#PrixHts=input('quel est le prix')
#PrixHts= int(PrixHts)
#PrixTtc= PrixHts + (PrixHts*20/100)
ContinuePartie=True
ContinuePartie2=False
#NomJoueur= input("Quel est votre nom : ")
#afficher les phrases
""" commentaire sur plusieur ligne  """
#print("\tbonjour tout le monde \n \tle ciel est couvert de l'air")
"""print(type(AgePersonne));
print(type(AgePersonne2));
print(type(PrixHts));
print(type(ContinuePartie));"""
#
texte="l'age de la personne est {} et le prit vaut {}$"
#print(texte.format(AgePersonne,PrixHts));
#print("bienvenue ",NomJoueur,"tu as acces a ton terminal")
ContinuePartie= int(ContinuePartie)
ContinuePartie2= int(ContinuePartie2)
print(ContinuePartie)
print(ContinuePartie2)
print(AgePersonne3)



