from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship, Session
from Base import Base

class Entrepot(Base):
    __tablename__ = 'ENTREPOT'
        
    code = Column(Integer, primary_key=True)
    nom = Column(Text)
    departement = Column(Text)
    stockEnt = relationship("Stocker", back_populates="lentrepot")
    
    def __init__(self, cd, nm, de):
        self.code = cd
        self.nom = nm
        self.departement = de
            
    def __str__(self):
        return f'Entrepot code : {self.code} {self.nom} dans {self.departement}'

def testEntrepot(session: Session):
    e1 = Entrepot(1, 'Orléans nord', 'Loiret') 
    e2 = Entrepot(2, 'Orléans sud', 'Loiret')
    e3 = Entrepot(3, 'Bourges', 'Cher')
    session.add_all([e1, e2, e3])
    session.commit()

def afficheEntrepot(session: Session):
    for e in session.query(Entrepot):
        print(e)
