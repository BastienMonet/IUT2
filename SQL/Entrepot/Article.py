from sqlalchemy import Column, Integer, Float, Text
from sqlalchemy.orm import relationship, Session
from Base import Base

class Article(Base):
    __tablename__ = 'ARTICLE'
        
    reference = Column(Integer, primary_key=True)
    libelle = Column(Text)
    prix = Column(Float)
    stockArt = relationship("Stocker", back_populates="larticle")
    
    def __init__(self, ref, lib, pr):
        self.reference = ref
        self.libelle = lib
        self.prix = pr
            
    def __str__(self):
        return f'Article référence : {self.reference} {self.libelle} au prix de {self.prix}'

def testArticle(session: Session):
    a1 = Article(1, 'Chaise', 49)
    a2 = Article(2, 'Table', 110)
    a3 = Article(123, 'tuile17x27', 2.55)
    session.add_all([a1, a2, a3])
    session.commit()

def afficheArticle(session: Session):
    for a in session.query(Article):
        print(a)
