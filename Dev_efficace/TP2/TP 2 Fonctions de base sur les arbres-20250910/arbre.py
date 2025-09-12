#!/usr/bin/env python3

class Arbre:
    def __init__(self, etiquette, enfants):
        self.__etiquette = etiquette
        self.__enfants = enfants

    def etiquette(self):
        return self.__etiquette

    def enfants(self):
        return self.__enfants

    @classmethod
    def Feuille(cls_arbre, etiquette): #méthode statique
        return cls_arbre(etiquette, [])

    def add(self, nourisson):
        """
        ajoute un enfant à l'arbre
        """
        self.__enfants.append(nourisson)

    def __repr__(self):
        repr_enfants = ",".join(("%r" % e) for e in self.enfants())
        return "%r<%s>" % (self.etiquette(), repr_enfants)
    
    def nbre_feuille(self):
        total = 0
        if self.enfants() == []:
            return 1
        for enfant in self.enfants():
            total += enfant.nbre_feuille()
        return total
    
        
    def nbre_noeud(self):
        total = 1
        if self.enfants() == []:
            return 1
        for enfant in self.enfants():
            total += enfant.nbre_noeud()
        return total
    
    def nbre_ni(self):
        return self.nbre_noeud() - self.nbre_feuille() - 1
    
    def hauteur(self):
        maxi = 0
        curr = 0
        for enfant in self.enfants():
            curr = enfant.nbre_noeud()
            maxi = max(maxi,curr)
        return maxi
        
            
if __name__ == "__main__":
    a1 = Arbre.Feuille(1)
    a2 = Arbre.Feuille(2)
    a3 = Arbre.Feuille(3)
    a4 = Arbre.Feuille(4)
    a5 = Arbre.Feuille(5)
    a6 = Arbre.Feuille(6)
    a1.add(a2)
    a1.add(a3)
    a2.add(a4)
    a4.add(a5)
    a5.add(a6)
    print(a1)
    print(a1.nbre_noeud())
    print(a1.nbre_ni())
    print(a1.hauteur())

