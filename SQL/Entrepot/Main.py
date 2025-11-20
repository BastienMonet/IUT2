from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from Base import Base
from Article import Article, testArticle, afficheArticle
from Entrepot import Entrepot, testEntrepot, afficheEntrepot
from Stocker import Stocker, testStocker, afficheStocker, afficheQteArtParEnt

if __name__ == '__main__':
    engine = create_engine('sqlite:///entrepot.db', echo=False)
    session = Session(engine)
    
    print('--- Suppression des tables existantes ---')
    Base.metadata.drop_all(bind=engine)
    
    print('--- Création des tables ---')
    Base.metadata.create_all(engine)
    
    testArticle(session)
    afficheArticle(session)
    testEntrepot(session)
    afficheEntrepot(session)
    testStocker(session)
    afficheStocker(session)
    afficheQteArtParEnt(session, 1)
