
|  No.  | [Questions]()                                                                                                 |
| :---: | ------------------------------------------------------------------------------------------------------------- |
|       | [How to copy files to another folder?](#how-to-copy-the-entire-folder-contents-to-another-folder-using-putty) |
|       | [How to zip?](#how-to-zip)                                                                                    |



### How to Remove a Directory in Linux
* To remove a file, say test.txt, you can use the command without options like this:
```php
rm test.txt
```
* How to delete a folder with contents
```php
rm -r test
```
* How to delete an empty folder
```php
rm -d test
```

### How to Copy the entire folder contents to another folder using PUTTY
cp -r /var/www/html/* /var/www/html/7may2023bkp


cp -r * /var/www/html/7may2023bkp



### Create the zip file for particular folder
sudo zip -r filename.zip foldername/


### How to copy files to another folder
```php
cp -r /var/www/html/* /var/www/html/bkp
```

### How to zip
```php
zip -r vendorbkp.zip vendorbkp
```
