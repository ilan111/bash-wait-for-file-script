#!/bin/bash
FILE="$1"
TIMEOUT="$2"
for second in $(seq 1 $TIMEOUT)
do
    if [ -e /home/ubuntu/$FILE ]
        then
            echo $second
            exit 0
    fi
    sleep 1
done
echo "-1"
exit 1