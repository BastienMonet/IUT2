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





    