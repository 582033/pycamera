#!/bin/bash

process_name='shot.py'
path='/opt/pycamera/'

function daemon(){
    result=`ps aux | grep $process_name | grep python | awk '{print $2}'`
    if test -z $result;then
        nohup python $path$process_name > /dev/null 2>&1 &
    else
        echo "$process_name is running!"
    fi
}

daemon
