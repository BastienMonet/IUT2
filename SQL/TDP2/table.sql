-- CREATE DATABASE IF NOT EXISTS ENTREPOT DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
-- USE ENTREPOT;

drop table STOCKER;
drop table ARTICLE;
drop table ENTREPOT;
drop table HISTORIQUE;

CREATE TABLE ARTICLE (
  reference INT(9),
  libelle VARCHAR(42),
  prix DECIMAL(6,2),
  PRIMARY KEY (reference)
) ;

CREATE TABLE HISTORIQUE (
  idH INT AUTO_INCREMENT primary key,
  mess Varchar(200),
  dateMess Date
) ;

CREATE TABLE ENTREPOT (
  code INT(9),
  nom VARCHAR(42),
  departement VARCHAR(42),
  PRIMARY KEY (code)
) ;

CREATE TABLE STOCKER (
  reference INT(9),
  code INT(9),
  quantite INT(5),
  PRIMARY KEY (reference, code)
) ;

ALTER TABLE STOCKER ADD FOREIGN KEY (code) REFERENCES ENTREPOT (code);
ALTER TABLE STOCKER ADD FOREIGN KEY (reference) REFERENCES ARTICLE (reference);

insert into ARTICLE values(1, 'Chaise', 49),
                          (2, 'Table', 110), 
                          (123, 'tuile17x27', 2.55);
    
insert into ENTREPOT values(1, 'Orléans nord', 'Loiret'), 
                           (2, 'Orléans sud', 'Loiret'), 
                           (3, 'Orléans sud-nord', 'Loiret'), 
                           (4, 'Orléans nord-sud', 'Loiret'), 
                           (5, 'Bourges', 'Cher'),
                           (123, 'Tours', 'Indre et Loire');

insert into STOCKER values(1, 1, 45), 
                          (1, 2, 55),
                          (1, 3, 25),
                          (2, 1, 10);


