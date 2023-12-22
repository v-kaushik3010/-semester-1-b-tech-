<?php
// process.php
include('config.php');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Handle form submission
    $student_id = $_POST['student_id'];
    $student_name = $_POST['student_name'];
    $amount_paid = $_POST['amount_paid'];
    $balance_amount = 100000 - $amount_paid;
    $data = "$student_id,$student_name,$amount_paid,$balance_amount," . date("Y-m-d") . PHP_EOL;
    file_put_contents($dataFilePath, $data, FILE_APPEND | LOCK_EX);
    header("Location: index3.php");
}
else{
    echo"not corect";
}
?>
