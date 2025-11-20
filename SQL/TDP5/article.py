from sqlalchemy import *
from exempleORMAlchemy import Base, relationship

class Article2:
    def __init__(self, ref, libelle, prix):
        self.ref=ref
        self.libelle=libelle
        self.prix=prix
    
    def __repr__(self):
        return str(self.ref) + " " + str(self.libelle) + " " + str(self.prix)
    
    
class Entrepot(Base):
    __tablename__ = 'ENTREPOT'

    code = Column(Integer, primary_key=True)
    nom = Column(Text)
    departement = Column(Text)
    codeE = relationship("Stocker", back_populates="codeS")

    def __repr__(self):
        return str(self.code) + " " + str(self.nom) + " " + str(self.departement)
    


class Article(Base):
    __tablename__ = 'ARTICLE'

    reference = Column(Integer, primary_key=True)
    libelle = Column(Text)
    prix = Column(Float)
    referenceA = relationship("Stocker", back_populates="referenceS")

    def __init__ (self, reference, libelle, prix):
        self.reference = reference
        self.libelle = libelle
        self.prix = prix

    def __repr__(self):
        return str(self.reference) + " " + str(self.libelle) + " " + str(self.prix)
    

class Stocker(Base):
    __tablename__ = 'STOCKER'

    code = Column(Integer, ForeignKey('ENTREPOT.code'), primary_key=True)
    reference = Column(Integer, ForeignKey('ARTICLE.reference'), primary_key=True)
    quantite = Column(Integer)
    codeS = relationship("Entrepot", back_populates="codeE")
    referenceS = relationship("Article", back_populates="referenceA")


    def __repr__(self):
        return str(self.code) + " " + str(self.reference) + " " + str(self.quantite)
