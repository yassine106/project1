from service.gestion import *

print("-----------Bienvenue dans notre application YH-trip-----------\n")

affiche()
var=choisirzone()

while True :
    print("\t-------------------------------------------")
    print("\t\t\t\t\tServices")
    print("\t-------------------------------------------")
    print("Afficher tous les sites de la zone :                               (1)")
    print("Afficher les sites selon un thème donné :                          (2)")
    print("Afficher les sites selon une catégorie donnée :                    (3)")
    print("Afficher les sites qui proposent une visite guidée :               (4)")
    print("Afficher la distance d'un itinéraire passant par pusieurs villes : (5)")
    print("Qutter :                                                           (6)")
    try:  #         pour eviter les valeurs de typs str
        x=eval(input("Veuillez saisir le chiffre covenable à votre service : "))

        if x>6 or x<1  :
            print("S'il Vous Plait vous voulez choisir un chiffre convenable à votre service (1-6)  ;) : ")

        if x == 1 :
            fonction1("Rabat-salé")

        if x == 2 :
            them=input("Veuillez entrer un théme : ")
            fonction2(var,them)

        if x == 3 :
            catg = input("Veuillez entrer une catégorie : ")
            fonction3(var,catg)

        if x == 4 :
            fonction4(var)

        if x == 5 :
            l = list()
            k = eval(input("Veuillez présiser le nombre de site à visiter : "))
            for i in range(k):
                l.append(input("Veuillez entrer le nom de site à visiter : "))
            fonction5(var,l,k)

        if x == 6 :
            break
    except:
        print("S'il Vous Plait vous voulez choisir un chiffre convenable à votre service (1-6)  ;) : ")

print("------- Au revoir ;) -------")