<?php
$username = $_POST["h1"];
$gender = $_POST["h2"];

if ($gender == "male") {
  echo "Hello, Mr. $username";
} elseif ($gender == "female") {
  echo "Hello, Mrs. $username";
}
?>
