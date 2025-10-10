class Article:
    def __init__(self, ref, libelle, prix):
        self.ref=ref
        self.libelle=libelle
        self.prix=prix
    
    def __repr__(self):
        return str(self.ref) + " " + str(self.libelle) + " " + str(self.prix)
    
    
    