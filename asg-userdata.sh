#!/bin/bash
yum update -y
yum install -y nginx
systemctl start nginx
systemctl enable nginx
echo "Hello from ASG instance" > /usr/share/nginx/html/index.html
