#!/bin/sh
#Author: bolin
#Date: 2016-08-19
#Description: redis监控脚本
#Usage:简单的redis监控指标
source /etc/profile


HOST="127.0.0.1"
PORT="6379"
PASS="****"

EXEC="/usr/local/bin/redis-cli -h $HOST -p $PORT -a $PASS"


case $1 in
	keys)
		$EXEC info keyspace | grep keys | cut -d= -f2 | cut -d, -f1 ;;
	expires)
		$EXEC info keyspace | grep keys | cut -d= -f3 | cut -d, -f1 ;;
	avg_ttl)
		$EXEC info keyspace | grep keys | cut -d= -f4 | cut -d, -f1 ;;
	mem)
		$EXEC info memory | grep 'used_memory:' |cut -d: -f2 ;;
	*)
		echo "usage: keys|expires|avg_ttl|mem"
esac

