prepare CreeSalle from 'insert into SALLE values( ?, ?, ?)';
set @ids = 123;
set @nomS = 'michel';
set @capa = 12;
execute CreeSalle using @ids, @nomS, @capa;


delete from SALLE where ids=123;
deallocate prepare CreeSalle;








