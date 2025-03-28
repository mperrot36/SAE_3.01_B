#!/usr/bin/zsh

while true; do
    ping -w1 $1 >> /dev/null

    if [ "$?" == "1" ]; then 
        # change route
        echo oui
    fi
done