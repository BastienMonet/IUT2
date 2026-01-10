<?php
function connectBD() {
    $dsn = "sqlite:./db.sqlite";
    try {
        $connection = new PDO($dsn);
    } catch (PDOException $e) {
        printf("Echec de la co, t nul");
        exit();
    }
    return $connection;
}

?>