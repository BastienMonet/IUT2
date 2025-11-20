<?php


function getProduct(){
    $data = file_get_contents('json.json');

    return json_decode($data, true);
}

function filterByBrand($parsedData) {
    if (!empty($_GET["brand"])){
        $parsedData = array_filter($parsedData, fn($item) => str_contains(strtoupper($item["brand"]), strtoupper($_GET["brand"])));
    }
    return $parsedData;
}

function filterByTitre($parsedData) {
    if (!empty($_GET["title"])){
        $parsedData = array_filter($parsedData, fn($item) => str_contains(strtoupper($item["title"]), strtoupper($_GET["title"])));
    }
    return $parsedData;
}


function getListMarque($parsedData){
    $res = array();
    foreach ($parsedData as $item){
        array_push($res,$item["brand"]);
    }
    return $res;
}


?>