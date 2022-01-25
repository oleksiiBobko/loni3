#!/bin/bash

if [ "$1" = "" ] ; then
    echo "Usage backup-lots.sh <filename>"
    exit
fi
for i in 0 1 2 3 4 5 6 7 8 9 ; do
    NEW_FILE=$1.BAK-$i
    if [ -e $NEW_FILE ] ; then fi
done
