from data.Monument_historique import *
class production(monHistorique):
    def __init__(self,nom,lieu,interet,theme,guidee):
        monHistorique.__init__(self,nom,interet,theme)
        self.lieu=lieu
        self.guidee=guidee
        self.categorie="Site de production"
