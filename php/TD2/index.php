<?php include '_inc/templates/filter.php'; 
require '_inc/data/product.php';
$parsedData = getProduct();?>

<link rel="stylesheet" href="/style.css">

<div class="container">
    

<p>mes produits </p>

<form action="index.php" method="get"> 
    <div>
        <input type="text" id="name" name="title" />
        
    </div>
    <div>
        <?php
            
            $marques = getListMarque($parsedData);

            echo "<input type=\"radio\" id=\"brand\" name=\"brand\" value=\"\">";

            foreach ($marque as $marques) {
                echo " <input type='radio' id='brand' name='brand' value=".$marques.">";
                echo " <label for=''>".$marques."</label>";
            }

        ?>
    </div>
    <button type="submit"> Rechercher</button>
</form>


<?php
    

    if ($_GET["brand"]) {
        $parsedData = filterByBrand($parsedData);
    } else {
        $parsedData = filterByTitre($parsedData);
    }
    
    
    foreach ($parsedData as $item) {
        echo "<p><strong> <a href='detail.php?id=".$item["id"]. "'>" .$item["title"]."</a>". $item["brand"]."</strong></p>";
    }
    ?>
</div>
</body>
</html>




