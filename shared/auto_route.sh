#!/usr/bin/bash

priority=$1

RBAS="172.16.31.227"
REDU="172.16.31.226"
RCRI="172.16.31.225"



if [ "$priority" != "BAS" ] && [ "$priority" != "EDU" ] && [ "$priority" != "CRI" ]; then
    echo /!\\ error: priority needs to be either BAS, EDU or CRI
    exit 1
fi



if [ "$priority" == "BAS" ]; then
    routeur1=$RBAS
    routeur2=$REDU
    routeur3=$RCRI
elif [ "$priority" == "EDU" ]; then
    routeur1=$REDU
    routeur2=$RBAS
    routeur3=$RCRI
elif [ "$priority" == "CRI" ]; then
    routeur1=$RCRI
    routeur2=$REDU
    routeur3=$RBAS
fi


gateway=$routeur1


change_gateway() {
    local old_gateway=$1
    local new_gateway=$2
    ip route del default via $old_gateway dev eth0
    ip route add default via $new_gateway dev eth0
}


while true; do

    new_gateway=$gateway

    ping -w1 routeur1 >> /dev/null
    ping_r1=$?

    ping -w1 routeur2 >> /dev/null
    ping_r2=$?

    ping -w1 routeur3 >> /dev/null
    ping_r3=$?

    if [ "$ping_r1" == "0" ]; then
        new_gateway=$routeur1
    elif [ "$ping_r1" == "1" ]; then 
        new_gateway=$routeur2
    elif [ "$ping_r1" == "1" ] && [ "$ping_r2" == "1" ]; then
        new_gateway=$routeur3
    elif [ "$ping_r1" == "1" ] && [ "$ping_r2" == "1" ] && [ "$ping_r3" == "1" ]; then
        echo "there's nothing we can do..."
    fi

    if [ "$new_gateway" != "$gateway" ]; then
        change_gateway $gateway $new_gateway
        gateway=$new_gateway
    fi

done