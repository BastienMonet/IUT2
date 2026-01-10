<?php

class Autoloader{
    static function register(){
        sql_autoload_register(array(__CLASS__, 'autoload'));
    }

    static function autoload($fqcn){
        $path = str_replace('\\', '/', $fqcn);
        require sprintf("Classes/$path.php");

    }
}


?>
