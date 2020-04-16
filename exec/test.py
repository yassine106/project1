
#list=["tour hassan","oudaya","chellah","e Musée Mohammed VI","Musée Belghazi","Musée Maroc Télécom","Village de poterie Oulja","Ancienne Médina Rabat","Oued Bouregreg","Jardin exotique"]
import csv
list = list()
with open("matriceZ1.csv","r+") as f:
    red = csv.reader(f,delimiter='\t')
    for i in red :
        list.append(i)

print(list)