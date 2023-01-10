import sys
import os
import re

bufsize = 8192
cfile = 'C:\inetpub\wwwroot\cons\system\srvprot.txt'
lines = 1
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
            line=''.join(data[-lines:])
            res=line.split()
            print(int(res[5]))
            break
