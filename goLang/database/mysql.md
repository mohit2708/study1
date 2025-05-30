```go
// connection.go

package database

import (
	"database/sql"
	"fmt"
	"log"

	_ "github.com/go-sql-driver/mysql"
)

// InitDB initializes the database connection
// func InitDB() (*sql.DB, error) {
// 	// Database connection parameters
// 	username := "root"
// 	password := ""
// 	host := "localhost"
// 	port := "3306"
// 	dbName := "go_proj"

// 	// Create a database URL
// 	dataSourceName := fmt.Sprintf("%s:%s@tcp(%s:%s)/%s", username, password, host, port, dbName)

// 	// Open a database connection
// 	db, err := sql.Open("mysql", dataSourceName)
// 	if err != nil {
// 		return nil, err
// 	}

// 	// Check if the connection is successful
// 	err = db.Ping()
// 	if err != nil {
// 		return nil, err
// 	}

// 	fmt.Println("Connected to the database!")

// 	return db, nil
// }

var DB *sql.DB

func init() {
	err := godotenv.Load()
	if err != nil {
		log.Fatal("Error loading .env file")
	}

	// Database connection parameters
	username := os.Getenv("DB_USERNAME")
	password := os.Getenv("DB_PASSWORD")
	host := os.Getenv("DB_HOST")
	portStr := os.Getenv("DB_PORT")
	dbName := os.Getenv("DB_NAME")

	// Convert port to int
	port, err := strconv.Atoi(portStr)
	if err != nil {
		log.Fatal("Error converting port to integer")
	}

	// Create a database URL
	dataSourceName := fmt.Sprintf("%s:%s@tcp(%s:%d)/%s", username, password, host, port, dbName)

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

### Create **.env** file in root folder
```go
DB_USERNAME=root
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=3306
DB_NAME=go_proj
```