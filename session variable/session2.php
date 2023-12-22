<?php
session_start();
$x=$_SESSION['username'];
$y=$_SESSION['mobile'];
echo"name is".$x."<br>number is ".$y;
session_destroy();
?>