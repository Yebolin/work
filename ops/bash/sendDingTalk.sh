#!/bin/bash
# dingTalk webhook for send text message
# bolin 2018-3-30

TOKEN=$1
MSG=$2
cd $(dirname $0)
exec 1>>log.log
exec 2>>log.log

function generate_data(){
  cat << EOF
{
        "msgtype": "text",
        "text": {
                "content": "$1"
        }
}
EOF
}

date +"%F %T"
echo $(generate_data $MSG)
curl -H 'Content-Type: application/json' -d "$(generate_data $MSG)" -s "https://oapi.dingtalk.com/robot/send?access_token=$TOKEN"
echo ""
