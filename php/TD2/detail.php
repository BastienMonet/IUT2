<?php
    require '_inc/data/product.php';

    $parsedData = getProduct();

    if (isset($_GET["id"])){
        $product = array_filter($parsedData, function($item) {
            return $item["id"] == $_GET["id"];
        });
    }

    if (count($product) === 1) {
        $product = array_values($product)[0];
    } else {
        $exp = "Produit non trouvé ou ID invalide.";
    }


    if (isset($exp)) {
            echo "<p> id :" . $exp . "non trouver </p>";
            echo '<a href="index.php">retour</a>';
            exit;
        }
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <p>Détail du produit</p>
    <?php
        echo "Détails du produit sélectionné ici.";
        echo "<h2>". $product["title"] . "</h2>";
        echo "<p> ". $product["description"] ."</p>"
    ?>
    <a href="index.php">retour</a>
</body>
</html>