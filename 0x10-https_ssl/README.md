# setting up https

# \#10 Tutorial:
- https://serversforhackers.com/c/letsencrypt-with-haproxy
- (INSIDE YOUR LB SERVER)
- sudo apt-get update
- sudo apt-get install -y certbot
- (manually) put the following into the frontend section of the ha_proxy config file (/etc/haproxy/haproxy.cfg)
- Underneath bind *:80 line :
-  	# Test URI to see if its a letsencrypt request
-  	acl letsencrypt-acl path_beg /.well-known/acme-challenge/
-  	use_backend letsencrypt-backend if letsencrypt-acl
- And then put this at the very end of the /etc/haproxy/haproxy.cfg file:
-	\# LE Backend
-	backend letsencrypt-backend
-  		server letsencrypt 127.0.0.1:8888
- then run -
- sudo service haproxy reload
- then (UPDATE THESE WITH YOUR INFO)-
- sudo certbot certonly --standalone -d www.<yourdomainname>.tech --non-interactive --agree-tos --email 	<youremailaddress> --http-01-port=8888
- (At this point you should have successfully created a certificate) :D
- NEXT (UPDATE THESE WITH YOUR INFO):
- sudo mkdir -p /etc/ssl/www.<yourdomainname>.tech
- And then (UPDATE THESE WITH YOUR INFO):
- sudo cat /etc/letsencrypt/live/www.<yourdomainname>.tech/fullchain.pem /etc/letsencrypt/live/www.<yourdomainname>.tech/privkey.pem | sudo tee /etc/ssl/www.<yourdomainname>.tech/www.<yourdomainname>.tech.pem
- NEXT:
- Add this line to the frontend section of /etc/haproxy/haproxy.cfg (underneath the bind *:80 line)
- with your info
-	bind *:443 ssl crt /etc/ssl/www.<yourdomainname>.tech/www.<yourdomainname>.tech.pem
- NOTE:
- In this section:
- backend web_servers
-    balance roundrobin
-    mode http
-    server 2327-web-01 35.237.166.125:80
-    server 2327-web-02 54.167.61.201:80
- /etc/haproxy/haproxy.cfg
- you must have the port specification :80 on the end of your server IPs
- you should be able to curl and be good to go at that point 

# commands to get certbot

-    sudo apt get-update
-    sudo apt get-upgrade
-    sudo apt-get install software-properties-common
-    sudo add-apt-repository ppa:certbot/certbot
-    sudo apt-get update
-    sudo apt-get upgrade
-    sudo apt-get install -y certbot
-    sudo apt-get install python-certbot-nginx
-    sudo apt-get update
-    sudo apt-get upgrade

