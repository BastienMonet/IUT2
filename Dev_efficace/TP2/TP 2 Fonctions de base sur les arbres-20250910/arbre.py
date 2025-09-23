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
    
    def hauteur(self, hauteur):
        maxi = hauteur
        curr = 0
        for enfant in self.enfants():
            curr = enfant.hauteur(hauteur + 1)
            maxi = max(maxi,curr)
        return maxi
    
    def hauteur2(self):
        if not self.enfants():
            return 0
        else:
            h = 0
            for e in self.enfants():
                h = max(h, e.hauteur2())
            return h + 1
    
    def deg(self):
        maxi = len(self.enfants())
        curr = 0
        for enfant in self.enfants():
            curr = enfant.deg()
            maxi = max(maxi,curr)
        return maxi
        

    def max_etiquette(self):
        maxi = self.etiquette()
        for e in self.enfants():
            maxi = max(maxi, e.max_etiquette())
        return maxi
    
    def a_deux_enfants(self):
        return len(self.enfants()) == 2
    
    def plus(self):
        return self.enfants()[0] + self.enfants()[1]
    
    def fois(self):
        return self.enfants()[0] * self.enfants()[1]
    
    def entier(self):
        return self.etiquette()
    
    def pas_enfant(self):
        return len(self.enfants()) == 0
    
    def est_arithmetique(self):
        if self.pas_enfant() and isinstance(self.etiquette(), int):
            return True
        elif self.etiquette() == "+" or self.etiquette() == "*" and self.a_deux_enfants():
            total = True
            for e in self.enfants():
                total = total and e.est_arithmetique() 
            return total
        else:
            return False
        
    def est_arithmetique_mieux(self):
        if self.pas_enfant() and type(self.etiquette()) == int:
            return True
        else:
            return (self.etiquette() == "+" or self.etiquette() == "*") \
                    and self.a_deux_enfants() and self.enfants()[0].est_arithmetique_mieux() \
                    and self.enfants()[1].est_arithmetique_mieux()
        
    def arithmetique(self):
        if self.pas_enfant() and isinstance(self.etiquette(), int):
            return self.entier()
        elif self.etiquette() == "+" and self.a_deux_enfants():
            total = 0
            for e in self.enfants():
                total += e.arithmetique() 
            return total
        elif self.etiquette() == "*" and self.a_deux_enfants():
            total = 1
            for e in self.enfants():
                total *= e.arithmetique() 
            return total
        else:
            return -1
        
    def arithmetique_mieux(self):
        # on considere que l'arbre est correctement former
        try:
            if isinstance(self.etiquette(), int):
                return self.entier()
            elif self.etiquette() == "+":
                return self.enfants()[0].arithmetique_mieux() + self.enfants()[1].arithmetique_mieux()
            elif self.etiquette() == "*":
                return self.enfants()[0].arithmetique_mieux() * self.enfants()[1].arithmetique_mieux()
        except:
            return 0
            

        


if __name__ == "__main__":
    # a1 = Arbre.Feuille(1)
    # a2 = Arbre.Feuille(2)
    # a3 = Arbre.Feuille(3)
    # a4 = Arbre.Feuille(4)
    # a5 = Arbre.Feuille(5)
    # a6 = Arbre.Feuille(6)
    # a1.add(a2)
    # a1.add(a3)
    # a2.add(a4)
    # a4.add(a5)
    # a5.add(a6)
    # print(a1)
    # print(a1.nbre_noeud())
    # print(a1.nbre_ni())
    # print(a1.deg())
    # print(a1.hauteur(0))
    # print(a1.hauteur2())
    # print(a1.max_etiquette())



    un = Arbre.Feuille(1)
    trois = Arbre.Feuille(3)
    quatre = Arbre.Feuille(4)
    fois = Arbre("*", [trois, quatre])
    plus = Arbre("+", [un, fois])

    print(plus)
    print(plus.est_arithmetique())
    print(plus.est_arithmetique_mieux())
    print(plus.arithmetique())
    print(plus.arithmetique_mieux())
