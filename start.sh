#!/bin/bash

DIR=`dirname $0`
cd $DIR
echo $DIR
#python manager.py   runserver 0.0.0.0:8080 >>$DIR/web.log 2>&1
python manager.py   runserver 0.0.0.0:8080
