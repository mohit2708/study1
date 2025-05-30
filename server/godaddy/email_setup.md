### Check email Routing
* go to cpanel -> email routing -> select the **Local Mail Exchanger**
* add the dns
  * A	    mail	    107.180.114.129(enter cpanel ip)	               10800 seconds
  * TXT	    @	        v=spf1 include:secureserver.net -all	           1 Hour
  * TXT	    admin	    v=spf1 a mx ptr include:secureserver.net ~all	   1 Hour
  * CNAME	webmail	    zoencure.com.	                                   10800 seconds