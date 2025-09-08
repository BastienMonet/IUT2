-- 1. ⋆ ´Ecrire une requˆete pour afficher les r´eservations qui se terminent apr`es 24h.

select * from RESERVER where hh_debut + duree > 24;

-- 2. ⋆⋆ ´Ecrire une requˆete pour afficher les r´eservations dont le nombre de personnes
-- d´epasse la capacit´e de la salle r´eserv´ee.

select * from SALLE natural join RESERVER where capacite < nbpers;

-- 3. ⋆⋆ ´Ecrire une requˆete pour afficher les r´eservations dont le type de l’occupant n’est
-- pas compatible avec les types disponibles pour la salle r´eserv´ee.

select * from RESERVER r where NOT EXISTS (select * from OCCUPANT natural join ETRE_DISPONIBLE_POUR where idO = r.idO and ids = r.ids);

-- 4. ⋆⋆ ´Ecrire une requˆete pour afficher les couples de r´eservations diff´erentes qui se che-
-- vauchent.

select distinct * from RESERVER r1, RESERVER r2 where r1.jma = r2.jma and r1.idO != r2.idO and (r1.hh_debut + r1.duree > r2.hh_debut and r1.hh_debut + r1.duree < r2.hh_debut + r2.duree);