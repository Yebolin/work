#!/bin/bash
set -e
set -o pipefail


function build(){
  curl -v -X POST -u name:authstring http://192.168.2.99:8080/job/xxxxxxxx/build |& grep '<'
  # sleep 30 waiting job start,if check immediately,will get SUCCESS,have to wait job starting.
  sleep 30
}


function check(){
  for i in {1..30};do
    res=$(curl -s -X POST -u name:authstring "http://192.168.2.99:8080/job/xxxxxxxx/lastBuild/api/json?pretty=true" | jq .result )
    if [ $res == '"SUCCESS"' ];then
      echo "==== build success ===="
      break
    else
      echo "==== $i building ===="
      sleep 15
    fi
done
}

build
check
