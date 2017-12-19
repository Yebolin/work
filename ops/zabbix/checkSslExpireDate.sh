#!/bin/bash
# 用户检查 ssl证书的有效时间
# $1:host   $2:port default 443
# 返回天数
# v1.0	bolin 2017-08-08

host=$1
[ -z "$2" ] && port=443

expire_date=$(echo | openssl s_client -connect "$host:$port" 2>/dev/null | openssl x509 -noout -enddate | grep notAfter | cut -d'=' -f2 )
expire_second=$( date -d "$expire_date" +%s)
now_second=$(date +%s)

echo "( $expire_second - $now_second )/3600/24" | bc