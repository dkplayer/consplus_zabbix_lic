import sys, os, re, io
import datetime
now = datetime.datetime.now()
cfile = 'C:\inetpub\wwwroot\cons\system\srvprot.txt'

#проверка аргументов коммандной строки. принимает единственный параметр - имя домена по которому вывести количество сессий
if len(sys.argv)>1:
    checkdom = sys.argv[1].upper()
else:
    checkdom = ''

#список доменов
domains={'DOMAIN1':0, 'DOMAIN2':0, 'DOMAIN3':0}

date=now.strftime("%d.%m.%Y,")
iter = 0
users=set()
with io.open(cfile, encoding='windows-1251', errors='ignore') as lic:
    for line in lic:
        rec=line.split()
        if rec[2]!="SetAuth":
            if rec[0]==date:
                dom=rec[6].split('\\')
                if rec[2]=='Create':
                    users.add(rec[6])
                if rec[2]=='Delete':
                    users.discard(rec[6])
for user in users:
   dom=user.split('\\')
   domains[dom[0].upper()]+=1

#если не указан конкретный домен выводит список доменов с количеством открытых сессий по каждому домену    
if checkdom != '':
    print(domains[checkdom])
else:
    for domain,cnt in domains.items():
        print(domain,cnt)