#coding:UTF-8
"""
Fonctions vues   : print()= afficher un texte
                   input()=saisir une valeur
                    type()=type de la valeur
                    int(),float(),str(),bool() = convertir une valeur(castrage)
                    format()=formater une valeur c'

"""
#print("Bonjour à vous ! :)" )
# age=input("Quel est votre age ?")
# age=int(age)
# print("Vous avez {} ans".format(age))

# def dire_bonjour():
#     print("Bonjour à vous ! :)" )
# #je ne suis plus dans la fonction
# dire_bonjour()

def dire1(nom_persenne,message ):
    print("{} : {}".format(nom_persenne,message))
#je ne suis plus dans la fonction
dire1("Mamadou","Bonjour à vous ! :)" )
dire1("Asam ","Comment allez vous ?" )

"""
    avec pythons on peut definir des valeur par defaut
    dans les parametres d'une fonction 
    on peut aussi passer les parametre comme on veut 
    dans l'ordre qu'on veut dans l'appel de la fonction
"""
def dire(nom_persenne="Mamadou",message="Bonjour à vous ! :)" ):
    print("{} : {}".format(nom_persenne,message))
#je ne suis plus dans la fonction
dire(message="Bonjour à vous ! :)" ,nom_persenne="Mamadou" )
"""
    avec pythons l'utilisation de * dans les parametres d'une fonction 
    permet de passer un nombre variable d'arguments
"""
def show_inventory(*items):
    for item in items:
        print(item)
#je ne suis plus dans la fonction
    
show_inventory("epée")
show_inventory("potion de mana","epée","arc","cape de dragon rouge")  

"""
faire une fonction qui retourne la somme de deux nombres
"""
def calculer_somme(nombre1,nombre2):
    resultat=nombre1+nombre2
    return resultat
#je ne suis plus dans la fonction
print(calculer_somme(5,6))

"""
"""
def compare_nombres(nombre1,nombre2):
    if nombre1>nombre2:
        return nombre1
    elif nombre1<nombre2:
        return nombre2
    else:
        return "Les deux nombres sont égaux"
