

-- 1. Ecrire une requˆete param ́etr ́ee pour avoir la liste des articles valant moins d’une certaine
-- somme.

prepare articleValantMoins from 'select * from ARTICLE where
prix < ?';
set @prix=10;
execute articleValantMoins using @prix;


-- 2. Ecrire une requˆete param ́etr ́ee pour avoir, en fonction du libell ́e d’un article et d’un
-- d ́epartement, les quantit ́e en stock de cet article dans les entrepˆots du d ́epartement
-- choisi

prepare qteEnStock from '
select * from ARTICLE natural join ENTREPOT natural join STOCKER 
where libelle = ? and departement = ?';
set @1='Chaise';
set @2='Loiret';
execute qteEnStock using @1, @2;

-- Exercice 2 TD :Proc ́edures et fonctions
-- 1. Ecrire une fonction maxRefArticle qui retourne la plus grande r ́ef ́erence utilis ́ee pour
-- identifier un article. (0 si la table article est vide).

delimiter |
create or replace function maxRefArticle() returns int
begin
    declare res int;
    select ifnull(max(reference),0) into res from ARTICLE;
    return res;
end |
delimiter ;

select maxRefArticle();

-- 2. Ecrire une fonction deptEntrepot(codeEnt int) qui retourne le d ́epartement ou se
-- trouve l’entrepˆot de code codeEnt.

delimiter |
create or replace function deptEntrepot(codeEnt int) returns Varchar(30)
begin
    declare res Varchar(30) ;
    select departement into res from ENTREPOT where code = codeEnt;
    if res is null then
        set res = 'n existe pas';
    end if;
    return res;
end |
delimiter ;

select deptEntrepot(4);

-- 3. Ecrire une fonction valEntrepot(codeEnt int) qui retourne la valeur des marchan-
-- dises contenues dans l’entrepˆot codeEnt.

delimiter |
create or replace function valEntrepot(codeEnt int) returns float
begin
    declare res float;
    select sum(quantite * prix) into res from STOCKER natural join ARTICLE where code = codeEnt;
    return res;
end |
delimiter ;

select valEntrepot(1);

-- 4. Ecrire une proc ́edure pour afficher tous les entrepˆots.

delimiter |
create or replace procedure afficheEntrepot()
begin
    declare code Varchar(30);
    declare nom Varchar(30);
    declare departement Varchar(30);
    declare res Varchar(500) default ' ';
    declare fini boolean default false ;
    declare entrepots cursor for
        select * from ENTREPOT;
    declare continue handler for not found set fini = true ;

    open entrepots;

    while not fini do
        fetch entrepots into code , nom, departement ;
        if not fini then
            set res = concat(res , code , ' ' , nom , ' ' , departement, ' / ') ;
        end if;
    end while;
    close entrepots;
    select res;
end |
delimiter ;

call afficheEntrepot();


-- 5. Ecrire une proc ́edure pour afficher tous les entrepˆots tri ́es par d ́epartement avec pour
-- chaque d ́epartement, le nombre d’entrepˆots qu’a le d ́epartement.

delimiter |
create or replace procedure afficheEparDepartement()
begin 
    declare codeE int;
    declare nomE Varchar(30);
    declare departementE Varchar(30);
    declare departementPrec Varchar(30) default ' ';
    declare nbE int default 0;
    declare fini boolean default false;
    declare res Varchar(500) default ' ';
    declare entrepots cursor for
        select code, nom, departement from ENTREPOT order by departement ;
    declare continue handler for not found set fini = true ;

    open entrepots;

    while not fini do
        fetch entrepots into codeE, nomE, departementE;
        if not fini then
        if departementPrec != departementE then
            set nbE = nbE + 1;
            set res = concat(res , 'soit un total de ', nbE , ' entrepot dans le departement : ', departementE, '\n');
        else 
            set nbE = 0;
        end if;    
            set res = concat(res,' ' ,codeE, '   ', nomE, '\n');
        end if;
        set departementPrec = departementE;
    end while;

    close entrepots;

    select res;

end |
delimiter ;

call afficheEparDepartement();


-- 6. Ajouter `a l’affichage pr ́ec ́edent, la valeur contenue dans chaque entrepˆot.


delimiter |
create or replace procedure afficheEparDepartement()
begin 
    declare codeE int;
    declare nomE Varchar(30);
    declare departementE Varchar(30);
    declare departementPrec Varchar(30) default ' ';
    declare valeur float default 0;
    declare nbE int default 0;
    declare fini boolean default false;
    declare res Varchar(500) default ' ';
    declare entrepots cursor for
        select code, nom, departement, sum(quantite * prix) from ENTREPOT natural join STOCKER natural join ARTICLE group by code order by departement ;
    declare continue handler for not found set fini = true ;

    open entrepots;

    while not fini do
        fetch entrepots into codeE, nomE, departementE, valeur;
        if not fini then
        if departementPrec != departementE then
            set nbE = nbE + 1;
            set res = concat(res , 'soit un total de ', nbE , ' entrepot dans le departement : ', departementE, '\n');
        else 
            set nbE = 0;
        end if;    
            set res = concat(res,' ' ,codeE, '   ', nomE, ' ', valeur, '\n');
        end if;
        set departementPrec = departementE;
    end while;

    close entrepots;

    select res;

end |
delimiter ;

call afficheEparDepartement();


-- 7. Ecrire une fonction qui permet de stocker un nouvel article dans la table article ou de
-- modifier le prix d’un article d ́ej`a existant. Par exemple majArticle(123, ’tuile17x27’,
-- 3.55) modifiera le prix de l’article 123 s’il existe et qu’il correspond `a ’tuile 17x27’,
-- si ne nom n’est pas ’tuile17x27’ afficher un message d’erreur, si l’article 123 n’est
-- pas dans la base ajouter un nouvel article en prenant comme r ́ef ́erence la plus grande
-- des r ́ef ́erences pr ́esentes dans la base plus 1 `a la place de 123. La fonction retournera
-- la r ́ef ́erence de l’article cr ́e ́e ou modifi ́e (-1 si erreur).

delimiter |
create or replace function majArticle(referenceA int, libelleA Varchar(30) , prixA float) returns int
begin 
    declare exist int default 0;
    select reference into exist from ARTICLE where reference = referenceA;

    if exist then
        update ARTICLE set libelle = libelleA, prix = prixA where reference = referenceA;
    else 
        insert into ARTICLE values (referenceA, libelleA, prixA);
    end if;
    return referenceA;
end |
delimiter ;


select majArticle(1, 'bla', 0.12);


-- 8. Ecrire une fonction entrerStock(refA int, codeE int, qte int) qui augmente le
-- stock de l’article refA dans l’entrepˆot codeE de qte. Retourne la nouvelle quantit ́e de
-- l’article (-1) quand l’article ou l’entrepˆot n’existe pas.

delimiter |
create or replace function entrerStock(refA int, codeE int, qte int) returns float
begin
    declare nouvQte float default 0;
    select quantite into nouvQte from STOCKER where reference = refA and code = codeE;
    if nouvQte then 
        set nouvQte = nouvQte + qte;
        update STOCKER set quantite = nouvQte where code = codeE and reference = refA;
        return nouvQte;
    else 
        return -1;
    end if;
end |
delimiter ;

select entrerStock(1, 1, 6);



-- 9. Ecrire une fonction sortirStock(refA int, codeE int, qte int) qui diminue le
-- stock de l’article refA dans l’entrepˆot codeE de qte. La quantit ́e `a sortir est limit ́ee `a
-- la quantit ́e pr ́esente. Retourne la quantit ́e r ́eellement sortie.

delimiter |
create or replace function entrerStock(refA int, codeE int, qte int) returns float
begin
    declare nouvQte float default 0;
    select quantite into nouvQte from STOCKER where reference = refA and code = codeE;
    if nouvQte then 
        set nouvQte = nouvQte - qte;
        if nouvQte < 0 then
            return -1;
        elseif nouvQte = 0 then
            delete from STOCKER where code = codeE and reference = refA;
            return nouvQte;
        else 
            update STOCKER set quantite = nouvQte where code = codeE and reference = refA;
            return nouvQte;
        end if;
    else 
        return -1;
    end if;
end |
delimiter ;

select entrerStock(1, 1, 6);


-- 1. On ne veut pas avoir plusieurs entrepˆots avec le mˆeme nom dans le mˆeme d ́epartement.

delimiter |
create or replace trigger nomUniqueDepartement before insert on ENTREPOT for each row
begin
    declare nomD Varchar(50);
    declare mes Varchar(100) default ' ';
    select nom into nomD from ENTREPOT where departement = NEW.departement and nom = NEW.nom limit 1;
    if nomD is not NULL then
        set mes = concat( 'inscription impossible') ;
        signal SQLSTATE '45000' set MESSAGE_TEXT = mes ;
    end if;
end |
delimiter ;

-- insert into ENTREPOT values(4, 'Orléans nord', 'Loiret');

-- 2. On ne veut pas plus de trois entrepˆots dans un mˆeme d ́epartement.

delimiter |
create or replace trigger pasPlusDe3 before insert on ENTREPOT for each row
begin
    declare nb int;
    declare mes Varchar(100) default ' ';
    select ifnull(count(*), 0) into nb from ENTREPOT where departement = NEW.departement;
    if nb >= 3 then
        set mes = concat( 'inscription impossible') ;
        signal SQLSTATE '45000' set MESSAGE_TEXT = mes ;
    end if;
end |
delimiter ;

-- 3. A chaque fois que le stock d’un article est modifi ́e (`a la hausse ou `a la baisse), on veut
-- conserver une trace de la mise `a jour


delimiter |
create or replace trigger metDansLhisto after update on STOCKER for each row
begin
    declare mes Varchar(100) default ' ';
    if OLD.quantite > NEW.quantite then
        set mes = concat('retrait de ', OLD.quantite - NEW.quantite);
    else
        set mes = concat('ajout de ', NEW.quantite - OLD.quantite);
    end if;
    insert into HISTORIQUE(mess, dateMess) VALUES (mes, CURDATE());
end |
delimiter ;

update STOCKER set quantite = 4 where reference = 1 and code = 1;