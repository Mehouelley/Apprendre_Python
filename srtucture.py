#coding:UTF-8

"""
Operateur de comparaisons : == (egal à)
                            != (différent de )
                            <  (plus petit que)
                            >   (plus grand que)
                            <=   (plus petit ou égal à)
                            >=   (plus grand ou égal à)

Mots clés des conditions  : if / elif / else

Condition multiples       : and (ET)
                            or (OU)
                            in / not in (DANS PAS DANS)
"""
identifiant="Fabrice"
mot_de_passe = "password1234"
#Age = input("entrez votre age :")
#Age = int(Age)
print("--------------Interface de connexion---------------")

#user_id=input("entrez votre identifiant : ")
#user_pass=input("entrez votre password : ")
#letrre_hasard= input("entrez votre letrre : ")
"""
if(user_id==identifiant and user_pass==mot_de_passe):{
    print("vous etes connecter bienvenue {}".format(user_id))
}
else:{
 print("information incorect")
}
"""

letrre_hasard= input("entrez votre letrre : ")
if(letrre_hasard not in "aeiouy"):
    print(letrre_hasard," est un consomne")

else:
    print(letrre_hasard," est un voyelle")

"""
if (Age > 0 and Age<18):
    print("tu es mineur")

elif(Age==18):
    print("tu es majeur")

elif(Age>18 and Age<=100):
    print("tu viellir")

else:
    print("la mort te guette")

"""