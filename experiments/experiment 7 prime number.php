<?php
$number=15;

for($j=2;$j<=$number;$j++){
  $flag=True;

   for($i=2; $i<$j;$i++)
   {
     $y=$j%$i;

     if( $y!=0)
     {
       
        continue;
     }
     else{
        $flag=False;
     }
    }
    if ($flag==True){
        echo"$j is a prime number<br>";
      }
   }
?>