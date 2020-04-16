from exec.Creation import *
import copy

def affiche():                         #     fonction qui affiche tous les zones
    obj = creation
    print("<----____----____----____----____----____----____----____----___")
    print("<-<-<-<-<-< Liste des zones touristiques disponibles >->->->->->")
    for i in obj.zoneliste :
        i.affichezone()
    print("____----____----____----____----____----____----____----____--->\n")

def choisirzone():                    #     fonction pour selectionner une zone
    obj = creation
    while True :
        var = input("---Veuillez saisir le nom de la zone qui vous préférez ;) :")
        for i in obj.zoneliste:
            if var == i.nom:
                print("vous avez choisi : ",var)
                return var
        print(var, "n'éxiste pas sur nos services")


def fonction1(nomm):                  #     fonction qui affiche tous les sites de la zone "nomm"
    obj= creation
    print("<-<-<-<-<-< Liste des sites touristiques de la zone ",nomm," >->->->->->")
    for i in range(obj.dic[nomm].__len__()):
        print("-------->",obj.dic[nomm][i].nom)

def fonction2(nomm,them):             #     fonction qui affiche les sites selon un thème donné
    obj = creation
    for i in range(obj.dic[nomm].__len__()):
        if "theme" in obj.dic[nomm][i].__dict__ and them.lower() == obj.dic[nomm][i].theme.lower()  :
            print("\n-------->",obj.dic[nomm][i].nom)

def fonction3(nomm,catg):             #     fonction qui affiche les sites selon une catégorie donnée
    obj = creation
    for i in range(obj.dic[nomm].__len__()):
        if catg.lower() == obj.dic[nomm][i].categorie.lower():
            print("\n-------->",obj.dic[nomm][i].nom)

def fonction4(nomm):                  #     fonction qui affiche les sites qui proposent une visite guidée
    obj = creation
    for i in range(obj.dic[nomm].__len__()):
        if "guidee" in obj.dic[nomm][i].__dict__ and obj.dic[nomm][i].guidee.lower() == "oui":
            print("\n-------->",obj.dic[nomm][i].nom)

def fonction5(nomm,sites,x):          #     fonction qui calcule la distance d’itinéraires

    ####### Dictionnaire pour les indices de chaque site pour la zone "Rabat-salé" ######

    dict1 = {"tour hassan":0, "oudaya":1, "chellah":2, "Le Musée Mohammed VI":3, "Musée Belghazi":4, "Musée Maroc Télécom":5,
            "Village de poterie Oulja":6, "Ancienne Médina Rabat":7, "Oued Bouregreg":8, "Jardin exotique":9}

    ####### Dictionnaire pour les indices de chaque site pour la zone "Marrakech" ######

    dict2 = {"Djemaa El Fna": 0, "Medersa Ben Youssef": 1, "Koutoubia Mosque": 2, "Le musée Dar Si Said": 3, "Musée Yves Saint Laurent": 4,"Musée d'Art et de Culture de Marrakech": 5,
            "Medina Souks": 6, "Le souk des tanneurs": 7, "Ourika": 8, "Terres d'amanar": 9}

    if x!= len(sites):
        print("  le nombre que vous avaez entré est different de celui des sites  :'( ")
    else:
        obj=creation
        distance = list() #     liste pour stocker la matrice de distances
        d = dict()        #     dictionnaire pour des sites d'un zone
        #### choisir la zone ####
        if  nomm == "Rabat-salé" :
            d=dict1
            distance = copy.deepcopy(obj.distancez1)
        else:
            d=dict2
            distance = copy.deepcopy(obj.distancez2)

        indice = list()   #      les indices de la  matrice des distance
        for i in sites :
            if i not in d.keys() :
                print("Certains site que vous avez entrer n'existe pas :'( ") #      si un site n'existe pas
                break
            indice.append(d[i]) #        si oui , ajouter les indice à partir de dictionnaire ci-dessus
        s=0
        for i in range(len(indice)-1):
            s=s+int(distance[indice[i]][indice[i+1]])
        print("la distance :",s ,"Km")

