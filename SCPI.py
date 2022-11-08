from telnetlib import Telnet
tn=Telnet('192.168.29.2', 5555) ## IP EB500
f=open('./RDSFM.txt','r',encoding="utf-8")
inst1 = f.readline()
inst2= f.readline()
inst3= f.readline()
print(inst1)
print(inst2)
print(inst3)

x4=inst2 + "\n"
x3=inst1 + "\n"
x5=inst3 + "\n"
tn.write(x3.encode('utf-8'))
tn.write(x4.encode('utf-8'))
tn.write(x5.encode('utf-8'))
f.close()
