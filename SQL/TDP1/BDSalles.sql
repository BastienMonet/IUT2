-- CREATE DATABASE IF NOT EXISTS SALLES DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
-- USE `SALLES`;

-- suppression des tables de la BD salle

drop table RESERVER;
drop table ETRE_DISPONIBLE_POUR;
drop table OCCUPANT;
drop table SALLE;
drop table TYPE;

-- creation des tables de la BD salle

CREATE TABLE OCCUPANT (
  ido INT(8),
  nom VARCHAR(42),
  carac VARCHAR(42),
  idt INT(8),
  PRIMARY KEY (ido)
) ;

CREATE TABLE TYPE (
  idt INT(8),
  nomtype VARCHAR(42),
  PRIMARY KEY (idt)
) ;

CREATE TABLE RESERVER (
  jma DATE,
  ido INT(8),
  hh_debut INT(2),
  ids INT(8),
  duree INT(2) check (duree between 1 and 24),
  nbpers INT(4),
  PRIMARY KEY (jma, hh_debut, ids)
) ;

CREATE TABLE ETRE_DISPONIBLE_POUR (
  ids INT(8),
  idt INT(8),
  PRIMARY KEY (ids, idt)
) ;

CREATE TABLE SALLE (
  ids INT(8),
  nomsalle VARCHAR(42),
  capacite INT(4),
  PRIMARY KEY (ids)
) ;

-- creation des clés etrangères de la BD salle

ALTER TABLE OCCUPANT ADD FOREIGN KEY (idt) REFERENCES TYPE (idt);
ALTER TABLE RESERVER ADD FOREIGN KEY (ids) REFERENCES SALLE (ids);
ALTER TABLE RESERVER ADD FOREIGN KEY (ido) REFERENCES OCCUPANT (ido);
ALTER TABLE ETRE_DISPONIBLE_POUR ADD FOREIGN KEY (idt) REFERENCES TYPE (idt);
ALTER TABLE ETRE_DISPONIBLE_POUR ADD FOREIGN KEY (ids) REFERENCES SALLE (ids);


-- insertion de valeur dans les tables de la BD salle

insert into TYPE values (1, 'Mairie'),
                        (2, 'Ecole'),
                        (3, 'Association'),
                        (4, 'Entretien'),
                        (5, 'Particulier');
                        
insert into SALLE values (1, 'Salle des fetes', 150),
                         (2, 'Salle info', 15),
                         (3, 'Salle des ecureuils', 35),
                         (4, 'Salle du conseil', 40);

insert into ETRE_DISPONIBLE_POUR values (1, 1),
                                        (1, 2),
                                        (1, 3),
                                        (1, 4),
                                        (1, 5),
                                        (2, 1),
                                        (2, 2),
                                        (2, 3),
                                        (2, 4),
                                        (3, 1),
                                        (3, 2),
                                        (3, 3),
                                        (3, 4),
                                        (3, 5),
                                        (4, 1),
                                        (4, 4) ;
                                        
insert into OCCUPANT values (1, 'Conseil municipal', NULL, 1),
                            (2, 'Accueil periscolaire', NULL, 1),
                            (3, 'ToutNet', 'contrat 22/23', 4),
                            (11, 'Classe1', 'Petite moyenne section', 2),
                            (12, 'Classe2', 'Grande section, CP', 2),
                            (13, 'Classe3', 'CE1 CE2', 2),
                            (14, 'Classe3', 'CM1, CM2', 2),
                            (21, 'Ping pong', NULL, 3),
                            (22, 'Yoga', NULL, 3),
                            (23, 'Theatre', NULL, 3),
                            (24, 'Club info', 'Initiation', 3),
                            (25, 'Tennis', 'Initiation', 3),
                            (26, 'Volley', 'Initiation', 3),
                            (51, 'Mariage', 'Dupond/Dubois', 5),
                            (52, 'Mariage', 'Dupond/Dubois', 1) ;

insert into RESERVER(jma, ido, hh_debut, ids, duree, nbpers) values ('2022-05-9', 3, 7, 1, 2, 1),
                                                                    ('2022-05-9', 13, 10, 1, 2, 25),
                                                                    ('2022-05-9', 12, 13, 1, 3, 22),
                                                                    ('2022-05-9', 21, 19, 1, 2, 20),
                                                                    ('2022-05-9', 1, 20, 4, 3, 20),
                                                                    ('2022-05-9', 2, 7, 4, 2, 15),
                                                                    ('2022-05-9', 12, 14, 4, 2, 20),
                                                                    ('2022-05-9', 3, 18, 4, 2, 1),
                                                                    ('2022-05-10', 3, 7, 2, 2, 1),
                                                                    ('2022-05-10', 24, 9, 2, 3, 8),
                                                                    ('2022-05-10', 2, 7, 4, 2, 15),
                                                                    ('2022-05-10', 22, 19, 1, 2, 30),
                                                                    ('2022-05-11', 2, 7, 4, 12, 15),
                                                                    ('2022-05-11', 25, 19, 1, 3, 15),
                                                                    ('2022-05-12', 11, 14, 1, 2, 18),
                                                                    ('2022-05-12', 26, 19, 1, 3, 30),
                                                                    ('2022-05-12', 13, 14, 2, 2, 25),
                                                                    ('2022-05-12', 3, 7, 3, 2, 1),
                                                                    ('2022-05-12', 2, 7, 4, 2, 15),
                                                                    ('2022-05-13', 12, 13, 1, 3, 22),
                                                                    ('2022-05-13', 13, 10, 2, 2, 25),
                                                                    ('2022-05-13', 2, 7, 4, 2, 15),
                                                                    ('2022-05-13', 23, 20, 4, 4, 10),
                                                                    ('2022-05-14', 51, 0, 1, 24, 120),
                                                                    ('2022-05-14', 52, 14, 4, 2, 30),
                                                                    ('2022-05-15', 51, 0, 1, 24, 120);
                                                                    
