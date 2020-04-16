from data.Monument_historique import *
from data.Naturel import *
from data.Musee import *
from data.Production import *
from data.ZoneTouristique import *
import csv
import os

class creation:
    dic = dict()
    #     la liste de tous les sites touristiques de la zone1 "Rabat-Salé"
    site1 = monHistorique("Tour Hassan", "Découvrir l’histoire et le patrimoine de la ville de Rabat", "Histoire")
    site2 = monHistorique("Oudaya", "Découvrir l’histoire et le patrimoine de la ville de Rabat", "Histoire")
    site3 = monHistorique("Chellah", "Découvrir l’histoire et le patrimoine de la ville de Rabat", "Histoire")
    site4 = musee("Le Musée Mohammed VI", "Rabat centre-ville","Découvrir des œuvres artistiques modernes marocains et étrangers", "Art moderne ","Oui", "20 DH")
    site5 = musee("Musée Belghazi", "Sidi Bouknadel Salé", "Découvrir la culture marocaine traditionnelle","Ethnographie", "Oui", "50 DH")
    site6 = musee("Musée Maroc Télécom", "Hay Riad,Rabat", "Avoir une idée sur l’évolution des Télécoms au Maroc","Télécommunications", "Non", "0 DH")
    site7 = production("Village de poterie Oulja", "Oulja, Salé"," Découvrir et acheter des produits de poterie marocains", "Artisanat", "Non")
    site8 = production("Ancienne Médina Rabat", "Rabat ville", " Acheter des produits d’artisanat", "Artisanat","non")
    site9 = naturel("Oued Bouregreg", "Entre Rabat et Salé", "Faire une balade fluviale en « Flouka »")
    site10 = naturel("Jardin exotique", "Sidi Bouknadel, Salé",
                     "Faire une balade dans un jardin qui abrite des plantes des cinq coins du monde.")
    list1 = (site1, site2, site3, site4, site5, site6, site7, site8, site9, site10)

    #     la liste de tous les sites touristiques de la zone2 "Marrakech"
    sitea = monHistorique("Djemaa El Fna", "Découvrir l’histoire et le patrimoine de la ville de Marrakech", "Histoire")
    siteb = monHistorique("Medersa Ben Youssef", "Découvrir l’histoire et le patrimoine de la ville de Marrakech",
                          "Histoire")
    sitec = monHistorique("Koutoubia Mosque", "Découvrir l’histoire et le patrimoine de la ville de Marakech",
                          "Histoire")
    sited = musee("Le musée Dar Si Said", "Riad Zitoun el-Jedid",
                  "Découvrir l'artisanat marocain du bois au travers des boiseries, céramiques,bijoux...", "Artisanat",
                  "non", "0 DH")
    sitee = musee("Musée Yves Saint Laurent ", "Yves Saint Laurent,Marrakech",
                  "Découvrir Des créations tirées des collections du couturier ", "Art moderne", "Oui", "150 DH")
    sitef = musee("Musée d'Art et de Culture de Marrakech", " Rue de Yougoslavie Passage Ghandour,Marrakech",
                  "propose de nombreuses expositions d'artistes locaux et internationaux", "Art moderne", "Oui",
                  "50 DH")
    sitej = production("Medina Souks", "Rue Bab Debbagh", "Acheter des produits d’artisanat", "Artisanat", "Non")
    siteh = production("Le souk des tanneurs", " Medina de Marrakech", " Acheter des articles en cuir en tous genres",
                       "Artisanat", "Oui")
    sitei = naturel("Ourika", "En dehors de Marrakech", "Faire une balade dans setti-fatma")
    siteg = naturel("Terres d'amanar", "Douar Akli , Marrakec",
                    " découvrir la culture berbère et pratiquer des activités sportives, « nature »,")
    list2 = (sitea, siteb, sitec, sited, sitee, sitef, sitej, siteh, sitei, siteg)

    zonz1=zone("Rabat-salé","Rabat-salé")
    zone2=zone("Marrakech","Marrakech")
    zoneliste = (zonz1,zone2)  #     liste des zones


    dic["Rabat-salé"] = list1
    dic["Marrakech"] = list2

    distancez1 = list() #    pour stoquer la matrice de distances pour zone1 "Rabat-salé"
    distancez2 = list() #    pour stoquer la matrice de distances pour zone2 "Marrakech"

    #    creer path des fichiers matrice.csv
    path = str(os.path.realpath(__file__))
    path1 =path[0:len(path)-12]+"\matriceZ1.csv"
    path2 =path[0:len(path)-12]+"\matriceZ2.csv"


    with open(path1, "r+") as f:
        red = csv.reader(f, delimiter='\t')
        for i in red:
            distancez1.append(i)

    with open( path2,"r+") as f2:
        red = csv.reader(f2, delimiter='\t')
        for i in red:
            distancez2.append(i)
