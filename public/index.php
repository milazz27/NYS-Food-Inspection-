<?php

require_once __DIR__ . '/../Config/config.php';

$db = new Database();
$pdo = $db->connect();

# testing 
$stmt = $pdo->query("SELECT NOW()");
echo json_encode($stmt->fetch());