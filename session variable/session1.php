<?php
session_start();



$a=$_POST["t1"];
$b=$_POST["t2"];
echo"mobile number is $b and name is $a <br><br>";


$_SESSION['username']=$a;
$_SESSION['mobile']=$b;
echo"<a href=session2.php>Next</a>";
?>

