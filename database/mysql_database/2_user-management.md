|  No.  | [Mysql User Management](#mysql-user-management)                                    |
| :---: | ---------------------------------------------------------------------------------- |
|       | [Create Databse user?](#create-user)                                               |
|       | [Show Databse user?](#show-all-users)                                              |
|       | [Show Current user?](#show-current-user)                                           |
|       | [User Password Change?](#user-password-change)                                     |
|       | [Drop User?](#drop-user)                                                           |
|       | [Grant Privileges to the MySQL New User?](#grant-privileges-to-the-mysql-new-user) |
|       | [Show Privileges?](#show-privileges)                                               |
|       | [REVOKE Privileges?](#revoke-privileges)                                           |

### **Create User**
```sql
CREATE USER username@hostname IDENTIFIED BY 'password';  
CREATE USER username IDENTIFIED BY 'password'; -- The hostname is optional
```

#### Show all Users
```sql
SELECT user, host FROM mysql.user;
+----------+-----------+
| user     | host      |
+----------+-----------+
| root     | localhost |
| newuser  | localhost |
| admin    | %         |
+----------+-----------+
```

#### Show Current User
```sql
SELECT USER();
Select current_user();
```
<div style="page-break-before: always;"></div>

#### User Password Change
```sql
SET PASSWORD FOR 'mohits4'@'hostname' = PASSWORD('jtp12345');  -- older versions
-- new version
ALTER USER mohits4@hostname IDENTIFIED BY 'jtp123';

-- iF current user logged-in: 
SET PASSWORD = 'new_password';
-- After password change:
FLUSH PRIVILEGES;
```

#### Drop User
```sql
DROP USER mohits4@localhost;  
--can also be used to remove more than one user accounts at once.
DROP USER john@localhost, peter@localhost;  
```
<div style="page-break-before: always;"></div>

#### Grant Privileges to the MySQL New User
1. **ALL PRIVILEGES**: It permits all privileges to a new user account.
2. **CREATE**: Allows the user to create new databases, tables, indexes, views, or stored procedures.
3. **DROP**: Allows the user to delete (drop) existing databases, tables, views, or other objects.
4. **DELETE**: It enables the user account to delete rows from a specific table.
5. **INSERT**: It enables the user account to insert rows into a specific table.
6. **SELECT**: It enables the user account to read a database.
7. **UPDATE**: It enables the user account to update table rows.

[ ] Note:- Sometimes, you want to flush all the privileges of a user account for changes occurs immediately
```sql
FLUSH PRIVILEGES;
```

```sql
-- 1. The first asterisk (*) refers to all databases
-- 2. The second asterisk (*) refers to all tables
GRANT CREATE, SELECT ON database_name.* TO 'username'@'host';

-- If you want to give all privileges to a newly created user, execute the following command.
GRANT ALL PRIVILEGES ON * . * TO username@hostname;

-- If you want to give specific privileges to a newly created user, execute the following command.
GRANT CREATE, SELECT, INSERT ON * . * TO username@hostname;
```

#### Show Privileges
```sql
SHOW GRANTS for mohits4;
SHOW GRANTS FOR 'local_user'@'localhost';
-- if user loged in
SHOW GRANTS;
```

#### REVOKE Privileges
```sql
REVOKE ALL PRIVILEGES ON *.* FROM 'mohits4'@'hostname';
-- If you want to remove specific privileges to a newly created user
REVOKE SELECT ON *.* FROM 'mohits4'@'hostname';
-- Revoke **all privileges** on a specific **database**:
REVOKE ALL PRIVILEGES ON database_name.* FROM 'mohits4'@'hostname';
-- Revoke **SELECT privilege** on a **specific** **table**:
REVOKE SELECT ON database_name.table_name FROM 'mohits4'@'hostname';
```