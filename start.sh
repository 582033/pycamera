
# XXX XXX XXX  THIS IS A NEW FILE XXX XXX XXX

#!/bin/sh

#
# start.sh
#
# Developed by UNKNOWN AUTHOR <UNKNOWN@undefined.net>
# Copyright (c) 2013 Platon Group, http://platon.sk/
# Licensed under terms of GNU General Public License.
# All rights reserved.
#
# Changelog:
# 2013-12-22 - created
#

# $Platon$
process_name='shot.py'
path='/root/pycamera/'
####
function daemon(){
	result=`ps aux | grep $process_name | grep python | awk '{print $2}'`
	if test -z $result;then
		nohup python $path$process_name > /dev/null 2>&1 &
	else
		echo "$process_name is running!"
	fi
}

daemon
