#coding:UTF-8

"""
Opperateur en python : +(addition)
                       -(soustration)
                       *(multiplication()
                       /(division)
                       %(modulo)-> reste d'une division eucludienne

Incrementation 
variable = variable+x
variable +=x 
Decrementation
variable = variable-x
variable -=x 
multimentation
variable = variable*x
variable *=x 
"""
calcul = 5/2
#calcul= int(calcul)
#calcul= float(calcul)
calcul= str(calcul)
NiveauDepart=input("Quel est votre niveau")
NiveauDepart= int(NiveauDepart)
print("vaute niveau est{}".format(NiveauDepart))
print("ouf vous avez gagnez de niveau")
NiveauDepart= NiveauDepart + 1
print("votre nivau actuelle est ",NiveauDepart)
#print("resultat vaut :",calcul)