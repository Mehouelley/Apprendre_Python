#coding:UTF-8

"""
Operateur de comparaisons : == (egal à)
                            != (différent de )
                            <  (plus petit que)
                            >   (plus grand que)
                            <=   (plus petit ou égal à)
                            >=   (plus grand ou égal à)

Condition multiples       : and (ET)
                            or (OU)
                            in / not in (DANS PAS DANS)
"""
identifiant="Fabrice"
mot_de_passe = "password1234"
print("--------------Interface de connexion---------------")
user_id=input("entrez votre identifiant : ")
user_pass=input("entrez votre password : ")
if(user_id==identifiant and user_pass==mot_de_passe):{
    print("vous etes connecter bienvenue {}".format(user_id))
}
else:{
 print("information incorect")
}
