<?php

declare(strict_types=1);


abstract class Input {

    protected boolean $required;

    protected string $name;

    protected string $id;

    protected string $content;

    public function __constructor(string $id, string $name, string $content, boolean $required){
        $this->$id = $id;
        $this->$name = $name; 
        $this->$required = $required;

    }

    protected abstract function render();

}

final class TextFiled extends Input {

    public function __constructor(string $id, string $name, string $content, boolean $required){
        Input::__constructor();
    }

    public function render() {
        return "<input for='text' name='{$name}' id='{$id}'>{$content}</input>";
    }

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
    <?php

    $textfiled = new TextFiled(1, 2, "hello", true);
    echo $textfiled->render();

    ?>
</body>
</html>