<?php
declare(strict_type=1);

namespace view;

final class Template{
    private string $path;
    private string $layout;
    private string $content;

    public function __construct(string $path){
        $this->path = $path;
    }

    public function getPath():string{
        return $this->path;
    }

    public function getLayout():string{
        return $this->layout;
    }

    public function getContent():string{
        return $this->layout;
    }

    public function setPath(string $path){
        $this->path = $path;
    }

    public function setLayout(string $layout){
        $this->layout = $layout;
    }

    public function setContent(string $content){
        $this->content = $content;
    }

    public function compile():string{
        $content = $this->content;
        ob_start();
        require sprintf(
            '%s/%s.php',
            $this->getPath(),
            $this->getLayout()
        );
        return ob_get_clean();
    }

}
?>