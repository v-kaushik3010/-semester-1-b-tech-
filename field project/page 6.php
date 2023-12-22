<?php
//$username = $_REQUEST["h1"];
//$email = $_REQUEST["h2"];
//$purpose = $_REQUEST["h3"];
$username = "varun";
$email = "varun@ gmak";
$purpose = " just to do nothing ";
echo "<table width='100%' border='1' 
       style='border-collapse: collapse; border: 3px solid grey;'>";
echo "<tr style='background-color:  #2eb82e;'>";
echo "<th>Name</th>";
echo "<th>E-Mail</th>";
echo "<th>Purpose</th>";
echo "</tr>";

echo "<tr>";
echo "<td>$username</td>";
echo "<td>$email</td>";
echo "<td>$purpose</td>";
echo "</tr>";

echo "</table>";
?>
