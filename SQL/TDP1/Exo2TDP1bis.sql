-- 1. ⋆ ´Ecrire une requˆete pour afficher les r´eservations qui se terminent apr`es 24h.

select * from RESERVER where hh_debut + duree > 24;

-- 2. ⋆⋆ ´Ecrire une requˆete pour afficher les r´eservations dont le nombre de personnes
-- d´epasse la capacit´e de la salle r´eserv´ee.

select * from SALLE natural join RESERVER where capacite < nbpers;

-- 3. ⋆⋆ ´Ecrire une requˆete pour afficher les r´eservations dont le type de l’occupant n’est
-- pas compatible avec les types disponibles pour la salle r´eserv´ee.

select * from RESERVER natural join OCCUPANT natural join SALLE S1
where OCCUPANT.idt not in (select idt from ETRE_DISPONIBLE_POUR natural join SALLE S2 where S1.ids = S2.ids);

-- 4. ⋆⋆ ´Ecrire une requˆete pour afficher les couples de r´eservations diff´erentes qui se che-
-- vauchent.

select * from RESERVER r1, RESERVER r2 where r1.ids = r2.ids and r1.idO != r2.idO and r1.jma= r2.jma and r1.hh_debut<R2.hh_debut and (R1.hh_debut+R1.duree)>R2.hh_debut;