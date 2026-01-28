### How do you back up a MySQL database?
- Use the **mysqldump** command to export a database. Example:
```git
mysqldump -u username -p database_name > backup.sql
```

### How do you restore a MySQL database?
- Use the mysql command to import a backup. Example:
```git
mysql -u username -p database_name < backup.sql
```