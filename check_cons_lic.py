import sys
import os
import re

bufsize = 8192
cfile = 'C:\inetpub\wwwroot\cons\system\srvprot.txt'
#lines = int(sys.argv[1])
lines = 1
#fname = sys.argv[2]
fsize = os.stat(cfile).st_size

iter = 0
with open(cfile) as f:
    if bufsize > fsize:
        bufsize = fsize-1
    data = []
    while True:
        iter +=1
        f.seek(fsize-bufsize*iter)
        data.extend(f.readlines())
        if len(data) >= lines or f.tell() == 0:
            result = re.search('\s[0-9]{2,3}\s',''.join(data[-lines:]))
            res = re.search('[0-9]{2,3}',result[0])
            print(res[0])
            break