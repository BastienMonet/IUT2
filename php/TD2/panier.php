<?php
session_start();

require_once '_inc/data/product.php';

$products = getProduct();

if (!empty($_REQUEST['cart'])){
    $_SESSION['cart'][$_REQUEST[['cart']['id']]] = $_REQUEST['cart'];
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
        $lineTotal = $product['price'] * $value['quantity'];
        echo <<<LINE
            <tr>
                <td>{$product['title']}</td>
                <td>{$value['quantity']}</td>
                <td>{$product['price']} €</td>
                <td>{$lineTotal} €</td>
            </tr>
        LINE;


        echo <<<FOOTER
        </tbody>
        <table>

        FOOTER;
    }
    ?>
    
</body>
</html>

