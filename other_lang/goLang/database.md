### Connect the databse mysql

* Create database folder and create file **connection.go**
```go
// connection.go
package database

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/go-sql-driver/mysql"
)

var DB *sql.DB

func init() {
	// Database connection parameters
	username := "root"
	password := ""
	host := "localhost"
	port := "3306"
	dbName := "go_proj"

	// Create a database URL
	dataSourceName := fmt.Sprintf("%s:%s@tcp(%s:%s)/%s", username, password, host, port, dbName)

	// Open a database connection
	db, err := sql.Open("mysql", dataSourceName)
	if err != nil {
		log.Fatal(err)
	}

	// Check if the connection is successful
	err = db.Ping()
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Connected to the database!")

	DB = db
}
```


* call connection in main file
```go
package main

import (
	"firstProject/database"
	"fmt"
)
func main() {
	// Use the initialized database connection
	fmt.Println("asfsaf")
	db := database.DB
	defer db.Close()

	// Your database-related code goes here
}
```