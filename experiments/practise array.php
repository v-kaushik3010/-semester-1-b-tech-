
<?php
//INDEXED ARRAY
/*$arr0=array("volvo", "chervolet", "BMW");
$len=count($arr0);
//echo (" \ni like $arr0[0], $arr0[1] and $arr0[2]");

//for ($x=0; $x<$len; $x++) 
//{
  //  echo"$arr0[$x]<br>";   
//}

foreach($arr0 as $x){
    echo "$x <br>";
}*/

#associative array 
/*$arr=array("volvo"=>3, "bmw"=>5, "bucatti"=>2);
echo"i have ". $arr["volvo"]." volvos<br>";
echo"i have ". $arr["bmw"]." BMW<br>";
echo"i have ". $arr["bucatti"]." bucatti<br>";

foreach ($arr as $car=>$have){
    echo "i have ".$have. $car."<br>";
}*/

//multidimensional array

$cars = array (
  array("Volvo",22,18),
  array("BMW",15,13),
  array("Saab",5,2),
  array("Land Rover",17,15)
);
  
echo $cars[0][0].": In stock: ".$cars[0][1].", sold: ".$cars[0][2].".<br>";
echo $cars[1][0].": In stock: ".$cars[1][1].", sold: ".$cars[1][2].".<br>";
echo $cars[2][0].": In stock: ".$cars[2][1].", sold: ".$cars[2][2].".<br>";
echo $cars[3][0].": In stock: ".$cars[3][1].", sold: ".$cars[3][2].".<br><br><br>";

for($r=0; $r<4;$r++){
  echo"row number".$r."<br>";

  for ($c=0;$c<3;$c++){
    echo $cars[$r][$c]."<br>";
  }
}

?>
