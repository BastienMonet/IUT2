from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from Base import Base
from Article import Article

class Stocker(Base):
    __tablename__ = 'STOCKER'
        
    reference = Column(Integer, ForeignKey("ARTICLE.reference"), primary_key=True)
    code = Column(Integer, ForeignKey("ENTREPOT.code"), primary_key=True)
    quantite = Column(Integer)
    larticle = relationship("Article", back_populates="stockArt")
    lentrepot = relationship("Entrepot", back_populates="stockEnt")
    
    def __init__(self, art, ent, qte):
        self.reference = art
        self.code = ent
        self.quantite = qte

    def getArtLibelle(self):
        return self.larticle.libelle	
                
    def __str__(self):
        return f'article ref : {self.reference} {self.getArtLibelle()} stocké dans entrepôt {self.code} quantité {self.quantite}'

def testStocker(session):
    s1 = Stocker(1, 1, 45) 
    s2 = Stocker(1, 2, 55)
    s3 = Stocker(1, 3, 25)
    s4 = Stocker(2, 1, 10)
    s5 = Stocker(123, 2, 2000)
    s6 = Stocker(123, 3, 1250)
    session.add_all([s1, s2, s3, s4, s5, s6])
    session.commit()

def afficheStocker(session):
    for e in session.query(Stocker):
        print(e)

def afficheQteArtParEnt(session, ref):
    art = session.get(Article, ref)
    print("Voici où se trouve l'article :", art)
    total = 0
    for st in art.stockArt:
        print(f"---- dans {st.lentrepot} en quantité : {st.quantite}")
        total += st.quantite
    print("-- quantité totale disponible :", total)
