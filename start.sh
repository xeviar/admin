#!/bin/bash

DIR=`dirname $0`
cd $DIR
echo $DIR
#python manage.py   runserver 0.0.0.0:8080 >>$DIR/web.log 2>&1
python manage.py   runserver 0.0.0.0:8080
#python manage.py runfcgi host=127.0.0.1 port=9090 pidfile=/tmp/admin.pid
