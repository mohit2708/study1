### How to setup a fresh AWS EC2 instance
* Go to the EC2 Instance
* click on the Launch Instance button.
* Enter Name:- My Web Server
* Select the Ubuntu Server
* By defalt select t2Micro (Instance type)
* Create new key pair
  * Enter Key pair name
  * Select RSA -> .pem
  * click on the button **Create Key Pair**
* Network Setting
  * Tick Allow SSH traffic from
  * Tick Allow SSH traffic from
  * Tick Allow SSH traffic from
Finally Click on the **Lunch Instance** Button

### Download Pem file convert into ppk file
* Open PuttyGen
* Load pem file 
* Save
* download ppk file save in secure folder in your system

### Open Putty 
* input the ip
* upload the ppk file

### Install the Apache Web Server on Ubuntu 20.04
* sudo apt update
* sudo apt install apache2
* sudo systemctl status apache2
```php
apache2.service - The Apache HTTP Server
     Loaded: loaded (/lib/systemd/system/apache2.service; enabled; vendor preset: enabled)
     Active: active (running) since Mon 2023-10-09 16:38:22 UTC; 28s ago
       Docs: https://httpd.apache.org/docs/2.4/
   Main PID: 2354 (apache2)
      Tasks: 55 (limit: 1141)
     Memory: 4.9M
        CPU: 29ms
     CGroup: /system.slice/apache2.service
             ├─2354 /usr/sbin/apache2 -k start
             ├─2356 /usr/sbin/apache2 -k start
             └─2357 /usr/sbin/apache2 -k start
```
* Check your url **http://your_server_ip**

### Install PHP
* sudo apt update
* sudo apt install --no-install-recommends php8.1
* php -v
* sudo apt-get install -y php8.1-cli php8.1-common php8.1-mysql php8.1-zip php8.1-gd php8.1-mbstring php8.1-curl php8.1-xml php8.1-bcmath

### Install Composer
* curl -sS https://getcomposer.org/installer -o /tmp/composer-setup.php
* HASH=`curl -sS https://composer.github.io/installer.sig`
* echo $HASH
```aws
Output 
55ce33d7678c5a611085589f1f3ddf8b3c52d662cd01d4ba75c0ee0459970c2200a51f492d557530c71c15d8dba01eae
```
* php -r "if (hash_file('SHA384', '/tmp/composer-setup.php') === '$HASH') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
* sudo php /tmp/composer-setup.php --install-dir=/usr/local/bin --filename=composer
```aws
Output
All settings correct for using Composer
Downloading...

Composer (version 2.3.5) successfully installed to: /usr/local/bin/composer
Use it: php /usr/local/bin/composer
```
* composer


### Install Phpmyadmin
* sudo apt install phpmyadmin
* enter password ...


### phpmyadmin is not working after I installed it
go to this path /etc/apache2/apache2.conf
* add this line
```aws
Include /etc/phpmyadmin/apache.conf
```

### Install MySQL
* sudo apt update
* sudo apt install mysql-server
* sudo systemctl start mysql.service
* sudo systemctl status mysql.service
* To Check:-
  * sudo mysql
  * GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;
  * FLUSH PRIVILEGES;

### To check mysql
```php
ubuntu@ip-172-31-47-243:~$ sudo mysql -u admin -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 41
Server version: 8.0.34-0ubuntu0.22.04.1 (Ubuntu)

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> exit;
Bye
```

### 
* sudo systemctl restart apache2
* sudo systemctl status apache2

### How to check which server installed
```aws
netstat -tulnp
```


### install unzip 
```aws
sudo apt install unzip
```

### Set permission
```aws
sudo chmod -R 777 /var/www
sudo chmod -R 777 /home/oceanside/storage/logs/
ls -l
```
sudo chmod -R 777 /var/www/html/storage

++++++++++++++++++++++++++++++++++++++++++++++++++




### **Mysql cmd:-**
1. connect database
```sql
mysql -u user_name  -p
mysql -u staging_user  -p /pass- staging_user@1234
password:
```

2. SHOW DATABASES;
3. use databses_name;
4. show tables;
5. Delete table from the databses
```sql
DROP TABLE table_name;
```

6. Show the datatype in table
```sql
SHOW COLUMNS FROM table_name;
```

7. Import database:-
```sql
mysql -u user_name -p database_name < var/www/html/db/table.sql;
mysql -u staging_user -p staging_traffic < var/www/html/db/actions_buttons.sql;
```

8. Export Databse:-
```sql
mysqldump -u user_name -p database_name --ignore-table=job_equipment.job_equipment > /var/www/html/db/table.sql
```

9. delete the folder or file:-
```sql
rm -rf /var/www/example
```

10. Unzip The folder
```sql
unzip file_name.zip
```


sudo chmod -R 777 /var/www/html/routes/web.php


SQL Query
* ALTER TABLE `table_name` ADD `new_field_name` VARCHAR(255) NULL AFTER `field_name`;

ALTER TABLE `dispatch_pickup_time_logs` ADD `job_equipment_id` VARCHAR(255) NULL AFTER `id`;



