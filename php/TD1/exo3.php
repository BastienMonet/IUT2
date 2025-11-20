
<?php

require_once 'exo1.php';

echo estPair(4) . " \n";

function carre(int| float $nombre){
    return $nombre**2;
}

if (empty($argv[1])){
    throw new Exception("Veuillez fournir un nombre en argument");
}

echo sprintf("Le carré de %s est %s", $argv[1], carre($argv[1]));


?>