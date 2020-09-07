#!/bin/bash

if [ -e "env" ]; then
source env/bin/activate
fi
TRACKINGNUMBER=$1
res=`python track.py $TRACKINGNUMBER`
if ! [ -e "result" ]; then
touch result
fi

res1=`cat result`

if [ "$res" = "$res1" ]; then
echo "No Update"
else
echo $res
fi

echo $res > result
if [ -e "env" ]; then
deactivate
fi
