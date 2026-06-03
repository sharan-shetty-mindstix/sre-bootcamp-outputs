#!/bin/bash
yum update -y
yum install -y nginx
systemctl start nginx
systemctl enable nginx
echo "Response from Instance 2" > /usr/share/nginx/html/index.html
