<?php

//inclusão de classes

include_once("../../lis/home.class.php");
include_once("../../upd/home.php");
include_once("../../lis/login.class.php");
include_once("../../connect/conexao.class.php");
include_once("../../ins/cadastroUsuario.class.php");

$view = file_get_contents("../error/404.html");
$structure = file_get_contents("../estruturas/index.php");

$pagina = $_GET['pagina'];
$tipo   = $_GET['tipo'];

$connection_db = connectdb::getConnection();

ob_start();
switch($tipo)
{
    case "delete":;
    break;
    case "insert":($pagina."Insert")::executar($connection_db);
    break;
    case "list":($pagina."List")::executar($connection_db);
    break;
    case "update":($pagina."Update")::executar();
    break;
    case "view": if(file_get_contents("../".$pagina.".html")){$view = file_get_contents("../".$pagina.".html");echo $view;}else{echo $view;};
    break;
    default:echo $view;
    break;
}

$content = ob_get_clean();

$template = str_replace("{{{struct}}}",$content,$structure);

echo $template;
