#!/usr/bin/env bash 
SCRIPT=${BASH_SOURCE[0]}
SCRIPTPATH=$(dirname $SCRIPT)
echo "$SCRIPT"
echo "$SCRIPTPATH"
cd ${SCRIPTPATH}
pwd
pip3 install -r requirements.txt
python3 ./markdown2mindnode.py $*