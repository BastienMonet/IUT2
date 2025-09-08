-- -- 1. Le type d’une salle doit ˆetre dans la table TYPE.
pourquoi?

insert into ETRE_DISPONIBLE_POUR values
(1, 6);

-- ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`DBmonet`.`ETRE_DISPONIBLE_POUR`, CONSTRAINT `ETRE_DISPONIBLE_POUR_ibfk_1` FOREIGN KEY (`idt`) REFERENCES `TYPE` (`idt`))



-- -- 2. Le type d’un occupant doit ˆetre dans la table TYPE.
insert into OCCUPANT values
(9, 'Alice', 'Etudiant', 6);

-- ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`DBmonet`.`OCCUPANT`, CONSTRAINT `OCCUPANT_ibfk_1` FOREIGN KEY (`idt`) REFERENCES `TYPE` (`idt`))


-- -- 3. Tous les types doivent avoir un nom distinct.
insert into TYPE values (6, 'Association');

-- aucune contrainte n'est violée car le nom 'Association' n'est pas une clé unique

-- solution, mettre NomType comme clé primaire ou mettre un UNIQUE a nomType


-- -- 4. Il n’y a pas deux salles avec le mˆeme nom.
insert into SALLE values (2, 'Salle des fêtes', 30);

-- aucune contrainte n'est violée car nomSalle n'est pas une clé unique

-- solution, mettre nomSalle comme clé primaire ou mettre nomSalle en UNIQUE


-- -- 5. Une r´eservation doit ˆetre faite par un occupant pr´esent dans la base de donn´ees.

insert into RESERVER(jma, ido, hh_debut, ids, duree, nbpers) values ('2022-05-08', 3, 7, 53, 2, 1);

-- ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`DBmonet`.`RESERVER`, CONSTRAINT `RESERVER_ibfk_1` FOREIGN KEY (`ids`) REFERENCES `SALLE` (`ids`))



-- -- 6. Seule une salle pr´esente dans la base de donn´ees peut ˆetre r´eserv´ee.


insert into RESERVER(jma, ido, hh_debut, ids, duree, nbpers) values ('2023-05-08', 3, 7, 1, 2, 1);

-- aucune contrainte n'est violée car la salle 1 est présente dans la base de données


-- -- 7. L’heure de fin d’une r´eservation doit ˆetre inf´erieure ou ´egale `a 24.


insert into RESERVER(jma, ido, hh_debut, ids, duree, nbpers) values ('2023-05-08', 3, 7, 1, 25, 1);

-- ERROR 4025 (23000): CONSTRAINT `RESERVER.duree` failed for `DBmonet`.`RESERVER



-- -- 8. Le type de l’occupant qui fait une r´eservation doit correspondre `a un type disponible
-- pour la salle r´eserv´ee.

insert into OCCUPANT(ido, nom, carac, idt) values (426, 'Charlie', 'Chercheur', 7);

-- ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`DBmonet`.`OCCUPANT`, CONSTRAINT `OCCUPANT_ibfk_1` FOREIGN KEY (`idt`) REFERENCES `TYPE` (`idt`))

-- -- 9. Une r´eservation doit toujours commencer `a une heure enti`ere.

insert into RESERVER(jma, ido, hh_debut, ids, duree, nbpers) values ('2025-05-08', 3, 9.1, 1, 2, 1);

-- apparement MySQL accepte les float pour les INT (mais un int est bien entré dans la bd), il n'y a pas de contrainte violée


-- -- 10. Le nombre de personnes d’une r´eservation doit ˆetre renseign´e.

insert into RESERVER(jma, ido, hh_debut, ids, duree, nbpers) values ('2125-05-08', 3, 9, 1, 2, null);

-- aucune contrainte n'est violée car nbpers n'est pas défini comme NOT NULL


-- -- 11. Le nombre de personnes d’une r´eservation ne doit pas d´epasser la capacit´e de la salle
-- r´eserv´ee.

insert into RESERVER(jma, ido, hh_debut, ids, duree, nbpers) values ('2225-05-08', 3, 9, 1, 2, 200);

-- aucune contrainte n'est violée car il n'y a pas de contrainte entre nbpers et la capacité de la salle

-- solution : trigger car les contraintes check ne s'appliquent pas si on a a faire a une contraite entre deux tables



-- -- 12. Deux r´eservations distinctes ne peuvent pas se chevaucher.

insert into RESERVER(jma, ido, hh_debut, ids, duree, nbpers) values ('2225-05-08', 1, 10, 1, 2, 1);

-- non, il faut un trigger pour cela