#coding:UTF-8
#importation de la date en format jj/mm/aaaa
import datetime
#recuperation de la date et de l'heure
currentDateTime = datetime.datetime.now()
#recuperation de la date
date = currentDateTime.date()
#recuperation de l'annee
year = date.strftime("%Y")
year=int(year)

age= input("entrez votre age :")
nom=input("entrez votre nom :")
age=int(age)
annee_nais=year-age

print("{} votre annee de naissance est donc {}".format(nom,annee_nais))
