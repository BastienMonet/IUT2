<?php
session_start();

require_once '_inc/data/product.php';

$products = getProduct();

if ($_GET["remove-id"]) {
    unset($_SESSION['cart'][$_GET['remove-id']]);
}

if (!empty($_REQUEST['cart'])){
    if ($_SESSION['cart'] && array_key_exists($_REQUEST['cart']['id'], $_SESSION['cart']) ){
        $_SESSION['cart'][$_REQUEST['cart']['id']]['qte'] += $_REQUEST['cart']['qte'];
    } else {
        $_SESSION['cart'][$_REQUEST['cart']['id']] = $_REQUEST['cart'];
    }
}

?>


<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
     echo <<<PANIER
    <table>
        <thead>
            <tr>
                <th>Produit</th>
                <th>Quantité</th>
                <th>Prix Unitaire</th>
                <th>Total</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
    PANIER;

    $total = 0;
    foreach ($_SESSION['cart'] as $key => $value){
        $k = array_search($value['id'],
        array_column($products, 'id')
        );

        $product = $products[$k];
        $lineTotal = $product['price'] * $value['qte'];
        echo <<<LINE
            <tr>
                <td>{$product['title']}</td>
                <td>{$value['qte']}</td>
                <td>{$product['price']} €</td>
                <td>{$lineTotal} €</td>
                <td> <a href=panier.php?remove-id={$product['id']}> supprimer </a> </td>
            </tr>
        LINE;


       
    }

     echo <<<FOOTER
            </tbody>
        </table>

        FOOTER;
    ?>
    <a href="index.php">retour</a>
    
</body>
</html>

