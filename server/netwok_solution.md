


### Network Solution renew
#### Genrate the CSR file and private key on aws server
```php
https://help.101domain.com/kb/how-to-generate-a-csr-for-aws-services
https://www.digicert.com/kb/csr-ssl-installation/apache-openssl.htm
```
#### Certificate Key Matcher
* crt and key matcher on google serch (or) https://www.sslshopper.com/certificate-key-matcher.html
* upload the crt file and key file.

#### genrate the matcher file
* search "pfx converter" on google (Or) https://www.sslshopper.com/ssl-converter.html
* File form-> 
  * Certificate File to Convert -> upload domain.crt file 
  * Type of Current Certificate -> selsct option standerd PEM
  * Type To Convert To -> PFX/PKCS#12
  * password -> 12345
  * private key file -> upload private .key file genrate first time(during crt create)

```php
# network solution ssl

Using username "ubuntu".
Authenticating with public key "imported-openssh-key"
Welcome to Ubuntu 22.04.2 LTS (GNU/Linux 6.8.0-1017-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Wed Dec 11 16:25:12 UTC 2024

  System load:  0.0                Processes:             119
  Usage of /:   36.8% of 15.32GB   Users logged in:       0
  Memory usage: 44%                IPv4 address for eth0: 172.31.47.245
  Swap usage:   0%

 * Ubuntu Pro delivers the most comprehensive open source security and
   compliance features.

   https://ubuntu.com/aws/pro

Expanded Security Maintenance for Applications is not enabled.

91 updates can be applied immediately.
1 of these updates is a standard security update.
To see these additional updates run: apt list --upgradable

11 additional security updates can be applied with ESM Apps.
Learn more about enabling ESM Apps service at https://ubuntu.com/esm

New release '24.04.1 LTS' available.
Run 'do-release-upgrade' to upgrade to it.


*** System restart required ***
Last login: Tue Dec 10 16:49:54 2024 from 14.99.194.2
ubuntu@ip-172-31-47-245:~$ sudo su
root@ip-172-31-47-245:/home/ubuntu# ls
beachservice.key  csr.pem  localhost.key  www_beachservice_com.csr  www_beachservice_com.key
root@ip-172-31-47-245:/home/ubuntu# cd /etc/apache2/sites-enabled/
root@ip-172-31-47-245:/etc/apache2/sites-enabled# ls
clipboard.beachservice.com.conf
root@ip-172-31-47-245:/etc/apache2/sites-enabled# cat clipboard.beachservice.com.conf
<VirtualHost *:80>
   ServerName staging-clipboard.beachservice.com
    DocumentRoot /var/www/html/public/
    ErrorLog /var/log/apache2/clipboard.beachservice.com_error.log
    CustomLog /var/log/apache2/clipboard.beachservice.com_access.log combined
RewriteEngine on
RewriteCond %{SERVER_NAME} =www.staging-clipboard.beachservice.com [OR]
RewriteCond %{SERVER_NAME} =staging-clipboard.beachservice.com
RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>

<VirtualHost *:443>
    ServerName staging-clipboard.beachservice.com
    ServerAlias www.staging-clipboard.beachservice.com
    DocumentRoot /var/www/html/public/
    ErrorLog /var/log/apache2/clipboard.beachservice.com_error-SSL.log
    CustomLog /var/log/apache2/clipboard.beachservice.com_access_SSL.log combined
    SSLEngine on
    SSLCertificateFile /etc/apache2/ssl/STAR.BEACHSERVICE.COM.crt
    SSLCertificateKeyFile /etc/apache2/ssl/BeachService.key
    SSLCertificateChainFile /etc/apache2/ssl/gd_bundle-g2-g1.crt
   # SSLCertificateChainFile /etc/ssl/OV_NetworkSolutionsOVServerCA2.crt
</VirtualHost>


root@ip-172-31-47-245:/etc/apache2/sites-enabled# cd ../ssl
root@ip-172-31-47-245:/etc/apache2/ssl# ls
BeachService.key  STAR.BEACHSERVICE.COM.crt  gd_bundle-g2-g1.crt  ssl-old
root@ip-172-31-47-245:/etc/apache2/ssl# mkdir old_11122024
root@ip-172-31-47-245:/etc/apache2/ssl# mv BeachService.key STAR.BEACHSERVICE.COM.crt gd_bundle-g2-g1.crt old_11122024/
root@ip-172-31-47-245:/etc/apache2/ssl# ls
old_11122024  ssl-old
root@ip-172-31-47-245:/etc/apache2/ssl# cd /home/ubuntu/
root@ip-172-31-47-245:/home/ubuntu# ls
beachservice.key  csr.pem  localhost.key  www_beachservice_com.csr  www_beachservice_com.key
root@ip-172-31-47-245:/home/ubuntu# mkdir old
root@ip-172-31-47-245:/home/ubuntu# mv beachservice.key csr.pem www_beachservice_com.csr www_beachservice_com.key old/
root@ip-172-31-47-245:/home/ubuntu# ls
localhost.key  old
root@ip-172-31-47-245:/home/ubuntu# ls
localhost.key  net_sol_new_ssl  old
root@ip-172-31-47-245:/home/ubuntu# mv net_sol_new_ssl/ /etc/apache2/ssl
root@ip-172-31-47-245:/home/ubuntu# cd /etc/apache2/ssl
root@ip-172-31-47-245:/etc/apache2/ssl# ls
net_sol_new_ssl  old_11122024  ssl-old
root@ip-172-31-47-245:/etc/apache2/ssl#
root@ip-172-31-47-245:/etc/apache2/ssl# ls
net_sol_new_ssl  old_11122024  ssl-old
root@ip-172-31-47-245:/etc/apache2/ssl# cd net_sol_new_ssl/
root@ip-172-31-47-245:/etc/apache2/ssl/net_sol_new_ssl# ls
BEACHSERVICE.COM.crt  BEACHSERVICE.COM.pfx  SSL_WILDCARD_IntermediateCA_3.crt  private.key
root@ip-172-31-47-245:/etc/apache2/ssl/net_sol_new_ssl# mv BEACHSERVICE.COM.crt private.key ../.
root@ip-172-31-47-245:/etc/apache2/ssl/net_sol_new_ssl# cd ..
root@ip-172-31-47-245:/etc/apache2/ssl# ls
BEACHSERVICE.COM.crt  net_sol_new_ssl  old_11122024  private.key  ssl-old
root@ip-172-31-47-245:/etc/apache2/ssl# cd ../sites-enabled/
root@ip-172-31-47-245:/etc/apache2/sites-enabled# ls
clipboard.beachservice.com.conf
root@ip-172-31-47-245:/etc/apache2/sites-enabled# vi clipboard.beachservice.com.conf
root@ip-172-31-47-245:/etc/apache2/sites-enabled# systemctl restart apche2
Failed to restart apche2.service: Unit apche2.service not found.
root@ip-172-31-47-245:/etc/apache2/sites-enabled# apachectl -t
AH00526: Syntax error on line 21 of /etc/apache2/sites-enabled/clipboard.beachservice.com.conf:
SSLCertificateChainFile: file '/etc/apache2/ssl/gd_bundle-g2-g1.crt' does not exist or is empty
Action '-t' failed.
The Apache error log may have more information.
root@ip-172-31-47-245:/etc/apache2/sites-enabled# vi clipboard.beachservice.com.conf
root@ip-172-31-47-245:/etc/apache2/sites-enabled# apachectl -t
Syntax OK
root@ip-172-31-47-245:/etc/apache2/sites-enabled# systemctl restart apache2
root@ip-172-31-47-245:/etc/apache2/sites-enabled# chalana
==================production=================

*** System restart required ***
Last login: Thu Nov  7 11:27:49 2024 from 14.99.194.2
ubuntu@ip-172-31-47-243:~$ sduo su
Command 'sduo' not found, did you mean:
  command 'sudo' from deb sudo (1.9.9-1ubuntu2.4)
  command 'sudo' from deb sudo-ldap (1.9.9-1ubuntu2.4)
Try: sudo apt install <deb name>
ubuntu@ip-172-31-47-243:~$ sudo su
root@ip-172-31-47-243:/home/ubuntu# ls
ne_sol_ssl_new
root@ip-172-31-47-243:/home/ubuntu# cd ne_sol_ssl_new/
root@ip-172-31-47-243:/home/ubuntu/ne_sol_ssl_new# cd /etc/apache2/sites-enabled/
root@ip-172-31-47-243:/etc/apache2/sites-enabled# ls
clipboard.beachservice.com.conf  www.clipboard.beachservice.com.conf
root@ip-172-31-47-243:/etc/apache2/sites-enabled# cat clipboard.beachservice.com.conf
<VirtualHost *:80>
   ServerName clipboard.beachservice.com
   ServerAlias www.clipboard.beachservice.com

   Redirect permanent / https://clipboard.beachservice.com


    DocumentRoot /var/www/html/public/
    ErrorLog /var/log/apache2/clipboard.beachservice.com_error.log
    CustomLog /var/log/apache2/clipboard.beachservice.com_access.log combined
#RewriteEngine on
#RewriteCond %{SERVER_NAME} =www.clipboard.beachservice.com [OR]
#RewriteCond %{SERVER_NAME} =clipboard.beachservice.com
#RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>



<VirtualHost *:443>
    ServerName clipboard.beachservice.com
    ServerAlias www.clipboard.beachservice.com
    <If "%{HTTP_HOST} == 'www.clipboard.beachservice.com'">
    Redirect permanent / https://clipboard.beachservice.com/
    </If>
    DocumentRoot /var/www/html/public/
    ErrorLog /var/log/apache2/clipboard.beachservice.com_error-SSL.log
    CustomLog /var/log/apache2/clipboard.beachservice.com_access_SSL.log combined
    SSLEngine on
    SSLCertificateFile /etc/apache2/ssl/STAR.BEACHSERVICE.COM.crt
    SSLCertificateKeyFile /etc/apache2/ssl/BeachService.key
   SSLCertificateChainFile /etc/apache2/ssl/gd_bundle-g2-g1.crt
   # SSLCertificateChainFile /etc/ssl/OV_NetworkSolutionsOVServerCA2.crt
</VirtualHost>
root@ip-172-31-47-243:/etc/apache2/sites-enabled# cat www.clipboard.beachservice.com.conf
<VirtualHost *:80>
   ServerName www.clipboard.beachservice.com
#<VirtualHost *:443>
#   ServerName clipboard.beachservice.com
#    ServerAlias www.clipboard.beachservice.com
#    DocumentRoot /var/www/html/public/
#    ErrorLog /var/log/apache2/clipboard.beachservice.com_error-SSL.log
#    CustomLog /var/log/apache2/clipboard.beachservice.com_access_SSL.log combined
#    SSLEngine on
#    SSLCertificateFile /etc/ssl/NetworkSolutionsRSAOVSSLCA3.crt
#    SSLCertificateKeyFile /etc/ssl/STAR.BEACHSERVICE.COM.crt
#    SSLCertificateChainFile /etc/ssl/OV_NetworkSolutionsOVServerCA2.crt
#</VirtualHost>



    DocumentRoot /var/www/html/public/
    ErrorLog /var/log/apache2/clipboard.beachservice.com_error.log
    CustomLog /var/log/apache2/clipboard.beachservice.com_access.log combined
RewriteEngine on
RewriteCond %{SERVER_NAME} =www.clipboard.beachservice.com [OR]
RewriteCond %{SERVER_NAME} =clipboard.beachservice.com
RewriteRule ^ https://%{SERVER_NAME}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>



#<VirtualHost *:443>
#    ServerName clipboard.beachservice.com
#    ServerAlias www.clipboard.beachservice.com
#    DocumentRoot /var/www/html/public/
#    ErrorLog /var/log/apache2/clipboard.beachservice.com_error-SSL.log
#    CustomLog /var/log/apache2/clipboard.beachservice.com_access_SSL.log combined
#   SSLEngine on
   # SSLCertificateFile /etc/ssl/NetworkSolutionsRSAOVSSLCA3.crt
   # SSLCertificateKeyFile /etc/ssl/ov_chain.key
    #SSLCertificateChainFile /etc/ssl/OV_NetworkSolutionsOVServerCA2.crt
#</VirtualHost>
root@ip-172-31-47-243:/etc/apache2/sites-enabled#
root@ip-172-31-47-243:/etc/apache2/sites-enabled# cd -
/home/ubuntu/ne_sol_ssl_new
root@ip-172-31-47-243:/home/ubuntu/ne_sol_ssl_new# ls
BEACHSERVICE.COM.crt  BEACHSERVICE.COM.pfx  private.key
root@ip-172-31-47-243:/home/ubuntu/ne_sol_ssl_new# cd -
/etc/apache2/sites-enabled
root@ip-172-31-47-243:/etc/apache2/sites-enabled# cd ../ssl/
root@ip-172-31-47-243:/etc/apache2/ssl# ls
BeachService.key  STAR.BEACHSERVICE.COM.crt  gd_bundle-g2-g1.crt
root@ip-172-31-47-243:/etc/apache2/ssl# mkdir old
root@ip-172-31-47-243:/etc/apache2/ssl# mv BeachService.key STAR.BEACHSERVICE.COM.crt gd_bundle-g2-g1.crt old/
root@ip-172-31-47-243:/etc/apache2/ssl# mv /home/ubuntu/ne_sol_ssl_new/* .
root@ip-172-31-47-243:/etc/apache2/ssl# ls
BEACHSERVICE.COM.crt  BEACHSERVICE.COM.pfx  old  private.key
root@ip-172-31-47-243:/etc/apache2/ssl# cd ../sites-enabled/
root@ip-172-31-47-243:/etc/apache2/sites-enabled# ls
clipboard.beachservice.com.conf  www.clipboard.beachservice.com.conf
root@ip-172-31-47-243:/etc/apache2/sites-enabled# vi clipboard.beachservice.com.conf
root@ip-172-31-47-243:/etc/apache2/sites-enabled# systemctl restart apache2
root@ip-172-31-47-243:/etc/apache2/sites-enabled# chalo
```