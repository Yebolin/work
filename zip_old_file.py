#!/usr/bin/python
# remove old file,and zip to dst
# bolin 2017-12-14

import os
import time
import zipfile

# init
SRC = r'f:\test'
DST = r'f:'
DAYS = 7

# time
now = time.time()
expireTimestamp = now - now % 86400 - 86400 * DAYS

zipFileName = 'bak' + time.strftime('%Y%m%d') + '.zip'
zipFileFullName = os.path.join(DST, zipFileName)

myzip = zipfile.ZipFile(zipFileFullName, 'a')

# find file
os.chdir(SRC)  # change dir to src, make the zip file have relative path
for root, dirs, files in os.walk('.'):
    for file in files:
        cur = os.path.join(root, file)
        if os.path.getmtime(cur) < expireTimestamp:
            myzip.write(cur)
            os.remove(cur)

myzip.close()
