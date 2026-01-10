<?php
require_once "connexion.php";

function insertBD($id, $name, $age) {
    $co = connectBD();
    $sql = "Insert into COMPANY (ID, NAME, AGE, SALARY) values (:id, :name, :age, 0)";
    $statement = $co->prepare($sql);
    $statement->bindParam(":id", $id, PDO::PARAM_INT);
    $statement->bindParam(":name", $name, PDO::PARAM_STR);
    $statement->bindParam(":age", $age, PDO::PARAM_INT);
    $statement->execute(); 
}


function printAll() {
    $co = connectBD();
    $sql = "select * from COMPANY";
    $stmt = $co->query($sql);
    foreach ($stmt as $row) {
        echo "ID: " . $row['ID'] . "<br>";
        echo "NAME: " . $row['NAME'] . "<br>";
    }
}


?>