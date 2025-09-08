
-- (a) Afficher l’ensemble des occupants avec leur type.
select nomO, typeO 
from Occupant;

-- (b) Afficher toutes les salles qui ont le type ”Association”.
select * 
from Salle natural join Accueillir 
where typeO = 'Association';

-- (c) Afficher les occupants qui ont r´eserv´e la salle des fˆetes ou la salle info.
select * 
from Occupant 
where idO in (select idO from Reserver where nomSalle = 'Salle des fêtes')
or idO in (select idO from Reserver where nomSalle = 'Salle info');

-- (d) Afficher les occupants qui ont r´eserv´e la salle des fˆetes et la salle info.
select * 
from Occupant 
where idO in (select idO from Reserver where nomSalle = 'Salle des fêtes')
and idO in (select idO from Reserver where nomSalle = 'Salle info');

-- (e) Afficher les occupants qui ont r´eserv´e la salle des fˆetes mais pas la salle info.
select * 
from Occupant 
where idO in (select idO from Reserver where nomSalle = 'Salle des fêtes')
and idO not in (select idO from Reserver where nomSalle = 'Salle info');

-- (f) Afficher la salle qui a la plus grande capacit´e.
select *
from Salle
where capacite = (select max(capacite) from Salle);

-- (g) Afficher la dur´ee totale r´eserv´ee pour chaque salle par mois.
select nomSalle, monthname(dateDebut), sum(duree)
from Reserver
group by nomSalle, monthname(dateDebut);

-- (h) Afficher les occupants qui ont d´ej`a r´eserv´e toutes les salles au moins une fois.
select idO, nomO
from Reserver natural join Occupant
group by idO
having count(distinct nomSalle) = (select count(nomSalle) from Salle);


-- V2

select * from OCCUPANT
where not exists 
(select ids from SALLE EXCEPT select ids from RESERVER where ido = OCCUPANT.ido);