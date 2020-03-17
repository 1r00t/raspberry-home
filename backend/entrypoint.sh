#!/bin/sh

# start crond
echo "- STARTING CROND!!!! -"
/usr/sbin/crond -f -l 8

# start flask
echo "- STARTING FLASK!!!! -"
flask run
