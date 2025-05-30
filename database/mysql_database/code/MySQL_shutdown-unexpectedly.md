### How to fix MySQL shutdown unexpectedly?
* https://www.webfulcreations.com/fix-error-mysql-shutdown-unexpectedly-in-xampp/
1. Rename the folder xampp/mysql/data to xampp/mysql/data_bk
2. Create a new folder xampp/mysql/data
3. copy all all backup folder data(Xampp8.1.6\mysql\backup) to data folder(xampp/mysql/data)
4. copy the ibdata1 file from xampp/mysql/data_bk and replace it inside xampp/mysql/data folder
5. finaly copy the database from xampp/mysql/data_bk to xampp/mysql/data folder
