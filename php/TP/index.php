<?php
require 'Classes/Autoloader.php';


Autoloader::register();


use View\Template;

// $myDataLoader = new DataLoaderJson();
// $form = $myDataLoader->getData();

// ob_start();
// foreach ($form as $field){
//     $className = 'Form\\Type\\'.ucfirst($field['type']);
//     echo new $className($filed['name'])
// }



$content = "bonjour les enfants";

$template = new Template('templates');
$template->setLayout('main');
$template->setsetContent($content);

echo $template->compile();



$action = $_REQUEST['action'] ?? false;


switch ($action){
    case 'valider':
        include 'Action/anwser.php';
        break;
    default:
        include 'Action/form.php';
        break;
}

?>