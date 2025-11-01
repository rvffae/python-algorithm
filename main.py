#1
print("bonjour monde")


#2
nombre1 = int(input("entrer le premier nombre : "))
nombre2 = int(input("entrer le second : "))

result = nombre1 + nombre2
print(result)

#3
annee_naissance = int(input("entrer votre année de naissance :"))
annee_actuelle = 2025
age = annee_actuelle - annee_naissance
print(age)

#4
celsius = float(input("entrez la température en celsius :"))
fareinheit = (celsius * 9/5) + 32
print(fareinheit)

#5
nombre = int(input("entrez un nombre:"))
if nombre % 2 == 0 :
    print("le nombre est pair")
else :
    print("le nombre est impair")

#6
nombre1_ = int(input("entrer le premier nombre : "))
nombre2_= int(input("entrer le second : "))
if nombre1_ > nombre2_ :
    print("le premier nombre est le plus grand")
else :
    print("le second nombre est le plus grand")
    
#7
_nombre = int(input("entrez un nombre: "))
for i in range (1,11):
    print(_nombre * i) 

#8 
nombre_ex8 = int(input("entrez un nombre :"))
somme = 0
for i in range (nombre_ex8 +1): 
    somme += i
print("la somme est :", somme)

#9
mot = (input("entrez un mot :"))
longueur_mot = len(mot)
print(longueur_mot)


#10
import random
nombre_a_deviner = random.randint(1, 10)
for essai in range(3):
    nombre_a_rentrer = int(input("entrez un nombre :"))
    if nombre_a_rentrer == nombre_a_deviner :
        print("bravo vous avez trouvé le nombre mystère")
        break 
    else : 
        print(f"il vous reste {2-essai} essais")

    if nombre_a_rentrer != nombre_a_deviner:
        print("dommage vous n'avez pas deviné le nombre")

#11
liste_course = []
liste_course.append(input("entrez un premier article : "))
liste_course.append(input("entrez un second article : "))
liste_course.append(input("entrez un troisieme article : "))

print("votre liste de courses est :", liste_course)


#12
mot_secret = "python"
mot_utilisateur = input("entrez un mot:")
while mot_utilisateur != mot_secret:
    print("ce n'est pas le mot secret essayez encore")
    mot_utilisateur = input("entrez un mot:")
    if mot_utilisateur == mot_secret:
        print("bravo vous avez trouvez le mot secret qui était", mot_secret)       
        break
        
#13 
nombre_de_la_factorielle = int(input("entrez un nombre: "))
factorielle = 1 
for i in range(1, nombre_de_la_factorielle+1):
    factorielle = factorielle * i
    print(factorielle)

#14
nombre_pair_impair = int(input("entrez un nombre : "))
for i in range(0, nombre_pair_impair+1):
    if i % 2 == 0:
        print(i)

#15 
note1 = float(input("entrer la premiere note: "))
note2 = float(input("entrer la seconde note: "))
note3 = float(input("entrer la troisieme note: "))
moyenne = (note1 + note2 + note3 ) / 3

print(moyenne)