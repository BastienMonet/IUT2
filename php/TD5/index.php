<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="post" action="">
        <button name=delete>Delete all</button>
        <input type="text" name=name>
        <button type="submit" name="insert">ajouter</button>
    </form>

    <?php
    require_once "insertion.php";

    $fruits = ["Pomme", "Banane", "Orange"];

    if (isset($_POST['insert']) && !empty($_POST['name'])) {
        insertBD(mt_rand(1,100), $_POST['name'], 32);
        printAll();
    } else if (empty($_POST['name'])) {
        echo "Le champ nom est vide.<br>";
    }

    if (isset($_POST['delete'])) {
        $co = connectBD();
        $sql = "DELETE FROM COMPANY";
        $count = $co->exec($sql);
        echo $count . " ligne effacée(s).<br>";
    }
    ?>

</body>
</html>