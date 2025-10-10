CREATE TABLE ENTREPOT (
  code INT(9),
  nom VARCHAR(42),
  departement VARCHAR(42)
) ;

insert into ENTREPOT values(1, 'Orléans-nord', 'Loiret'), 
                           (2, 'Orléans-sud', 'Loiret'), 
                           (3, 'Bourges', 'Cher'),
                           (4, 'Centre', 'Cher'),
                           (5, 'Aubigny', 'Cher'),
                           (6, 'Saint-Amand', 'Cher'),
                           (7, 'Vierzon', 'Cher'),
                           (8, 'La-Ferté', 'Loiret'),
                           (9, 'Centre', 'Loir-et-Cher'),
                           (10, 'Blois', 'Loir-et-Cher'),
                           (11, 'Salbris', 'Loir-et-Cher'),
                           (12, 'Vendôme', 'Loir-et-Cher'),
                           (13, 'Saran', 'Loiret'),
                           (14, 'Lamotte-Beuvron', 'Loir-et-Cher'),
                           (15, 'Sancerre', 'Cher');


create index indcode on ENTREPOT( code ) ;


create index departement on ENTREPOT(nom, departement ) ;