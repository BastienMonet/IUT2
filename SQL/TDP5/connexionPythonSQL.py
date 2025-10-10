import sqlalchemy  
from sqlalchemy import text
from article import Article
# pour avoir sqlalchemy :
# sudo apt-get update 
# sudo apt-get install python3-sqlalchemy
# pip3 install mysql-connector-python

import getpass  # pour faire la lecture cachée d'un mot de passe

def ouvrir_connexion(user,passwd,host,database):
    """
    ouverture d'une connexion MySQL
    paramètres:
       user     (str) le login MySQL de l'utilsateur
       passwd   (str) le mot de passe MySQL de l'utilisateur
       host     (str) le nom ou l'adresse IP de la machine hébergeant le serveur MySQL
       database (str) le nom de la base de données à utiliser
    résultat: l'objet qui gère le connection MySQL si tout s'est bien passé
    """
    try:
        #creation de l'objet gérant les interactions avec le serveur de BD
        engine=sqlalchemy.create_engine('mysql://'+user+':'+passwd+'@'+host+'/'+database)
        #creation de la connexion
        cnx = engine.connect()
    except Exception as err:
        print(err)
        raise err
    print("connexion réussie")
    return cnx


def maxref(co):
    res = co.execute(text("select max(reference) from ARTICLE"))
    (max,) = res.first()
    return max

def get_article(co, num):
    res = co.execute(text("select * from ARTICLE where reference = %d" % num))
    (ref, lib, prix) = res.first()
    return Article(ref, lib, prix)

def max_id_article(co):
    return get_article(maxref(co))

def list_article(co):
    res = []
    req = co.execute(text("Select * from ARTICLE"))
    for (ref, lib, prix) in req:
        res.append(Article(ref, lib, prix))
    return res

def entrepot_par_departement(co):
    res = ""
    cpt = 0
    prev = ""
    req = co.execute(text("select code, nom, departement from ENTREPOT order by departement"))
    for (code, nom, departement) in req:
        if departement != prev:
            if prev != "":
                res += "il y a " + str(cpt) + "entrepot dans ce departement\n"
            res += "les entrepots dans le departement :" + departement + "\n"
            cpt = 0
        res += "    " + str(code) + " " + nom +"\n"
        cpt += 1
        prev = departement
    if cpt != 0:
        res += "il y a " + str(cpt) + "entrepot dans ce departement\n"
    return res

def entrepot_possede_article(co, num):
    req = co.execute(text("select code, nom, quantite from ENTREPOT natural join STOCKER where reference = %d" % num))
    for (code, nom, quantite) in req:
        print(code, nom, quantite)

def valeur_entrepot(co, code):
    req = co.execute(text("select sum(quantite * prix) from STOCKER natural join ARTICLE where code = %d" % code))
    return req.first()

def exist_article(co, code):
    req = co.execute(text("select * from ARTICLE where reference = %d " % code ))
    return req.first()


if __name__ == "__main__":
    login="monet"
    passwd="monet"
    serveur="servinfo-maria"
    bd="DBmonet"
    cnx=ouvrir_connexion(login,passwd,serveur,bd)
    print(maxref(cnx))
    print(list_article(cnx))
    print(entrepot_possede_article(cnx, 1))
    # ici l'appel des procédures et fonctions
    cnx.close()
