#!/bin/sh

# start crond
echo "- STARTING CROND!!!! -"
/usr/sbin/crond -f -l 8

# start flask
echo "- STARTING FLASK!!!! -"
export FLASK_APP="/code/app.py"
#export FLASK_ENV=development
export FLASK_RUN_HOST="0.0.0.0"
flask run &> flask.log