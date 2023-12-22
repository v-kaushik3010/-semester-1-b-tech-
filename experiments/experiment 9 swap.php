<?php

// Function to swap two integers using call by value
function swapByValue($a, $b) {
    $temp = $a;
    $a = $b;
    $b = $temp;
    echo "Inside swapByValue function:\n";
    echo "a: $a, b: $b\n";
}

// Function to swap two integers using call by reference
function swapByReference(&$a, &$b) {
    $temp = $a;
    $a = $b;
    $b = $temp;
    echo "Inside swapByReference function:\n";
    echo "a: $a, b: $b\n";
}

// Initial values
$x = 5;
$y = 10;

// Display initial values
echo "Before swapping:\n";
echo "x: $x, y: $y\n";

// Swap using call by value
swapByValue($x, $y);

// Display values after call by value
echo "After swapByValue:\n";
echo "x: $x, y: $y\n";

// Swap using call by reference
swapByReference($x, $y);

// Display values after call by reference
echo "After swapByReference:\n";
echo "x: $x, y: $y\n";

?>
