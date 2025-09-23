
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




# Question 2
def sousArbreChemin(arbre, chemin):
    if chemin == []:
        return arbre
    else:
        return sousArbreChemin(arbre.enfants()[chemin[0]], chemin[1:])
        

# Question 3
def chemin_a_etiquette_0(arbre, n):
    if arbre.etiquette() == n:
        return []
    else:
        for i in range(len(arbre.enfants())):
            chemin = chemin_a_etiquette_0(arbre.enfants()[i], n)
            if chemin is not None:
                return [i]+chemin
        return None




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

print(chemin_a_etiquette_0(a1, 2))