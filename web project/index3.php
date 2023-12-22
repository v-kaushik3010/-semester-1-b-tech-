<?php

include('config.php');

function readDataFromFile($filePath) {
    if (file_exists($filePath)) {
        $data = file_get_contents($filePath);
        $rows = explode(PHP_EOL, $data);
        return array_filter($rows);  // Remove empty lines
    }
    return [];
}


$data = readDataFromFile($dataFilePath);
?>


<h2>Student Details</h2>
<table>
    <thead>
        <tr>
            <th>Student ID</th>
            <th>Student Name</th>
            <th>Amount Paid</th>
            <th>Balance Amount</th>
            <th>Transaction Date</th>
        </tr>
    </thead>
    <tbody>
        <?php foreach ($data as $row): ?>
            <?php list($student_id, $student_name, $amount_paid, $balance_amount, $transaction_date) = explode(',', $row); ?>
            <tr>
                <td><?php echo $student_id; ?></td>
                <td><?php echo $student_name; ?></td>
                <td><?php echo $amount_paid; ?></td>
                <td><?php echo $balance_amount; ?></td>
                <td><?php echo $transaction_date; ?></td>
            </tr>
        <?php endforeach; ?>
    </tbody>
</table>
