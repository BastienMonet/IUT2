class Personne:
    def __init__(self, nom, naissance, mort, epoux, enfants):
        self.nom = nom
        self.naissance = naissance # la date de naissance
        self.mort = mort # la date de mort, None pour les vivants!
        self.epoux = epoux # la liste de ses époux successifs
        self.enfant = enfants # la liste de ses enfants,
        # triée par âge décroissant
    def est_vivant(self):
        return (self.mort == None)

    
    def ajoute_enfant(self, nouvel_enfant):
        return self.lesenfants.append(nouvel_enfant)
    
    def etait_vivant(self, date):
        return date > self.naissance and (date < self.mort or self.mort is None)
    

def mystere(personne):
    """
    Renvoie un ensemble de de noms de personne qui sont vivant
    """
    vivants = set()
    if personne.est_vivant():
        vivants.add(personne.nom)
    for e in personne.enfants():
        vivants = vivants | mystere(e)
    return vivants
    
def plus_jeune_dans_la_famille(personne):
    plus_jeune = personne
    for e in personne.enfants:
        minot = plus_jeune_dans_la_famille(e)
        if minot.naissance > plus_jeune.naissance:
            plus_jeune = minot
        return plus_jeune
    

def heritier(personne, date):
    if not personne.etait_vivant(date):
        for enfant in personne.enfant:
            fam = heritier(enfant, date)
            if fam != None:
                return fam
        return None
    else:
        return personne.nom



# def heritier(Cesar , 1850) -> Cesar
# def heritier(Cesar , 1939) -> Elise
# def heritier(Cesar , 1990) -> None
# def heritier(Cesar , 1938) -> Hildegate