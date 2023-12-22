<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    $email = $_POST["email"];
    $password = $_POST["password"];

    
    $correctEmail = "user@example.com";
    $correctPassword = "password123";

    if ($email == $correctEmail && $password == $correctPassword) {
        
        echo "Login successful. Welcome, $email!";
        
    } else {
        echo "Login failed. Please check your email and password.";
    }
}
?>
