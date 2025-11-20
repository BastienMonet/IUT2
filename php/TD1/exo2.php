
<?php

function estCoteServeur(int $langage) : null
{
    $langageServeur = ["php", "python"];
    $res = [];
    foreach ($langages as $l){
        if (in_array($l , $langageServeur)){
            array_push($res, $l);
        }
    }
}

$langage = ["php", "html", "css", "python"]



?>