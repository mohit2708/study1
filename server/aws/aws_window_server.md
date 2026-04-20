### How to configration project to IP
- setup project in C:\xampp\htdocs\project_name


### Open httpd-vhosts.conf
- C:\xampp\apache\conf\extra\httpd-vhosts.conf
```
<VirtualHost *:80>
    ServerName your-public-ip
    DocumentRoot "C:/xampp/htdocs/project_name/public"

    <Directory "C:/xampp/htdocs/project_name/public">
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>

```
- Replace:
  - your-public-ip → AWS Public IPv4 address
  - myproject → your Laravel folder name


### Enable Virtual Hosts
- open file C:\xampp\apache\conf\httpd.conf
```
# Make sure this line is NOT commented:
Include conf/extra/httpd-vhosts.conf
```

### Fix Laravel .env
```
APP_URL=http://YOUR_PUBLIC_IP
```
```
php artisan config:clear
php artisan cache:clear
```