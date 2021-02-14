#配置---------------
ipl=500
#请输入IP连接数阈值
import os
import time
#os.system("netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n")
while True:
    a = os.popen("netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -n")  
    a = a.read()
    lj=[]
    ip=[]
    for line in a.splitlines():
        #print("---"+line+"---")
        b=" "
        c=0
        d=len(line)
        while b==" " and c<=d:
            b=line[c]
            c=c+1
        #print("--"+b+"--")
        cc=c-1
        while b != " " and c<=d:
            b=line[c]
            c=c+1
        ccc=c
        while b==" " and c<=d:
            b=line[c]
            c=c+1
        ipa=c-1
        while b != " " and c<d:
            b=line[c]
            c=c+1
        ipb=c
        #print("--"+a+"--")
        #print(d)
        #print(line[cc:ccc])
        lj.append(line[cc:ccc])#连接数
        ip.append(line[ipa:ipb])#ip
    #print(lj)
    #print(ip)
    c=0
    for i in lj:
        if int(i)>=int(ipl):
            print("""------
            已封禁ip: """+ip[c]+"""
            ------""")
            os.system("iptables -I INPUT -s "+ip[c]+" -j DROP")
        c=c+1
    time.sleep(1)