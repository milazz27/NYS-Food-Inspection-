<?php

class Database {
    private $host = "127.0.0.1";
    private $port = "5432";
    private $dbname = "food_safety";
    private $user = "postgres";
    private $password = "postgres";

    public function connect(){
        # Data Source Name = establishing database address
        $dsn = "pgsql:host={$this->host};port={$this->port};dbname={$this->dbname}";

        try {
            # Trying to open connection to the database and creating a db connection object
            $pdo = new PDO($dsn, $this->user, $this->password, [
                # if query fails --> throw error immediately
                PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                # queries come back like ["violation_code" => "10A"]
                PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
            ]);
            return $pdo;
        }
        catch (PDOException $e){
            die("DB connection error: " . $e->getMessage());
        }
    }
}


