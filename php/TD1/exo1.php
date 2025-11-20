#!/usr/bin/php script.php
<?php

function estPair(int $nb) : bool
{
    return $nb % 2 == 0;
}

for ($i=0; $i<10; $i++) {
  echo "The number is $i " . (estPair($i) ? "est pair" : "n'est pas pair") . "\n";
}

var_dump($argv); // arguments de la cli

echo "Nombre : $nb\n";


$colors = array("Red", "Green", "Blue");

foreach ($colors as $key=>$value) {
  echo "$key : $value \n";
}

?>