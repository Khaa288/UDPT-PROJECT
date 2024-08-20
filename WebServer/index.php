<?php
session_start();
require_once("./controller/PublicController.php");

$action = "";
if (isset($_REQUEST["action"]))
{    
    $action = $_REQUEST["action"];
}
 
switch ($action)
{       
    default:
        $controller = new PublicController();
        $controller->index();
}
?>
