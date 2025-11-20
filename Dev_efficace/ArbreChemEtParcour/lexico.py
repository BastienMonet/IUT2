class Lexico:
    def __init__(self, enfants, fin):
        self.enfants = enfants 
        self.fin = fin

    def contient(self, mot):
        if mot == '':
            return self.fin
        if mot[0] not in self.enfants:
            return False
        e = self.enfants[mot[0]]
        return e.contient(mot[1:])

    def __repr__(self): #pour l'affichage
        return "(%r)\n" % (self.enfants)


    @classmethod
    def singelton(cls, mot):
        res = Lexico({}, False)
        noeud_courant = res
        for lettre in mot:
            e = Lexico({}, False)
            noeud_courant.enfants[lettre] = e
            noeud_courant = e
        noeud_courant.fin = True
        return res
    
    def ajout(self, mot):
        if len(mot) == 0:
            self.fin = True
        elif mot[0] not in self.enfants:
            self.enfants[mot[0]] = Lexico.singelton(mot[1:])
        else:
            self.enfants[mot[0]].ajout(mot[1:])



a1 = Lexico({}, False)
a1.ajout("an")
a1.ajout("ass")
print(a1)
    