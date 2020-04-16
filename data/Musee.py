from data.Monument_historique import *
class musee(monHistorique) :
    def __init__(self,nom,lieu,interet,theme,guidee,tarif):
            monHistorique.__init__(self,nom,interet,theme)
            self.lieu=lieu
            self.guidee=guidee
            self.tarif=tarif
            self.categorie="Musée"