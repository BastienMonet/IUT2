Drop table Reserver;
Drop table Accueillir; 
Drop table Occupant;
Drop table TypeO;
Drop table Salle;


Create table if not exists TypeO (
    typeO Varchar(20) primary key
);

Create table if not exists Salle (
    nomSalle Varchar(20) primary key,
    capacite INT
);

Create table if not exists Accueillir (
    typeO Varchar(20),
    nomSalle Varchar(20)
);

Create table if not exists Occupant (
    idO INT primary key,
    nomO Varchar(30),
    carac Varchar(50),
    typeO Varchar(20)
);

Create table if not exists Reserver (
    nomSalle Varchar(20),
    dateDebut date,
    heureDebut INT,
    duree INT check (duree <= 24),
    nbPersonnes INT,
    idO INT,
    primary key (nomSalle, dateDebut, heureDebut),
    constraint horaire check (heureDebut + duree <= 24)
);

alter table Reserver add foreign key (nomSalle) references Salle(nomSalle);
alter table Reserver add foreign key (idO) references Occupant(idO);


alter table Accueillir add foreign key (typeO) references TypeO(typeO);
alter table Accueillir add foreign key (nomSalle) references Salle(nomSalle);

alter table Occupant add foreign key (typeO) references TypeO(typeO);

insert into TypeO(typeO) values
('Association'),
('Piscine'),
('Football');

insert into Occupant(idO, nomO, carac, typeO) values
(1, 'Alice', 'Etudiant', 'Association'),
(2, 'Bob', 'Professeur', 'Piscine'),
(3, 'Charlie', 'Chercheur', 'Football');


insert into Salle(nomSalle, capacite) values
('Salle des fêtes', 30),
('Salle info', 50),
('SalleB', 20);

insert into Accueillir(typeO, nomSalle) values
('Association', 'Salle des fêtes'),
('Piscine', 'Salle info'),
('Football', 'SalleB'),
('Association', 'SalleB');

insert into Reserver(nomSalle, dateDebut, heureDebut, duree, nbPersonnes, idO) values
('Salle des fêtes', STR_TO_DATE("August 12 2017", "%M %d %Y"), 9, 2, 20, 1),
('Salle info', STR_TO_DATE("January 11 2017", "%M %d %Y"), 10, 3, 40, 2),
('Salle des fêtes', STR_TO_DATE("January 13 2017", "%M %d %Y"), 10, 3, 40, 2),
('SalleB', STR_TO_DATE("February 10 2017", "%M %d %Y"), 14, 1, 15, 2),
('SalleB', STR_TO_DATE("February 12 2017", "%M %d %Y"), 14, 1, 15, 2);
