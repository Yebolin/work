#!/usr/bin/python
# remove old file,and zip to dst
# bolin 2017-12-14
# v0.2 use argparse

import os
import time
import zipfile
import argparse


parser = argparse.ArgumentParser(description='zip old file')
parser.add_argument('-s', '--src', dest='src', required=True, help='src file path')
parser.add_argument('-d', '--dst', dest='dst', required=True, help='dst file path')
parser.add_argument('-e', dest='day', required=True, type=int, help='expire day,old file day')
args = parser.parse_args()
# args = parser.parse_args(['-s','ss','-d','dd','-e', '99'])

# init
SRC = args.src
DST = args.dst
DAYS = args.day

# make dirs
if not os.path.exists(DST):
    os.makedirs(DST)

# time
now = time.time()
expireTimestamp = now - now % 86400 - 86400 * DAYS

zipFileName = 'bak' + time.strftime('%Y%m%d') + '.zip'
zipFileFullName = os.path.join(DST, zipFileName)

myzip = zipfile.ZipFile(zipFileFullName, 'a', zipfile.ZIP_DEFLATED)

# find file
os.chdir(SRC)  # change dir to src, make the zip file have relative path
for root, dirs, files in os.walk('.'):
    for file in files:
        cur = os.path.join(root, file)
        if os.path.getmtime(cur) < expireTimestamp:
            myzip.write(cur)
            os.remove(cur)

myzip.close()
